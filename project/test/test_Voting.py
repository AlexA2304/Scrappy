#!/usr/bin/python3
import os
import json
import unittest
from app import app
from const.dbNames import projectDB

# Purpose: This file tests the voting api
# Author: Jarryd Allison
# Usage: run python3 ./test_Voting.py

# Headers
headers = { "Content-Type": "application/json" }

# Story ID omitted error
storyIDError = {'error':'Story ID must be specified'}
# Username omitted error
usernameError = {'error':'Username must be specified'}
# Vote value omitted error
voteValError = {'error':'Vote must be specified'}
# Vote value not supported
voteValNotSupportedError = {'error':'Vote must be in options [1, 2, 3, 5, 8, 13]'}

def success(type: str):
    return {'success':'vote '+type+' success'}

class TestVotingApi(unittest.TestCase):

    # This setup should be common to all tests
    @classmethod
    def setUpClass(self) -> None:
        # Set the test client for the entire test suite
        self.client = app.test_client()
        if (os.getcwd().split('/')[-1] != 'test'):
            # Ensuring the directory is correct is beyond this scope. Just gracefull fail
            # if the directory is incorrect
            print("Tests must be run in the /test directory only.")
            self.fail()
        try:
            os.remove(os.getcwd()+'/project.db')
        except OSError:
            # Don't do anything here. If there was an error,
            # it means the file likely doesn't exist, which is good.
            return
        
    @classmethod
    def tearDownClass(self) -> None:
        try:
            os.remove(os.getcwd()+'/project.db')
        except OSError as error:
            print("There was an error attempting to delete project.db:", error)

    # Function to insert/update the vote table
    def mutate(self, type: str, storyID: int, username: str, voteVal: int):
        # send data as POST form to endpoint
        return self.client.post(
            '/vote/'+type,
            data='{ "storyID":"'+str(storyID)+'", "username":"'+username+'", "vote":"'+str(voteVal)+'"}',
            headers=headers
        )
    
    # Function to query the vote table
    # Supports all querys: findAll, findByID, doVotesExist, findByUsername, and findByVote
    def query(self, type: str):
        return self.client.get('/vote/'+type)
    
    # Function that returns an array of json values
    def checkJSON(self, result, check):
        return [json.dumps(result.json), json.dumps(check)]

    # Test the insert function
    def test_1_insert_success(self):
        # Insert a vote for storyID 1
        check = self.checkJSON(self.mutate('insert', 1, 'test_user_1', 1), success('insert'))
        self.assertEqual(*check)
        # Now ensure the insert worked by querying the vote table and checking the value
        check  = self.checkJSON(self.query('findAll'), [{"storyID":1, "username":"test_user_1", "vote":1}])
        self.assertEqual(*check)
    
    # Test the insert function failure
    def test_2_insert_failure(self):
        # Check error for inserting an incorrect vote
        check = self.checkJSON(self.mutate('insert', 1, 'test_user_2', 4), voteValNotSupportedError)
        # check result from server with expected data
        self.assertEqual(*check)
        # Check error for omitting storyID
        check = self.checkJSON(self.mutate('insert', "", 'test_user_2', 4), storyIDError)
        self.assertEqual(*check)
        # Check error for omitting Username
        check = self.checkJSON(self.mutate('insert', 1, '', 4), usernameError)
        self.assertEqual(*check)
        # Check error for omitting Vote
        check = self.checkJSON(self.mutate('insert', 1, 'test_user_2', 0), voteValError)
        self.assertEqual(*check)
        # Now ensure the insert failed by querying the vote table
        check = self.checkJSON(self.query('findAll'), [{"storyID":1, "username":"test_user_1", "vote":1}])
        self.assertEqual(*check)
    
    # Test the update function
    def test_3_update_success(self):
        check = self.checkJSON(self.mutate('update', 1, 'test_user_1', 2), success('update'))
        self.assertEqual(*check)
        # Now ensure the insert worked by querying the vote table
        check = self.checkJSON(self.query('findAll'), [{"storyID":1, "username":"test_user_1", "vote":2}])
        self.assertEqual(*check)

    def test_4_update_failure(self):
        # Check error for omitting storyID
        check = self.checkJSON(self.mutate('update', "", 'test_user_2', 4), storyIDError)
        self.assertEqual(*check)
        # Check error for omitting Username
        check = self.checkJSON(self.mutate('update', 1, '', 4), usernameError)
        self.assertEqual(*check)
        # Check error for omitting Vote
        check = self.checkJSON(self.mutate('update', 1, 'test_user_2', 0), voteValError)
        self.assertEqual(*check)
        # check for vote doesn't exist
        check = self.checkJSON(self.mutate('update', 2, 'test_user_1', 1), { 'error':'The vote does not exist'})
        self.assertEqual(*check)
        # check for invalid vote update value
        check = self.checkJSON(self.mutate('update', 2, 'test_user_1', 20), voteValNotSupportedError)
        self.assertEqual(*check)
        # And ensure the vote table wasn't actually edited
        check = self.checkJSON(self.query('findAll'), [{"storyID":1, "username":"test_user_1", "vote":2}])
        self.assertEqual(*check)
    
    # Test findAll
    def test_5_findAll(self):
        # Add another vote
        self.mutate('insert', 1, 'test_user_2', 3)
        check = self.checkJSON(self.query('findAll'), [
            {"storyID":1, "username":"test_user_1", "vote":2},
            {"storyID": 1, "username": "test_user_2", "vote": 3}
        ])
        self.assertEqual(*check)
    
    # Test findByID
    def test_6_findByID(self):
        # Insert a new storyID vote
        self.mutate('insert', 2, 'test_user_2', 3)
        # Ensure the second storyID isn't included
        check = self.checkJSON(self.query('findByID/1'), [
            {"storyID":1, "username":"test_user_1", "vote":2},
            {"storyID":1, "username": "test_user_2", "vote": 3}
        ])
        self.assertEqual(*check)

    # Test doVotesExist
    def test_7_getVotes(self):
        check = self.checkJSON(self.query('doVotesMatch/1/2'), { "match": False })
        self.assertEqual(*check)
        check = self.checkJSON(self.query('doVotesMatch/2/1'), { "match": True })
        self.assertEqual(*check)

    # Test findByUsername
    def test_8_findByUsername(self):
        check = self.checkJSON(self.query('findByUsername/test_user_2'), [
            {"storyID": 1, "username": "test_user_2", "vote": 3},
            {"storyID": 2, "username": "test_user_2", "vote": 3}
        ])
        self.assertEqual(*check)

    # Test findByVote
    def test_9_findByVote(self):
        check = self.checkJSON(self.query('findByVote/3'), [
            {"storyID": 1, "username": "test_user_2", "vote": 3},
            {"storyID": 2, "username": "test_user_2", "vote": 3}
        ])
        self.assertEqual(*check)

# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()