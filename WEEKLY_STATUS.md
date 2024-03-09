# Milestone 3
## Weekly Status for 10/9 to 10/13
### Current Project Board
<img width="1437" alt="Screenshot 2023-10-12 at 7 29 23 PM" src="https://github.com/jarrydallison/Colorfornia/assets/51180529/8674d294-3660-49ae-aefa-2f8912408d77">

### Backend Planning and Design:
#### Suggested E/R Diagram:
![Screenshot 2023-10-11 at 2 00 11 PM](https://github.com/jarrydallison/Colorfornia/assets/90670725/ef27fb57-9c38-489a-8986-83bb4dd668ec)
#### Backend Meeting Notes:
- User Login Table:
    - This is just the table of users so they can log into the system. To populate this table, we need a sign up page that pushes a username and password entry to the user login table.
    - FE requirements: login page, sign up page
- Meeting Table: 
    - This table is used to create meetings, which hold attendee lists and stories.
    - FE requirements: create a meeting page or modal
- Attendee Table:
    - Tracks attendees by username and meeting ID
    - FE must be able to add attendees to a meeting
- Story Table:
    - Tracks story requirements like title, etc.
    - Each story is linked to one meeting (many-to-one relationship)
    - FE requirements: page to create stories
- Votes Table:
    - Tracks votes by story ID
    - The logic here is that we know how many attendees in each meeting. We need to run a trigger after each vote that says:
        - If all attendees have voted AND 
        - If all vote values are equal
        - Then update the story with the agreed effort level
    - FE Requirements: Allow voting
#### SQL Commands (Working):
```
CREATE TABLE userlogin (
    userName VARCHAR(40) PRIMARY KEY,
    password CHAR(8) NOT NULL
);

CREATE TABLE meeting (
    meetingID INT PRIMARY KEY AUTO_INCREMENT,
    meetingTitle VARCHAR(100) NOT NULL
);

CREATE TABLE attendee (
    userName VARCHAR(40) PRIMARY KEY,
    meetingID INT NOT NULL,
    FOREIGN KEY (userName) REFERENCES userlogin(userName),
    FOREIGN KEY (meetingID) REFERENCES meeting(meetingID)
);

CREATE TABLE story (
    storyID INT PRIMARY KEY AUTO_INCREMENT,
    meetingID INT NOT NULL,
    storyTitle VARCHAR(100) NOT NULL,
    asA VARCHAR(100) NOT NULL,
    iWant VARCHAR(100) NOT NULL,
    soThat VARCHAR(500) NOT NULL,
    effortLevel INT,
    FOREIGN KEY (meetingID) REFERENCES meeting(meetingID)
);

CREATE TABLE votes (
    userName VARCHAR(40) PRIMARY KEY,
    storyID INT,
    voteValue INT NOT NULL,
    FOREIGN KEY (userName) REFERENCES userlogin(userName),
    FOREIGN KEY (storyID) REFERENCES story(storyID)  
);
```
### Frontend Planning and Design:
 - Completed initial pass at wire frame for frontend design
   - Attempted to incorporate as many of the backend requirements as possible

#### Link to Full Frontend Wireframe:
https://app.moqups.com/OKCyMUeSvjQAOIaiUew0CLmKtNd2jUqW/view/page/a8b49fd9f

#### App Landing Page:
<img width="1919" alt="Screenshot 2023-10-12 at 7 41 48 PM" src="https://github.com/jarrydallison/Colorfornia/assets/51180529/3134adea-ee96-4b39-8a7f-cad591c6b364">

### Frontend Architecture:
- Completed preliminary research on frontend frameworks and ultimately decided on either vanilla HTML/CSS or React.js
#### React.js:
- pros:
    - React is good for code reusability. The use of React Components allows you to call a large part of the website with a simple one-line tag that resembles self-closing HTML: `<component/>`.
    - React has built-in state management, meaning it will be easier to handle real-time data.
    - React has tons of libraries that can extend our app's functionality.
- cons:
    - The learning curve for React will be much steeper than vanilla HTML/CSS.
    - Given the scope of our project, React may be overkill given the learning curve (React really shines on very large projects).
    - May cause us to work with Node.js rather than Flask (which we all have a little experience with).
 
#### Vanilla HTML/CSS:
- pros:
    - It's simple! We won't have to worry about any frameworks, and we will most likely be going over the basics of both in class.
    - It's easy to get started with given we only need to create an HTML file to get started.
    - working with HTML/CSS will better solidify our foundations of web development.
- cons:
    - UI updates and state changes will have to be done manually, which for a web app can become complex.
    - Vanilla HTML/CSS doesn't prioritize code reusability like React does so we may end up writing more code overall.
    - less efficient at making dynamic page updates (such as voting) given we won't benefit from React's virtual DOM.

==============================================================
 ## Weekly Update for 10/16 to 10/20
 ### Current Project Board
<img width="1426" alt="Screenshot 2023-10-24 at 9 54 53 PM" src="https://github.com/jarrydallison/Colorfornia/assets/51180529/bf8ba6f3-ef3f-40b5-b361-cee132307a69">

#### Notes
- Due to overlapping class tests this week, interaction was relatively light.
- We discussed replicating the SQL framework from our lab this week into the final application design.
- On frontend, we discussed sticking with Vanilla html to simplify the dependencies.

==============================================================
## Weekly Update for 10/23 to 10/27
### Current Project Board
 <img width="1426" alt="Screenshot 2023-10-24 at 9 54 53 PM" src="https://github.com/jarrydallison/Colorfornia/assets/51180529/bf8ba6f3-ef3f-40b5-b361-cee132307a69">

 ### Web page design and dataflow
 ![Scappy App Web Design](https://github.com/jarrydallison/Colorfornia/assets/51180529/0bf9d238-ea58-4549-8267-86d876976169)

 Whiteboard link (view only): https://link.excalidraw.com/l/6amen0SdcIX/49M5JNYMryz

 #### Notes
 - We spent the majority of this week working collaboratively on the web page design for Milestone 4.
 - Using a collaborative whiteboard, we mocked out the user flow through our app including the params and data that would be needed for each page.
 - Considered each page in terms of the data we would need to GET/POST from the database and the general layout based on our previous wire frames.

==============================================================
## Weekly Update for 10/30 to 11/3
### Current Project Board
<img width="1778" alt="11-30 to 11-3 Trello Board" src="https://github.com/jarrydallison/Colorfornia/assets/51180529/1d9743a1-e00e-4963-91d2-8f7f36aa1af5">

### Role Assignment
![Scappy App Role Assignment](https://github.com/jarrydallison/Colorfornia/assets/51180529/259bedbd-b9cd-431a-b815-502917840ecb)

- Landing Page, Login Page, Sign-up Page: Charlie (Full Stack).
- Create Meeting Page: Ning (BE) and Alex (FE).
- Add User Story Page: Ning (BE) and Clayton (FE).
- Voting Page: Jarryd (BE) and Clayton (FE).

#### Notes
- Split up page work amongst the team.
- Set premissions on git main branch to require code review.
- Solidified git workflow and environment setup.

==============================================================
## Weekly Update for 11/6 to 11/10
### Current Project Board
<img width="1678" alt="Weekly Update 11-6 to 11-10 " src="https://github.com/jarrydallison/Colorfornia/assets/51180529/d56f6317-b0d9-43eb-a770-2d091015ca09">

#### Notes
- Began working on our assigned portions of the build.
- Famliarlized ourselves with the dev environment and fixed some inital setup bugs.
- Started working on a global CSS guide.
- Began building initial backend architecture skeleton.
- Continued working on SQL Design milestone.

==============================================================
## Weekly Update for 11-13 to 11-17
### Current Project Board
<img width="1678" alt="Weekly Update 11-13 to 11-17" src="https://github.com/jarrydallison/Colorfornia/assets/51180529/a15f2025-8801-42b2-a6ba-043078768d2d">

#### Notes
- Completed global CSS Style guide.
- Finialized SQL Design milestone.
- Finished initial backend skeleton.
- Completed API for voting.
- In progress on: add story page, voting page. create meeting page FE.

==============================================================
## Weekly Update for 11-20 to 11-24
### FALL BREAK
#### Notes
- Everyone continued to work independently; no team meeting.

==============================================================
## Weekly Update for 11-27 to 12-1
### Current Project Board
<img width="1418" alt="Weekly Update 11-27 to 12-1" src="https://github.com/jarrydallison/Colorfornia/assets/51180529/af526a44-d632-460b-bad2-b359391e81f2">

#### Notes
- Deep into build mode; everyone continuing to work on their respective portions of the application.
- Set feature freeze for Friday of next week.

==============================================================
## Weekly Update for 12-4 to 12-8
### Current Project Board
<img width="1420" alt="Weekly Status 12-4 to 12-8" src="https://github.com/jarrydallison/Colorfornia/assets/51180529/8cfcab5f-9a10-4fd3-96ad-d200b632d554">

### Notes
- Completed majority of the build; feature freeze in place.
- Working to integrate all changes and fix data handoff issues between FE and BE.
- Initial testing framework complete.
- Starting deployment process to render.

==============================================================
## Weekly Update for 12-11 to 12-15
### Current Project Board
<img width="1417" alt="Weekly Status 12-11 to 12-15" src="https://github.com/jarrydallison/Colorfornia/assets/51180529/c59ab94b-f95f-487e-97e7-f585154f8dc1">


#### Notes
- Fixed most integration issues and created demoable product.
- Work on presentation slides and flow.
- Fixed concurrency issue on deployed instance
- Began working on remaining unit tests.
- Gave presentation and crushed it!

==============================================================
## Weekly Update for 12-18
### Current Project Board
<img width="1420" alt="Weekly Status 12-18" src="https://github.com/jarrydallison/Colorfornia/assets/51180529/e707dc99-4f33-4f6e-8a7d-19da9c99058a">

#### Notes
- Final cleanup and documentaiton of repo.
- Finished all unit tests.
- Wrote final report.
- Submitted final project.
