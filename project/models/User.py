# User data model for storing username and password

class User:

    username=""
    password=[]

    def __init__(self, username, password):
        self.username = username
        self.password = password

