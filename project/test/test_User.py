import unittest
from app import app
import os
import json
from const.dbNames import projectDB

# Purpose: This file tests the login and signup api
# Author: Charlie Bailey
# Usage: from the /test directory run python3 ./test_User.py

class TestUserApi(unittest.TestCase):

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

    # Test adding a user via signup
    def test_1_signup_success(self):
        # create new username and password data to be added
        data = {
            'username': 'testuser1',
            'password': 'testingpw1'
        }

        # make the post request
        response = self.client.post('/signup', json=data, follow_redirects=True)

        # check that status code is 200 ok
        self.assertEqual(response.status_code, 200)

        # check that the page is redirected to /createMeeting
        self.assertEqual(response.request.path, '/createMeeting')

    # Test trying to add a username that already exists
    def test_2_signup_failure(self):
        data = {
            'username': 'testuser1',
            'password': 'differenttestpw'
        }

        # make the post request
        response = self.client.post('/signup', json=data, follow_redirects=True)

        # check that status code is 409 conflict
        self.assertEqual(response.status_code, 409)

    # try logging in with an existing username and password
    def test_3_login_success(self):
        data = {
            'username': 'testuser1',
            'password': 'testingpw1'
        }

        # make the post request
        response = self.client.post('/login', json=data, follow_redirects=True)

        # check that status code is 200 ok
        self.assertEqual(response.status_code, 200)

        # check that the page is redirected to /createMeeting
        self.assertEqual(response.request.path, '/createMeeting')

    # try logging in with an invalid username and password
    def test_4_login_success(self):
        data = {
            'username': 'badusername',
            'password': 'badtestingpw1'
        }

        # make the post request
        response = self.client.post('/login', json=data, follow_redirects=True)

        # check that status code is 401 unauthorized
        self.assertEqual(response.status_code, 401)


# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
