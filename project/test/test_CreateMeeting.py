import unittest
from app import app
import os
from services.UserService import UserService
from services.StoryService import StoryService
from services.MeetingService import MeetingService
from services.AttendeeService import AttendeeService
from models.Story import Story
from models.Meeting import Meeting


# Purpose: This file tests the get and post methods of createMeeting page
# Author: Ning Chih Chang
# Usage: run python3 ./test_CreateMeeting.py

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

    # This method tests the GET method for createMeeting page
    def test_getCreateMeeting(self):
        # create some users (the database should have test1 and test2)
        userService = UserService()
        # Author Charlie: re-adding test1 and test2 users here since dummy data removed from UserRepo
        userService.createUser("test1", "testingpw1")
        userService.createUser("test2", "testingpw2")
        userService.createUser("Jane Doe","123456")
        userService.createUser("John Smith","987654")

        # create 1 userstory
        cookStory = Story("Great Cook","As a cook","I want to cook yummy food","My customer will be happy")
        storyService = StoryService()
        storyService.createStory(cookStory)

        # create 2 meetings (thus the next meeting id should be 3)
        meeting1 = Meeting("testM1")
        meeting2 = Meeting("testM2")
        meetingService = MeetingService()
        meetingService.create(meeting1)
        meetingService.create(meeting2)

        # get response from GET method and convert into text
        response = self.client.get('createMeeting')
        renderData = response.get_data(True)

        # check if status code is 200
        self.assertEqual(response.status_code,200)

        # check if usernames are in the rendered html
        self.assertIn("test1",renderData)
        self.assertIn("test2",renderData)
        self.assertIn("Jane Doe",renderData)
        self.assertIn("John Smith",renderData)

        # check if story name and effort are in rendered html
        self.assertIn("Great Cook",renderData)
        self.assertIn("Effort: N/A",renderData)

        # check if username is in rendered html
        self.assertIn("Host: <span>testuser</span>",renderData)

        # check if meeting id = 3 is in rendered html
        self.assertIn("Meeting id: <span>3</span>",renderData)

        # check if url is in rendered html
        self.assertIn("/meeting/3",renderData)

    # This method tests the POST method of createMeeting page
    def test_postCreateMeeting(self):
        response = self.client.post('createMeeting', data={'selectedUsernames':'test1,Jane Doe'}
                                    ,follow_redirects = True)

        # check if status is 200
        self.assertEqual(response.status_code,200)

        # check if it redirects to meeting page
        self.assertEqual(response.request.path,"/meeting/3")

        # check if it creates a new meeting
        meetingService = MeetingService()
        db_meeting = meetingService.findMeetingByID(3)
        self.assertEqual(db_meeting.meetingTitle,"new meeting")
        self.assertEqual(db_meeting.meetingID,3)

        # check if attendees have been entered into database
        attendeeService = AttendeeService()
        db_attendees = attendeeService.findAllAttendeeNamesByID(3)
        self.assertEqual(db_attendees,['testuser','test1','Jane Doe'])


if __name__ == '__main__':
    unittest.main()