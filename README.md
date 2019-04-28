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
* /index should display a short description of the site instead of being a simple redirect
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
* Style entries to display within a borderless page
* The Entry model has an entry field which should be a content field instead
* Create description at /index of site's purpose, with register and login buttons
* ~~Add DELETE button to entries~~
* The user should have the option to display entries in order of date created, last modified, or most frequently accessed
* Add confirmation pop-up when DELETE button is pressed
* Change DB model to add association table for user follower/followed relationship
* Create search option for finding users by username
* Create page to see followed users
* Add MAKE PUBLIC button to entries
* /user/<username> should display only entries marked as PUBLIC

Issues:
* Outline buttons (class="btn btn-outline-primary") are not loading properly even when using local bootstrap files
