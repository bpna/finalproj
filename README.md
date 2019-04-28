# finalproj
Tufts CS Master's Independent Study project

See this application in production at *www.thoughtkeeper.me*

Features in Development:
* ~~Add delete and edit entry options to complete basic CRUD model for entries~~
* Share entries by email
* Enable triple- or double-newline entry creation on /write/<username> 
* Add follow option, feed to show new posts from followed users, make public option for entries
* File upload feature, text box/dropdown for entry time

TODOs:
* ~~after submitting an entry, the form should be cleared on /write/<username>~~
* ~~add EDIT THIS ENTRY button to entries~~
* ~~the EDIT THIS ENTRY link for an entry should be a button, not a link~~
* ~~the Entry model should have a "last edited" timestamp field~~
* ~~editing an entry should change it's last edited timestamp in app/routes.py~~
* ~~viewing an entry should show the time it was created and the time last edited~~
* ~~restrict entry edits to only entry owner (redirect bad requests to /current\_user/<username>)~~
* ~~do not display EDIT THIS ENTRY button when current\_user != author~~
* style entries to display within a borderless page
* the Entry model has an entry field which should be a content field instead
* create description at /index of site's purpose, with register and login buttons
* ~~add DELETE button to entries~~
* add confirmation pop-up when DELETE button is pressed
* change DB model to add association table for user follower/followed relationship
* create search option for finding users by username
* create page to see followed users
* add MAKE PUBLIC button to entries
* /user/<username> should display only entries marked as PUBLIC

Issues:
* outline buttons (class="btn btn-outline-primary") are not loading properly even when using local bootstrap files
