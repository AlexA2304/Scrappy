from repositories.MeetingRepo import MeetingRepo
from models.Meeting import Meeting

class MeetingService:
    meetingRepo = None


    def __init__(self):
        self.meetingRepo = MeetingRepo()


    # returns an array of meeting objects
    def findAll(self):
        result = []
        for i in self.meetingRepo.findAll():
            meeting = Meeting(i[1])
            meeting.setMeetingID(i[1])
            result.append(meeting)
        return result


    # takes a meeting object and store it in db. Returns the meetingID
    def create(self, meeting):
        return self.meetingRepo.create(meeting)


    def getNextId(self):
        return self.meetingRepo.getNextId()

    # Alex: Method to retrieve a meeting from the SQL statement in MeetingRepo.py
    def findMeetingByID(self, meetingID):
        return self.meetingRepo.findByID(meetingID)


if __name__ == '__main__':

    service = MeetingService()
