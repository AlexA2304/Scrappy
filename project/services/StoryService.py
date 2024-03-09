from repositories.StoryRepo import StoryRepo
from models.Story import Story

class StoryService:
    storyRepo = None

    def __init__(self):
        self.storyRepo = StoryRepo()

    # takes a Story object and save it in the db. Returns the storyID
    def createStory(self, story):
        return self.storyRepo.create(story)

    # returns an array of Story objects
    def findAll(self):
        result = []
        for i in self.storyRepo.findAll():
            story = Story(i[2],i[3],i[4],i[5])
            story.setStoryID(i[0])
            story.setMeetingID(i[1])
            story.setEffortLevel(i[6])
            result.append(story)
        return result

    def findById(self):
        return self.storyRepo.findByID()


    #returns all of the story names (for createMeeting page)
    def findAllNames(self):
        result = []

        for i in self.storyRepo.findAll():
            result.append(i[2])

        return result

    def findByMeetingId(self, meetingId):
        result = []
        for i in self.storyRepo.findByMeetingId(meetingId):
            story = Story(i[2],i[3],i[4],i[5])
            story.setStoryID(i[0])
            story.setMeetingID(i[1])
            story.setEffortLevel(i[6])
            result.append(story)
        return result



if __name__ == '__main__':

    service = StoryService()
