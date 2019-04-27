# finalproj
Tufts CS Master's Independent Study project

See this application in production at *www.thoughtkeeper.me*

Features in Development:
* ~~Add delete and edit entry options to complete basic CRUD model for entries~~
* Add follow option
* File upload feature, text box for entry time (later dropdown)
* Style selector. Program applies separate CSS styling options for an entry
* LaTeX rendering option

TODOs:
* ~~add EDIT THIS ENTRY button to entries~~
* ~~restrict entry edits to only entry owner (redirect bad requests to /current\_user/<username>)~~
* ~~do not display EDIT THIS ENTRY button when current\_user != author~~
* add entry CSS so each entry is displayed in its own text box
* the EDIT THIS ENTRY link for an entry should be a button
* the Entry model "time" field should be renamed to "created"
* the Entry model should have a "last modified" field
* add DELETE button to entries
* add MAKE PUBLIC button to entries
* /user/<username> should display only entries marked as PUBLIC
* the Entry model has an entry field which should be a content field instead

