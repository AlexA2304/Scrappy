# The Story table contains each story's information, including meetingID (foreign key),
# storyID (primary key), the story title, "as a" statement, "i want" statement,
# "so that" statement, and effort Level.

class Story:
    meetingID = -1
    storyID = -1
    storyTitle = ""
    asA = ""
    iWant = ""
    soThat = ""
    effortLevel = -1

    def __init__(self,storyTitle, asA, iWant, soThat):
        self.storyTitle = storyTitle
        self.asA = asA
        self.iWant = iWant
        self.soThat = soThat

    def setStoryID(self, storyID):
        self.storyID = storyID

    def setMeetingID(self, meetingID):
        self.meetingID = meetingID

    def setEffortLevel(self,effortLevel):
        self.effortLevel = effortLevel