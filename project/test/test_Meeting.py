import unittest
from app import app
import os
from services.AttendeeService import AttendeeService
from services.MeetingService import MeetingService
from services.StoryService import StoryService
from models.Story import Story
from models.Meeting import Meeting


# Purpose: This file tests the get method of meeting page
# Author: Ning Chih Chang
# Usage: run python3 ./test_Meeting.py

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

    # This method tests the GET method for meeting page
    def test_getMeeting(self):
        # create 1 userstory
        cookStory = Story("Super Hero","As a super hero","I want to fight bad guys","I can save Princess Peach")
        storyService = StoryService()
        storyService.createStory(cookStory)

        # create 1 meeting (meetingId should be 1)
        test_meeting = Meeting("Test Meeting 1")
        meetingService = MeetingService()
        meetingService.create(test_meeting)

        # create some attendees and assign their meetingIDs to 1
        attendeeService = AttendeeService()
        attendeeService.addAttendee(1,"testuser")
        attendeeService.addAttendee(1,"Mario")
        attendeeService.addAttendee(1,"Luigi")
        attendeeService.addAttendee(1,"Santa")

        # get response from GET method and convert into text
        response = self.client.get('meeting/1')
        renderData = response.get_data(True)

        # checks if status code is 200
        self.assertEqual(response.status_code,200)

        # checks if attendees are in the rendered html
        self.assertIn("testuser",renderData)
        self.assertIn("Mario",renderData)
        self.assertIn("Luigi",renderData)
        self.assertIn("Santa",renderData)

        # checks if story is in the rendered html
        self.assertIn("Super Hero",renderData)
        self.assertIn("As a super hero",renderData)
        self.assertIn("I want to fight bad guys",renderData)
        self.assertIn("I can save Princess Peach",renderData)


if __name__ == '__main__':
    unittest.main()