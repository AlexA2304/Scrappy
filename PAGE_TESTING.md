## Landing Page:
- Page title: Landing Page
- Page Description: When navigating to the application, this is the page that catches everyone, explains the app, and allows users to sign in or sign up.
- Parameters: None
- Data Needed: Login status (i.e. username not in localStorage)
- Link destination: /
- Tests:
  * User can see "Scrappy App" on the page
  * User can see "Login" button on the page
  * User can select the login button
  
  ![Scappy App Landing Page](https://github.com/jarrydallison/Colorfornia/assets/51180529/7a0f60d9-733d-439c-9094-63a03db2599a)

## Login Page:
- Page title: Login Page
- Page Description: When a user wants to sign into the system, they will use this page to enter their credentials, and login.
- Parameters: None
- Data Needed:
  * Login status
  * Username
  * Password
- Link destination: /login
- Tests:
  * User can see and type in the 'username' field on the page
  * User can see and type in the 'password' field on the page
  * User can see the 'Login' button on the page
  * The 'Login' button will be unclickable unless both the username and password fields are not empty
  * Pressing the 'Login' button passes the username and password to the database, and validates it
  * If the user credentials are valid, user is logged in and forwarded to the create meeting page
  * If the user credentials are invalid, an error message is shown

 ![Scappy App Login Page](https://github.com/jarrydallison/Colorfornia/assets/51180529/f9acfd53-2133-4b78-b9d5-d696fc32a974)

## Sign-up Page:
- Page title: Sign-up Page
- Page Description: When a user wants to sign up by creating credentials for the system, they will use this page to enter their desired username and password, and sign up.
- Parameters: None
- Data Needed:
  * Login status
  * Username
  * Password
- Link destination: /signup
- Tests:
  * User can see and type in the 'username' field on the page
  * User can see and type in the 'password' field on the page
  * User can see the 'Sign Up' button on the page
  * The 'Sign Up' button will be unclickable unless both the username and password fields are not empty
  * Pressing the 'Sign Up' first validates that the username and password meet the requirements
  * If the user credentials are invalid, an error message is shown.
  * If the user credentials are valid and meet the requirements, the username and passowrd are passed to the database and checks if the username and password already exist
  * If the username and password don't exist they are stored in the database and the user is logged in and is forwared to the create meeting page
  * If the username and password already exist, and error message is shown

![Scappy App Sign Up Page](https://github.com/jarrydallison/Colorfornia/assets/51180529/0d312171-40d1-4f1c-beb7-f25f84de8339)

## Create Meeting Page:
Page title: Create Meeting Page
- Page Description: This page gathers the essential information (i.e., meeting title, attendees, user stories) to create a meeting.
- Parameters: Username passed in URL
- Data Needed:
  * Login status
  * Current date and time 
  * All usernames from the database
  * Names of all user stories from the database
  * Next available meeting id from the database
- Link destination: /createmeeting/<username>
- Tests:
  * User can see and type in the ‘meeting title' field on the page
  * User can see, scroll and select any attendee on the attendees list
  * The database pulls out the names of all users correctly
  * The “Add Attendee” button will not be clickable unless two attendees are selected
  * Pressing the "Add Attendee" button will add the names of selected attendees to the new meeting object column
  * User can see the user story names on the user story list
  * The database pulls out names of all user stories correctly
  * User can see the meeting id on the page
  * The meeting id is valid (i.e., does not exist in database and is the next meeting id)
  * User can see the selected attendees, new meeting id and the current date and time in the new meeting object column 	
  * User can see and press the "Create Meeting" button
  * Pressing the "Creating Meeting" button creates a new Meeting object with accurate data (e.g., meeting title, attendees, and user stories) and stores it to the database 
  * User can see and press the “Sign out” button
  * Pressing the “Sign out” will sign out the user
 
 ![Scappy App Create Meeting Page](https://github.com/jarrydallison/Colorfornia/assets/51180529/b0e5ea49-f787-418d-a608-5583c741623c)

## Voting Page:
- Page title: Voting Page
- Page Description: After the meeting has been created, each meeting member will be taken to their own voting page where they will be shown: the current meeting attendees, a list of all user stories, the current user story on which they can vote, and the voting options for that user story. There will be an initial message showing that voting is in progress and a warning message when votes do not match. Once all of the votes match, a sucess message will be displayed. Once the meeting is conclude the user will be routed back to the meeting page—which will display the agreed upon consensus difficulty level for each of the stories voted on.
- Parameters: Meeting ID passed in URL
- Data Needed:
  * Username from localStorage
  * List of current meeting attendees from the database
  * List of User Stories from the database
  * Current User Story from the database
  * Voting options for current User Story
  * Each members vote updated in real-time
- Link destination: /meeting?ID=meeting_id
- Tests:
  * User can see Attendees list on the page
  * User can see list of User Stories on the page
  * User can see the current User Story on the page
  * User can see the voting options on the page
  * User can select and submit a voting option
  * User can see "Voting currently in progress" on the page initially
  * User can see "non-consensus" warning when votes do not match
  * User can see "voting sucess" message when all votes match
  * Meeting host can see the Start and End voting buttons
  * Clicking the Start Voting button enables the voting options buttons
  * Clicking the End Voting button disables the voting options buttons

![Scappy App Voting Page](https://github.com/jarrydallison/Colorfornia/assets/51180529/12c2de3e-65af-4c4e-8ee5-66bcf5b3dbe3)

## Add User Story Page:
- Page title: Add User Story Page
- Page Description: Before your meeting, from the 'Create Meeting' Page you can navigate to this page to upload a user story to the database, where it will be displayed once the meeting begins.
- Parameters: Username passed in URL
- Data Needed:
  * Login status (i.e. username not in localStorage)
  * Username from localStorage
- Link destination: /storyform/<username>
- Tests:
  * User can see and type in the 'Title' field on the page
  * User can see and type in the 'As' field on the page
  * User can see and type in the 'I want to' field on the page
  * User can see and type in the 'So that' field on the page
  * User can see and press the 'Submit...' button
  * User cannot click on the submit button unless all fields filled out
  * Pressing submit posts the user story to the database

![Scappy App Add Story Page](https://github.com/jarrydallison/Colorfornia/assets/51180529/dacdca21-6901-4f01-9d80-a5d1a40d4044)

## Whiteboard Design and Wire Frames:
Overall application:
![Scappy App Web Design](https://github.com/jarrydallison/Colorfornia/assets/51180529/4a8f8a09-340b-47fa-a5ba-9a2a2e7e6bd4)

View current design whiteboard:
https://link.excalidraw.com/l/6amen0SdcIX/49M5JNYMryz



