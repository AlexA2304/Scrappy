## Testing API endpoints for Scrappy App

This directory contains the unit tests for the Scrappy Appy endpoints. Each unique service is represented by a test\_{TheService} file. Whenever the test library is run, it will create a local project.db file inside the test directory. Each test should implement a setUp and tearDown class function that attempts to remove the local project.db file (not the overall project file!).

## To Run

1. cd to the /test directory. If tests are run from the top directory, you will overwrite the existing project.db database!
2. In the command line, you can run your specific test: python3 ./test_Voting.py

## Common errors

If you receive a "ModuleNotFound" error, you may not have PYTHONPATH set, which can screw up module imports. To fix:
1. echo $PYTHONPATH. If this command is blank, it would be good to set it.
2. export PYTHONPATH={the path to the project directory}

- An easy way to do this is navigate to the project directory and type pwd.
- Put the result from pwd into the PYTHONPATH export function
- Your imports should now work
- Remember, since we don't have flask installed on this project, you should be running in a python venv.