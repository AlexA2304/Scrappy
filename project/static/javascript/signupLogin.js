/**
 * Author: Charlie Bailey
 * Date: 12/3/2023
 * Description: Javascript for running login and signup pages
 */

// URLs
const url = window.location.href;
const baseUrl = url.substring(0, url.lastIndexOf("/"));
const page = url.substring(url.lastIndexOf("/") + 1);
const loginUrl = baseUrl + "/login";
const signupUrl = baseUrl + "/signup";

// Headers
const headers = { "Content-Type": "application/json" };

// Validation checkers
const validateUsername = (username) => {
  if (username.length < 3 || username.length > 20) {
    return false;
  }
  return true;
}

const validatePassword = (password) => {
  if (password.length < 8 || password.length > 20) {
    return false;
  }
  return true;
}

///////////////////////////////////////////////////////////////////
// login page
///////////////////////////////////////////////////////////////////

const login = async (username, password) =>
  await fetch(`${loginUrl}`, {
    method: 'POST',
    body: JSON.stringify({ username, password }),
    headers: headers,
  })
    .then((response) => response);

if (page == 'login') {
  window.addEventListener("DOMContentLoaded", (event) => {
    const loginSubmit = document.getElementById("loginSubmit")
    loginSubmit.addEventListener("click", async (event) => {

      const usernameInput = document.getElementById("username");
      const passwordInput = document.getElementById("password");
      const loginContainer = document.getElementById("login-container");

      // clear previous error message
      loginContainer.removeChild(loginContainer.lastChild);

      let res;
      let result;
      let el = document.createElement("p");
      const username = usernameInput.value;
      const password = passwordInput.value;

      // validate username and password
      usernameValid = validateUsername(username);
      passwordValid = validatePassword(password);

      if (!usernameValid) {
        el.id = "invalid";
        result = document.createTextNode(
          "Invalid username. Must be between 5 and 20 character long."
        );
      }
      else if (!passwordValid) {
        el.id = "invalid";
        result = document.createTextNode(
          "Invalid password. Must be between 8 and 20 character long."
        );
      }
      else {
        // log the user in
        res = await login(usernameInput.value, passwordInput.value);

        if (!res.ok) {
          el.id = "invalid";
          result = document.createTextNode(
            "Invalid username/password. Please try again."
          )
        }
        else if (res.redirected) {
          el.id = "success";
          result = document.createTextNode(
            "Login Successful!"
          )
          window.location.href = res.url
        }
        else {
          // catch all
          el.id = "invalid";
          result = document.createTextNode(
            "Unknown error. Please try again."
          )
        }
      }

      // append error messages
      el.append(result);
      loginContainer.append(el);

      // clear username and password
      usernameInput.value = "";
      passwordInput.value = "";
    });
  });
}


///////////////////////////////////////////////////////////////////
// sign-up page
///////////////////////////////////////////////////////////////////

const signup = async (username, password) =>
  await fetch(`${signupUrl}`, {
    method: 'POST',
    body: JSON.stringify({ username, password }),
    headers: headers,
  })
    .then((response) => response);

if (page == 'signup') {
  window.addEventListener("DOMContentLoaded", (event) => {
    const signupSubmit = document.getElementById("signupSubmit")
    signupSubmit.addEventListener("click", async (event) => {
      const usernameInput = document.getElementById("username");
      const passwordInput = document.getElementById("password");
      const signupContainer = document.getElementById("signup-container");

      // clear previous error message
      signupContainer.removeChild(signupContainer.lastChild);

      let res;
      let result;
      el = document.createElement("p");
      const username = usernameInput.value;
      const password = passwordInput.value;

      // validate username and password
      usernameValid = validateUsername(username);
      passwordValid = validatePassword(password);

      if (!usernameValid) {
        el.id = "invalid";
        result = document.createTextNode(
          "Invalid username. Must be between 5 and 20 character long."
        );
      }
      else if (!passwordValid) {
        el.id = "invalid";
        result = document.createTextNode(
          "Invalid password. Must be between 8 and 20 character long."
        );
      }
      else {
        // create account
        res = await signup(username, password);
        console.log(res)
        if (!res.ok) {
          el.id = "invalid";
          result = document.createTextNode(
            "Username already exists. Please try again."
          )
        }
        else if (res.redirected) {
          el.id = "success";
          result = document.createTextNode(
            "Sign-up Successful!"
          )
          window.location.href = res.url
        }
        else {
          // catch all
          el.id = "invalid";
          result = document.createTextNode(
            "Unknown error. Please try again."
          )
        }
      }

      // append error messages
      el.append(result);
      signupContainer.append(el);

      // clear username and password
      usernameInput.value = "";
      passwordInput.value = "";
    });
  });
}