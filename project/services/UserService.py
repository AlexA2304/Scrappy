from repositories.UserRepo import UserRepo
from models.User import User


class UserService:
    userRepo = None

    def __init__(self):
        self.userRepo = UserRepo()


    # takes a User object and save it in the db. Returns the userID. Returns -1 if username has been taken
    # Author Charlie: updated service to accept username and password, then create User object and attempt account creation
    def createUser(self, username, password):
        user = User(username, password)
        return self.userRepo.create(user)


    def findAll(self):
        return self.userRepo.findAll()

    # Finds and returns User with the given matching id. Returns None if no user is found.
    def findById(self,id):
        uArray = self.userRepo.findByID(id)

        # if uArray is None, this means that we did not find any user matching id
        if uArray is None:
            return None

        user = User(uArray[1],uArray[2])
        return user


    # return all usernames in an array
    def findAllNames(self):
        result = []
        for i in self.userRepo.findAllUsernames():
            result.append(i[0])
        return result

    # find a single user
    def findByUsername(self, username):
        uArray= self.userRepo.findByName(username)

        if uArray is None:
            return False

        return True

    # verify username and password
    # returns true is valid and false otherwise
    def verifyCredentials(self, username, password):
        uArray = self.userRepo.findByName(username)

        if uArray is None:
            return False

        user = User(uArray[1],uArray[2])

        if (user.username == username) and (user.password == password):
            return True
        else:
            return False


if __name__ == '__main__':

    service = UserService()

