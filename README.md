# finalproj

Tufts CS Master's Independent Study project

See this application in production [here](www.thoughtkeeper.me)

## Installation

To run this application locally, first make sure you have the following packages installed:
* gcc
* python3
* pip3
* postgresql-devel (libpq-dev on Debian/Ubuntu)

Then, in your local clone run:

```
    pip3 install virtualenv
    source venv/bin/activate
    pip3 install -r requirements.txt
    flask run
```

Then visit http://127.0.0.1:5000 in your Web browser.

The first and second commands are necessary to create the virtual environment which contains the necessary python packages, which are listed in `requirements.txt`. 
*THIS STEP IS IMPORTANT* because it prevents conflicts with other versions of the same packages required by different applications system-wide, and maintains application stability when these packages are upgraded system-wide.
To exit the virtual environment, use `deactivate`.

To run the application in development mode, allowing stack trace output inside your Web browser, add `FLASK_ENV=development` to `.flaskenv`.

## Description

JournalPro is a journaling and publishing application for avid writers. On login, users are presented with an entry prompt that allows them to quickly and easily make entries separated by the click of a button. Entries are private by default. Project work focused entirely on front-end development, as ease of use is critical for eventual adoption of such a tool.

Future front-end work will enable easy sharing of content within the application by allowing followers like the traditional social media model, and outside the application by presenting a REST interface.

To support the goal of total privacy, future back-end work will support a distributed network model using a DHT. 

## Features and TODOs

### Features in Development:
* ~~Add delete and edit entry options to complete basic CRUD model for entries~~
* Text wrap
* Share entries by email
* Enable triple- or double-newline entry separation on /write/<username> 
* File upload feature, text box/dropdown for entry time
* Add follow option, feed to show new posts from followed users, make public option for entries

### TODOs:
* /index should display a description of the site's purpose, with register and login buttons
* ~~Base template needs a Write link at the top to go to /write/<username>~~
* ~~After submitting an entry, the form should be cleared on /write/<username>~~
* ~~Add EDIT THIS ENTRY button to entries~~
* ~~The EDIT THIS ENTRY link for an entry should be a button, not a link~~
* ~~The Entry model should have a "last edited" timestamp field~~
* ~~Editing an entry should change it's last edited timestamp in app/routes.py~~
* ~~Viewing an entry should show the time it was created and the time last edited~~
* ~~Restrict entry edits to only entry owner (redirect bad requests to /current\_user/<username>)~~
* ~~Do not display EDIT THIS ENTRY button when current\_user != author~~
* If a user has no posts, their user\_page should say so instead of listing 0 entries
* User.all\_entries() should order entries returned by time last modified
* The user should have the option to display entries in order of date created, last modified, or most frequently accessed
* Style entries to display within a borderless page
* ~~Add DELETE button to entries~~
* Add confirmation pop-up when DELETE button is pressed
* Change DB model to add association table for user follower/followed relationship
* Create search option for finding users by username
* Create page to see followed users
* Add MAKE PUBLIC button to entries
* /user/<username> should display only entries marked as PUBLIC
* Outline buttons (class="btn btn-outline-primary") are not loading properly even when using local bootstrap files


### Bugs
* Creating an entry longer than some number of characters and submitting, lost the end of the entry. Only the first 5439 characters were written.
* ~~App currently 404's on every GET request for /static/static/bootstrap.css~~
* ~~App styles elements strangely (shrunken dropdown button, sizing a little too large~~
* App does not give dropdown options when clicking the list icon button
