import unittest
from app import app
import os
from services.StoryService import StoryService


# Purpose: This file tests the get and post methods of createStory page
# Author: Ning Chih Chang
# Usage: run python3 ./test_Story.py

class TestUserApi(unittest.TestCase):

    # This method sets the database file and session object during the start of this class
    @classmethod
    def setUpClass(self) -> None:
        # Set the test client for the entire test suite
        self.client = app.test_client()
        # set session object 'x'
        with self.client.session_transaction() as session:
            session['x']  = "testuser"
        if (os.getcwd().replace('\\','/').split('/')[-1] != 'test'):
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

    # This method deletes database file after running this class
    @classmethod
    def tearDownClass(self) -> None:
        try:
            os.remove(os.getcwd()+'/project.db')
        except OSError as error:
            print("There was an error attempting to delete project.db:", error)

    # This method tests the GET method for createStory page
    def test_getCreateStory(self):
        response = self.client.get('createStory')

        # check if status code is 200
        self.assertEqual(response.status_code,200)

    # This method tests the POST method for createStory page
    def test_postCreateStory(self):
        response = self.client.post('createStory',data={"storyTitle":"test1","asA":"as a 1","iWant":"i want 1","soThat":"so that 1"}
                                    ,follow_redirects = True)

        # check if status code is 200
        self.assertEqual(response.status_code,200)

        # check if it redirects to createMeeting page
        self.assertEqual(response.request.path,"/createMeeting")

        # check if the new story has been entered into database
        storyService = StoryService()
        db_data = storyService.findAll()[0]
        self.assertEqual(db_data.storyID, 1)
        self.assertEqual(db_data.meetingID, -1)
        self.assertEqual(db_data.storyTitle, "test1")
        self.assertEqual(db_data.asA, "as a 1")
        self.assertEqual(db_data.iWant, "i want 1")
        self.assertEqual(db_data.soThat, "so that 1")
        self.assertEqual(db_data.effortLevel, -1)


if __name__ == '__main__':
    unittest.main()