import sqlite3

class AttendeeRepo:

    def __init__(self):
        self.conn = sqlite3.connect("./project.db")
        c = self.conn.cursor()
        # check if the table exists
        # if yes, then skip
        for table in c.execute("SELECT name FROM sqlite_master").fetchall():
            if table[0] == "attendee":
                return

        # if table does NOT exist, create one and fill in dummy values
        c.execute("CREATE TABLE attendee (userName VARCHAR(40), meetingID INT);")
        self.conn.commit()
        self.conn.close()


    def findAllAttendeeNamesByID(self,meetingID):
        self.conn = sqlite3.connect("./project.db")
        statement = "SELECT * FROM attendee WHERE meetingID ='"+str(meetingID)+"';"
        result = self.conn.cursor().execute(statement).fetchall()
        self.conn.commit()
        self.conn.close()
        return result

    def findAll(self):
        self.conn = sqlite3.connect("./project.db")
        all = self.conn.cursor().execute("Select * from attendee").fetchall()
        self.conn.commit()
        self.conn.close()
        return all

    # Alex: Created an addAttendee method which should allow for us to add
    # attendees via AttendeeService.py
    def addAttendee(self, meetingID, username):
        self.conn = sqlite3.connect("./project.db")
        statement = "INSERT INTO attendee (userName, meetingID) VALUES (?, ?)"
        self.conn.cursor().execute(statement, (username, meetingID))
        self.conn.commit()
        self.conn.close()



if __name__ == '__main__':
    a = AttendeeRepo()

