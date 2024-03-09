from flask import Flask, render_template, request, session, url_for, redirect, jsonify, send_from_directory
import os
from models.Story import Story
from models.Meeting import Meeting
from services.MeetingService import MeetingService
from services.StoryService import StoryService
from services.UserService import UserService
from services.AttendeeService import AttendeeService

# import prefix from Professor Knox lab so that this app can run on csel.io virtual machine
import prefix


app = Flask(__name__)
# Import subroutes
import endpoints.voteEndpoints

# for session object
app.secret_key = "abc"

prefix.use_PrefixMiddleware(app)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')

@app.route("/")
def index():
    return redirect('/login')

@app.route("/endpoints")
def endpoints():
    return render_template("endpoints.html")


@app.route("/createStory", methods=['GET','POST'])
def createStory():
    if request.method == 'POST':
        s = Story(request.form.get("storyTitle"),request.form.get("asA"),request.form.get("iWant"),request.form.get("soThat"))
        storyService = StoryService()
        newId = storyService.createStory(s)
        # Alex: The successful creation of a story now redirects back to the /createMeeting route
        return redirect('/createMeeting')

    else:
        return render_template("createStory.html")



@app.route("/createMeeting", methods=['GET','POST'])
def createMeeting():

    meetingService = MeetingService()
    # Alex: initializing the attendeeService for the creation of a new meeting
    attendeeService = AttendeeService()

    if request.method == 'POST':
        # create Meeting and save it to db
        # Alex: Creates new meeting with the title "new meeting"
        newMeeting = Meeting("new meeting")
        newMeetingID = meetingService.create(newMeeting)

        current_user = session.get('x', None)
        if current_user:
            attendeeService.addAttendee(newMeetingID, current_user)

        # create Attendees and save them to db
        # Alex: Retrieves the selected list of attendees from the Javascript array
        # in getCreateMeeting.html separated by commas. (the .strip method removes white space)
        # each attendee is then added to the list of attendees using the new .addAttendee method
        # of AttendeeService
        attendees = request.form.get('selectedUsernames').split(',')
        for attendee in attendees:
            attendee = attendee.strip()
            # Check if attendee is not an empty string
            if attendee and attendee != current_user:
                attendeeService.addAttendee(newMeetingID, attendee)

        # redirects to the meeting page
        return redirect(url_for('meeting', meetingID=newMeetingID))


    else:
        # get host's username from session
        username = session['x']

        # get next available meetingId
        meetingId = meetingService.getNextId()

        # get all usernames in db (usernameArray)
        userService = UserService()
        usernameArray = userService.findAllNames()

        # get all the userstory names (storynameArray)
        storyService = StoryService()

        storyArray = storyService.findAll()
        storyNameArray = []
        storyEffortArray = []

        for story in storyArray:
            storyNameArray.append(story.storyTitle)
            storyEffortArray.append(story.effortLevel)
        # Alex: Generates an array of tuples each with the story name and it's effort
        stories_with_effort = zip(storyNameArray, storyEffortArray)

        # create the url for meeting page
        url = request.host_url + url_for('meeting',meetingID = meetingId)

        # render html page and send all necessary variables to the front end
        # Alex: Pass in all needed variables one by one due to having issues with **locals()
        return render_template("getCreateMeeting.html", usernames=usernameArray, stories=stories_with_effort, username=username, meetingID=meetingId, url=url)

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.json.get("username")
        password = request.json.get("password")

        user = UserService()
        isValid = user.verifyCredentials(username, password)
        # error first handling
        if not isValid:
            # username and password not valid
            response = jsonify()
            response.status = 401 # Unauthorized
            return response
        else:
            # saving username as a session object x
            session['x'] = username
            return redirect('/createMeeting')

    return render_template("login.html")


@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.json.get("username")
        password = request.json.get("password")

        user = UserService()

        # check if username exists
        usernameExists = user.findByUsername(username)

        # if username exists return conflict error
        if usernameExists:
            response = jsonify()
            response.status_code = 409 # Conflict
            return response
        else:
            # create user account
            user.createUser(username, password)

            # saving username as a session object x
            session['x'] = username
            return redirect('/createMeeting')

    return render_template("signup.html")


@app.route("/meeting/<meetingID>", methods=['GET','POST'])
def meeting(meetingID):

    attendeeService = AttendeeService()
    attendeesNames = attendeeService.findAllAttendeeNamesByID(meetingID)

    for i in attendeesNames:
        if (session['x']) == i:
            currentUser = i

            # display user story
            storyService = StoryService()

            storyArray = storyService.findAll()
            storyNameArray = []
            storyAsA = []
            storyIWant = []
            storySoThat = []
            storyEffortArray = []

            for story in storyArray:
                storyNameArray.append(story.storyTitle)
                storyAsA.append(story.asA)
                storyIWant.append(story.iWant)
                storySoThat.append(story.soThat)
                storyEffortArray.append(story.effortLevel)
                # display the first story
                currentStory = storyArray[0]

            # show all selected users and their vote
            votes = [None]*len(attendeesNames)

            return render_template("meeting.html",**locals())


    return "you are not invited to the meeting"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3308)