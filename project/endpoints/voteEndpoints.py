from app import app
import json
from flask import request, jsonify
from models.Vote import Vote
from services.VoteService import VoteService
from const.dbNames import voteOptions, projectDB

# Error response for not supported endpoints
def notSupported(type):
  return {'error': type+" not supported"}

# Error handling for POST endpoints
def postErrors(storyID: str, username: str, vote: str):
  if storyID == "" or not storyID:
    return "Story ID must be specified"
  elif username == "" or not username:
    return "Username must be specified"
  elif vote == "" or not vote:
    return "Vote must be specified"
  elif vote not in voteOptions:
    return "Vote must be in options "+str(voteOptions)
  else:
    return ""
  
# Returns the entire vote table
@app.route("/vote/findAll", methods=['GET'])
def findAll():
  if request.method == 'GET':
    votes = VoteService()
    return votes.findAll()
  return notSupported(request.method)
  
# Returns all votes for a given storyID
@app.route("/vote/findByID/<int:storyID>", methods=['GET'])
def findByID(storyID):
  if request.method == 'GET':
    votes = VoteService()
    return votes.findByID(storyID)
  return notSupported(request.method)
  
# Returns only an array of vote values for a given storyID
@app.route("/vote/doVotesMatch/<int:storyID>/<int:numberOfVoters>", methods=['GET'])
def doVotesMatch(storyID, numberOfVoters):
  if request.method == 'GET':
    votes = VoteService()
    return votes.doVotesMatch(storyID, numberOfVoters)
  return notSupported(request.method)
  
# Returns all votes from a specific username
@app.route("/vote/findByUsername/<username>", methods=['GET'])
def findByUsername(username):
  if request.method == 'GET':
    votes = VoteService()
    return votes.findByUsername(username)
  return notSupported(request.method)
  
# Returns all votes whose weight is provided
@app.route("/vote/findByVote/<int:voteVal>", methods=['GET'])
def findByVote(voteVal):
  if request.method == 'GET':
    votes = VoteService()
    return votes.findByVote(voteVal)
  return notSupported(request.method)

# Insert a story vote. Will return "success" on success
@app.route("/vote/insert", methods=['POST'])
def insertVote():
  if request.method == 'POST':
    storyID = request.json.get("storyID")
    username = request.json.get("username")
    vote = int(request.json.get("vote"))
    # Handle errors
    errors = postErrors(storyID, username, vote)
    if errors != "":
      return jsonify({'error': errors})
    v = Vote(storyID, username, vote)
    return VoteService().insert(v)
  return notSupported(request.method)
  
# Update an existing vote
@app.route("/vote/update", methods=['POST'])
def updateVote():
  if request.method == 'POST':
    storyID = request.json.get("storyID")
    username = request.json.get("username")
    vote = int(request.json.get("vote"))
    # Handle errors
    errors = postErrors(storyID, username, vote)
    if errors != "":
      return jsonify({'error': errors})
    v = Vote(storyID, username, vote)
    return VoteService().update(v)
  return notSupported(request.method)
