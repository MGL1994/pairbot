# Pairbot

## Installation

* Clone or download the repo
* Run `pip install pipenv`
* Run `pipenv shell`
* Install packages
* Run `flask db init`
* Run `flask db migrate`
* Run `flask db upgrade`
* Run `flask run`
* Navigate to `http://localhost:5000/` in the browser

## Overview

Pairbot is a Flask app which allows you to enter a list of students into a database and then create randomised pairings.

The pairings should not repeat.

This is a prototype for a problem in my day to day work life.

### Technologies Used

* Python
* Flask
* Pipenv
* Flask SQLalchemy
* Flask wtf
* Unittest