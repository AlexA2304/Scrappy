# Vote is a table holding the meeting attendees
# along with their vote per story.

class Vote:
  storyID = ""
  username = ""
  vote = -1

  def __init__(self, storyID: int, username: str, vote: int):
    self.storyID = storyID
    self.username = username
    self.vote = vote

  def setVote(self, vote):
    self.vote = vote