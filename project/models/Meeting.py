class Meeting:
    meetingID = -1
    meetingTitle = ""

# Alex: meetingID can now be set during initialization
    def __init__(self, meetingTitle, meetingID=None):
        self.meetingTitle = meetingTitle
        self.meetingID = meetingID

    def setMeetingID(self, meetingID):
        self.meetingID = meetingID
