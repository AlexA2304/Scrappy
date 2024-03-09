import sqlite3
from models.Story import Story

class StoryRepo:

    def __init__(self):
        self.conn = sqlite3.connect("./project.db")
        c = self.conn.cursor()
        # check if the table exists
        # if yes, then skip
        for table in c.execute("SELECT name FROM sqlite_master").fetchall():
            if table[0] == "story":
                return

        # if table does NOT exist, create one
        c.execute("CREATE TABLE story (storyID INT PRIMARY KEY, meetingID INT, storyTitle VARCHAR(100) NOT NULL, asA VARCHAR(100) NOT NULL, iWant VARCHAR(100) NOT NULL, soThat VARCHAR(500) NOT NULL, effortLevel INT);")

        self.conn.commit()
        self.conn.close()


    def findAll(self):
        self.conn = sqlite3.connect("./project.db")
        all = self.conn.cursor().execute("Select * from story").fetchall()
        self.conn.commit()
        self.conn.close()
        return all

    def findByID(self, id):
        self.conn = sqlite3.connect("./project.db")
        statement = "SELECT * FROM story WHERE storyID ="+str(id)+";"
        result = self.conn.cursor().execute(statement).fetchall()
        self.conn.commit()
        self.conn.close()
        return result

    def findByName(self,name):
        self.conn = sqlite3.connect("./project.db")
        statement = "SELECT * FROM story WHERE storyTitle ='"+str(name)+"';"
        result = self.conn.cursor().execute(statement).fetchall()
        self.conn.commit()
        self.conn.close()
        return result

    # Alex: Was running into a syntax error when submitting and redirecting
    # back to /createMeeting so I restructured.
    def create(self, story: Story):
        self.conn = sqlite3.connect("./project.db")
        # get the next available id
        rows = int(self.conn.cursor().execute("SELECT count(*) FROM story").fetchone()[0])
        new_id = rows + 1
        statement = "INSERT INTO story (storyID, meetingID, storyTitle, asA, iWant, soThat, effortLevel) VALUES (?, ?, ?, ?, ?, ?, ?)"
        self.conn.cursor().execute(statement, (new_id, story.meetingID, story.storyTitle, story.asA, story.iWant, story.soThat, story.effortLevel))
        self.conn.commit()
        self.conn.close()
        return new_id

    def findByMeetingId(self,meetingId):
        self.conn = sqlite3.connect("./project.db")
        statement = "SELECT * FROM story WHERE meetingID ='"+str(meetingId)+"';"
        result = self.conn.cursor().execute(statement).fetchall()
        self.conn.commit()
        self.conn.close()
        return result


if __name__ == '__main__':
    s = StoryRepo()
