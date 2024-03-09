/**
 * Author: Jarryd Allison
 * Date: 11/15/2023
 * Description: Javascript running for endpoints page
 */

// URLs
const url = window.location.href;
const baseUrl = url.substring(0, url.lastIndexOf("/"));
const votesUrl = baseUrl + "/vote";

// Headers
const headers = { "Content-Type": "application/json" };

// Voting
///////////////////////////////////////////////////////////////////
// findAll
///////////////////////////////////////////////////////////////////
const getAllVotes = async () =>
  await fetch(`${votesUrl}/findAll`)
    .then((response) => response.json())
    .then((votes) => votes);
window.addEventListener("DOMContentLoaded", (event) => {
  const voteFindAll = document.getElementById("voteFindAll");
  voteFindAll.addEventListener("click", async () => {
    // Get the results container
    const container = document.getElementById("voteFindAllResult");
    // Clear out the old info
    container.textContent = "";
    // Get the votes
    const votes = await getAllVotes();
    // Append the element with the JSON stringified response
    const el = document.createElement("p");
    const results = document.createTextNode(JSON.stringify(votes));
    container.appendChild(el.appendChild(results));
  });
});

///////////////////////////////////////////////////////////////////
// findByID
///////////////////////////////////////////////////////////////////
const findVotesByID = async (storyID) =>
  await fetch(`${votesUrl}/findByID/${storyID}`, {
    method: "GET",
  })
    .then((response) => response.json())
    .then((votesByID) => votesByID);
window.addEventListener("DOMContentLoaded", (event) => {
  const voteFindByID = document.getElementById("voteFindByID");
  voteFindByID.addEventListener("click", async () => {
    // Get the storyID to query
    const storyID = document.getElementById("storyID").value;
    // Get the results container
    const container = document.getElementById("voteFindByIDResult");
    // Clear out the old info
    container.textContent = "";
    let votes;
    let results;
    el = document.createElement("p");
    if (storyID) {
      votes = await findVotesByID(storyID);
      results = document.createTextNode(JSON.stringify(votes));
    } else {
      el.id = "error";
      results = document.createTextNode("You must specify a story ID");
    }
    el.appendChild(results);
    container.appendChild(el);
  });
});

///////////////////////////////////////////////////////////////////
// getVotes
///////////////////////////////////////////////////////////////////
const getVotesByID = async (storyID, numberOfVoters) =>
  await fetch(`${votesUrl}/doVotesMatch/${storyID}/${numberOfVoters}`, {
    method: "GET",
  })
    .then((response) => response.json())
    .then((votesByID) => votesByID);
window.addEventListener("DOMContentLoaded", (event) => {
  const voteGetVotesByID = document.getElementById("voteGetVotes");
  voteGetVotesByID.addEventListener("click", async () => {
    // Get the storyID to query
    const storyID = document.getElementById("getVotesStoryID").value;
    // Get the expected number of voters
    const numberOfVoters = document.getElementById(
      "getVotesNumberOfVoters"
    ).value;
    // Get the results container
    const container = document.getElementById("voteGetVotesResult");
    // Clear out the old info
    container.textContent = "";
    let votes;
    let results;
    el = document.createElement("p");
    if (storyID) {
      votes = await getVotesByID(storyID, numberOfVoters);
      results = document.createTextNode(JSON.stringify(votes));
    } else {
      el.id = "error";
      results = document.createTextNode("You must specify a story ID");
    }
    el.appendChild(results);
    container.appendChild(el);
  });
});

///////////////////////////////////////////////////////////////////
// Find by username
///////////////////////////////////////////////////////////////////
const findVotesByUsername = async (username) =>
  await fetch(`${votesUrl}/findByUsername/${username}`, {
    method: "GET",
  })
    .then((response) => response.json())
    .then((votesByUsername) => votesByUsername);
