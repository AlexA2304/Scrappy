import json
from sqlite3 import connect, Error
from models.Vote import Vote
from const.dbNames import vote, projectDB

class VoteRepo:

  # StoryID, username, vote

  def __init__(self):
    self.conn = connect(projectDB)
    c = self.conn.cursor()
    # Create the table with storyID and username comprising the primary keys
    c.execute("CREATE TABLE IF NOT EXISTS "+vote+'''(
        storyID INT,
        username VARCHAR(40),
        vote INT,
        PRIMARY KEY (storyID, username)
    );''')
    self.conn.commit()
    self.conn.close()

  # Query the vote table
  def query(self, query: str):
    self.conn = connect(projectDB)
    c = self.conn.cursor()
    result = c.execute(query).fetchall()
    self.conn.commit()
    self.conn.close()
    return result
  
  # Change the vote table
  def mutate(self, mutation: str, type: str):
    response = {'success': type + " success"}
    self.conn = connect(projectDB)
    c = self.conn.cursor()
    try:
      c.execute(mutation)
    except Error as er:
      response = {'error': str(er)}
    self.conn.commit()
    self.conn.close()
    return response
  
  # Query the entire table
  def findAll(self):
    return self.query("SELECT * from "+vote)
  
  # Query by storyID
  def findByID(self, storyID: int or str):
    query = "SELECT * FROM "+vote+" WHERE storyID = '"+str(storyID)+"';"
    return self.query(query)
  
  # Query to return only votes for a specific storyID
  def getVotes(self, storyID: int or str):
    query = "SELECT vote FROM "+vote+" WHERE storyID = "+str(storyID)+";"
    return self.query(query)
  
  # Query by username
  def findByUsername(self, username: str):
    query = "SELECT * FROM "+vote+" WHERE username = '"+str(username)+"';"
    return self.query(query)
  
  # Query by vote amount
  def findByVote(self, voteValue: int):
    query = "SELECT * FROM "+vote+" WHERE vote = "+str(voteValue)+";"
    return self.query(query)
  
  # Insert a new vote into the table
  def insert(self, insertVote: Vote):
    mutation = "INSERT INTO "+vote+" VALUES ("\
               +str(insertVote.storyID)+",'"\
               +str(insertVote.username)+"',"\
               +str(insertVote.vote)+");"
    return self.mutate(mutation, 'vote insert')
  
  # Update an existing vote
  def update(self, voteUpdate: Vote):
    # Check that the vote exists
    query = "SELECT * FROM "+vote+" WHERE storyID = "+str(voteUpdate.storyID)+" AND username = '"+str(voteUpdate.username)+"';"
    voteExists = self.query(query)
    if (len(voteExists) > 0):
      mutation = "UPDATE "+vote+" SET vote = "+str(voteUpdate.vote)+" WHERE storyID = "+str(voteUpdate.storyID)+" AND username = '"+str(voteUpdate.username)+"';"
      return self.mutate(mutation, 'vote update')
    # If the vote doesn't exist, return the error
    return {'error': 'The vote does not exist'}