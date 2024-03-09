# The attendee table holds all the meeting table's attendees.
# It uses the meetingID foreign key to link to the meeting, and also
# contains each attendee's username.

class Attendee:
    userName=""
    meetingID=-1

    def __init__(self, userName, meetingID):
        self.userName = userName
        self.meetingID = meetingID