window.addEventListener("DOMContentLoaded", (event) => {
  const voteFindByUsername = document.getElementById("voteFindByUsername");
  voteFindByUsername.addEventListener("click", async () => {
    // Get the Username to query
    const username = document.getElementById("findByUsernameUsername").value;
    // Get the results container
    const container = document.getElementById("voteFindByUsernameResult");
    // Clear out the old info
    container.textContent = "";
    let votes;
    let results;
    el = document.createElement("p");
    if (storyID) {
      votes = await findVotesByUsername(username);
      results = document.createTextNode(JSON.stringify(votes));
    } else {
      el.id = "error";
      results = document.createTextNode("You must specify a username");
    }
    el.appendChild(results);
    container.appendChild(el);
  });
});

///////////////////////////////////////////////////////////////////
// Find by vote
///////////////////////////////////////////////////////////////////
const findVotesByVote = async (id) =>
  await fetch(`${votesUrl}/findByVote/${id}`, {
    method: "GET",
  })
    .then((response) => response.json())
    .then((votesByID) => votesByID);
window.addEventListener("DOMContentLoaded", (event) => {
  const voteFindByVote = document.getElementById("voteFindByVote");
  voteFindByVote.addEventListener("click", async () => {
    // Get the vote value to query
    const voteValue = document.getElementById("findByVoteVote").value;
    // Get the results container
    const container = document.getElementById("voteFindByVoteResult");
    // Clear out the old info
    container.textContent = "";
    let votes;
    let results;
    el = document.createElement("p");
    if (storyID) {
      votes = await findVotesByVote(voteValue);
      results = document.createTextNode(JSON.stringify(votes));
    } else {
      el.id = "error";
      results = document.createTextNode("You must specify a vote value");
    }
    el.appendChild(results);
    container.appendChild(el);
  });
});

///////////////////////////////////////////////////////////////////
// insert
///////////////////////////////////////////////////////////////////
const insertVote = async (storyID, username, vote) =>
  await fetch(`${votesUrl}/insert`, {
    method: "POST",
    body: JSON.stringify({ storyID, username, vote }),
    headers,
  }).then((response) => response.json().then((res) => res));

window.addEventListener("DOMContentLoaded", (event) => {
  const insert = document.getElementById("insertVoteButton");
  insert.addEventListener("click", async () => {
    // Get the fields
    const storyID = document.getElementById("insertStoryID").value;
    const username = document.getElementById("insertUsername").value;
    const vote = document.getElementById("insertVote").value;
    // Get the results container
    const container = document.getElementById("insertVoteResult");
    // Clear out the old info
    container.textContent = "";
    let res;
    let results;
    el = document.createElement("p");
    if (storyID && username && vote) {
      el.id = "success";
      res = await insertVote(storyID, username, vote);
      if (res.error) {
        el.id = "error";
      }
      results = document.createTextNode(JSON.stringify(res));
    } else {
      el.id = "error";
      results = document.createTextNode(
        "You must provide a storyID, username, and vote."
      );
    }
    el.appendChild(results);
    container.appendChild(el);
  });
});

///////////////////////////////////////////////////////////////////
// update
///////////////////////////////////////////////////////////////////
const updateVote = async (storyID, username, vote) =>
  await fetch(`${votesUrl}/update`, {
    method: "POST",
    body: JSON.stringify({ storyID, username, vote }),
    headers,
  }).then((response) => response.json().then((res) => res));

window.addEventListener("DOMContentLoaded", (event) => {
  const update = document.getElementById("updateVoteButton");
  update.addEventListener("click", async () => {
    // Get the fields
    const storyID = document.getElementById("updateStoryID").value;
    const username = document.getElementById("updateUsername").value;
    const vote = document.getElementById("updateVote").value;
    // Get the results container
    const container = document.getElementById("updateVoteResult");
    // Clear out the old info
    container.textContent = "";
    let res;
    let results;
    el = document.createElement("p");
    if (storyID && username && vote) {
      el.id = "success";
      res = await updateVote(storyID, username, vote);
      if (res.error) {
        el.id = "error";
      }
      results = document.createTextNode(JSON.stringify(res));
    } else {
      el.id = "error";
      results = document.createTextNode(
        "You must provide a storyID, username, and vote."
      );
    }
    el.appendChild(results);
    container.appendChild(el);
  });
});
