from repositories.AttendeeRepo import AttendeeRepo


class AttendeeService:
    attendeeRepo = None

    def __init__(self):
        self.attendeeRepo = AttendeeRepo()


    # return usernames of all attendees in an array of a given meetingID
    def findAllAttendeeNamesByID(self,meetingID):
        result = []
        for i in self.attendeeRepo.findAllAttendeeNamesByID(meetingID):
            result.append(i[0])
        return result

    # Alex: Method to add a new attendee via AttendeeRepo.py
    def addAttendee(self, meetingID, username):
        self.attendeeRepo.addAttendee(meetingID, username)


if __name__ == '__main__':

    service = AttendeeService()