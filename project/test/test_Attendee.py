import unittest
from app import app
import os

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

    # Insert your test cases below