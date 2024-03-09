import sqlite3
from models.Meeting import Meeting

class MeetingRepo:

    def __init__(self):
        self.conn = sqlite3.connect("./project.db")
        c = self.conn.cursor()
        # check if the table exists
        # if yes, then skip
        for table in c.execute("SELECT name FROM sqlite_master").fetchall():
            if table[0] == "meeting":
                return

        # if table does NOT exist, create one
        c.execute("CREATE TABLE meeting (meetingID INT, meetingTitle VARCHAR (100));")
        self.conn.commit()
        self.conn.close()

    def findAll(self):
        self.conn = sqlite3.connect("./project.db")
        all = self.conn.cursor().execute("Select * from meeting").fetchall()
        self.conn.commit()
        self.conn.close()
        return all

    def getNextId(self):
        self.conn = sqlite3.connect("./project.db")
        nextId = int(self.conn.cursor().execute("SELECT count(*) FROM meeting").fetchone()[0])+1
        self.conn.commit()
        self.conn.close()
        return nextId

    def create(self, meeting):
        self.conn = sqlite3.connect("./project.db")
        # get the next available id
        rows = int(self.conn.cursor().execute("SELECT count(*) FROM meeting").fetchone()[0])
        statement = "INSERT INTO meeting VALUES ("+str(rows+1)+",'"+str(meeting.meetingTitle)+"');"
        self.conn.cursor().execute(statement)
        self.conn.commit()
        self.conn.close()
        return rows+1

    # Alex: Simple SQL statement that selects a meeting by its meetingID
    def findByID(self, meetingID):
        self.conn = sqlite3.connect("./project.db")
        statement = "SELECT * FROM meeting WHERE meetingID = ?"
        result = self.conn.cursor().execute(statement, (meetingID,)).fetchone()
        if result:
            return Meeting(result[1], meetingID=result[0])

        self.conn.commit()
        self.conn.close()
        return None



if __name__ == '__main__':
    m = MeetingRepo()
