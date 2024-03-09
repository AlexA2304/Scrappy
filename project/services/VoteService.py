from repositories.VoteRepo import VoteRepo
from models.Vote import Vote
from const.dbNames import projectDB

class VoteService:
  voteRepo = None

  def __init__(self):
    self.voteRepo  = VoteRepo()

  # Formats list of votes into a JSON object
  def returnVoteJson(self, votes: list):
    result = []
    for i in votes:
      vote = Vote(*i)
      result.append({'storyID': vote.storyID, 'username': vote.username, 'vote': vote.vote})
    return result

  ############################################################
  # Queries
  ############################################################
  # returns an array of all story votes as a dictionary
  def findAll(self):
    return self.returnVoteJson(self.voteRepo.findAll())
  
  # Return a single storyID
  def findByID(self, id):
    return self.returnVoteJson(self.voteRepo.findByID(id))
  
  # Returns true if all vote values are equal
  def doVotesMatch(self, storyID, numberOfVoters):
    voteResults = self.voteRepo.getVotes(storyID)
    return {'match' : (len(set(voteResults)) == 1 and len(voteResults) == numberOfVoters)}
  
  # Get all votes for a specific username
  def findByUsername(self, username):
    return self.returnVoteJson(self.voteRepo.findByUsername(username))
  
  # Get all votes by vote value
  def findByVote(self, vote: int):
    return self.returnVoteJson(self.voteRepo.findByVote(vote))
  
  ############################################################
  # Mutations
  ############################################################
  # takes a StoryVote object and saves in the DB.
  def insert(self, vote: Vote):
    return self.voteRepo.insert(vote)
  
  # Update an existing vote
  def update(self, vote: Vote):
    return self.voteRepo.update(vote)
