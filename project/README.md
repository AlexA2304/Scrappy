# Scrappy App

## Date: Nov-2-2023

This is the preliminary code for group project Scrappy App.

## app.py

the main controller that has all endpoints and logic for this app

## project.db

the database file

## prefix.py

a library from Professor Knox which helps our app to run in csel.io virtual machine

## models folder:

contains the data models

## repositories folder:

contains files that connect to database (sqlite3)

## services folder:

contains files that get data from the repositories and transfer into objects/data models which then can be used in app.py

## templates folder:

contains html files

## How to run:

export FLASK_APP=app.py

export FLASK_RUN_PORT=3308

export FLASK_DEBUG=true

export FLASK_ENV=development

run flask

Or, from the main directory, run `./start.cmds`

## Run sqlite3 locally

To run sqlite3 locally and verify tables, etc., run the following commands:

1. sqlite3 project.db
2. Query the schema using .schema
3. Query the tables using .tables
4. Run any other SQL commands as desired

## Landing page ("/"):

standard browser: http://127.0.0.1:3308

## Endpoints:

- http://127.0.0.1:3308/endpoints
- Shows existing vote endpoints, and how to use them

JupterLab: https://coding.csel.io/user/<your_username>/proxy/3308
