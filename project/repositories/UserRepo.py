from models.User import User
import sqlite3
class UserRepo:

    def __init__(self):
        self.conn = sqlite3.connect("./project.db")
        c = self.conn.cursor()

        # check if the table exists
        # if yes, then skip
        for table in c.execute("SELECT name FROM sqlite_master").fetchall():
            if table[0] == "user":
                return

        # if table does NOT exist, create one
        # Author: Charlie 12-2-23
          # Changed password from BLOB type to VARCHAR to simplify login checking
        c.execute("CREATE TABLE user (userID INT PRIMARY KEY, username VARCHAR(40) unique, password VARCHAR(20));")
        self.conn.commit()

        # Author Charlie 12-8-23:
            # closing to handle concurrency issue on deployed instance
            # will now need to re-connect to database in each method
        self.conn.close()


    def findAll(self):
        self.conn = sqlite3.connect("./project.db")
        all = self.conn.cursor().execute("Select * from user").fetchall()
        self.conn.commit()
        self.conn.close()

        return all

    def findByID(self, id):
        self.conn = sqlite3.connect("./project.db")
        statement = "SELECT * FROM user WHERE userID ="+str(id)+";"
        result = self.conn.cursor().execute(statement).fetchone()
        self.conn.commit()
        self.conn.close()
        return result

    def findByName(self,name):
        self.conn = sqlite3.connect("./project.db")
        c = self.conn.cursor()
        statement = "SELECT * FROM user WHERE username ='"+str(name)+"';"
        result = c.execute(statement).fetchone()
        self.conn.commit()
        self.conn.close()
        return result

    def findAllUsernames(self):
        self.conn = sqlite3.connect("./project.db")
        statement = "SELECT username FROM user;"
        result = self.conn.cursor().execute(statement).fetchall()
        self.conn.commit()
        self.conn.close()

        return result


    def create(self,user):
        self.conn = sqlite3.connect("./project.db")

        # get the next available id
        rows = int(self.conn.cursor().execute("SELECT count(*) FROM user").fetchone()[0])
        try:
            self.conn.cursor().execute("INSERT INTO user (userID, username, password) values (?,?,?)",(rows+1,user.username,user.password))
            self.conn.commit()
            self.conn.close()
        except sqlite3.IntegrityError as e:
            print(e)
            # return -1 if username has been taken
            return -1

        return rows+1



if __name__ == '__main__':
    u = UserRepo()