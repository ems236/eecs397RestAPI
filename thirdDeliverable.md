The third deliverable will be a write-up that explains how far you got in your project, whatdifficulties you faced, and what future improvements you could make. You should also includeinstructions on how to demo the code you developed (a Jupyter Notebook could come in handyfor this).

### Ellis Saupe ems236 second writeup / third deliverable

#### How far I got
I didn't want to get too crazy with this, so I got about as far as I expected to get.  
* I set up a sqllite3 database and made some tables using sqlAlchemy as an ORM.  Because this was the backend to a flask REST api, I used flask-sqlAlchemy, which seems to be about the same other than some small steps in declaring the engine and setting up the models.  I have some simple relationships covering one-many and many-many, through the tables: User, Topic, Post, and UserPostVote.
* I set up a pretty simple flask api using vanilla flask.  I chose not to use the flask-RESTful package because it didn't look that convenient and I figured I'd get a better understanding of what I was doing if I used basic flask.  The API has endpoints for all basic CRUD operations for all of these models.  There aren't any good tools in my API for filtering data beyond hierarchical relationships (getting posts within a topic) or sorting.  All requests are expected to be JSON.  I do not set the content-type headers on my responses, but they are also all JSON.
* I made a file that will test every endpoint of the API using the requests module.  These tests are by no means thorough, but they demonstrate the most basic functionality of my API.  

#### What was difficult
* *sqlAlchemy*: Setting up many to many relationships is not nearly as nice as I had expected it to be; either requiring an association table definition or making a weird not really an entity entity like I used.  This is usable, but isn't nearly as seamless as something like entity framework.  Being able to test queries in the python interpretter is a very nice feature.  It is also much simpler to generate tables based on your models than it is in EF; I'm sure that gets difficult if you do it a lot, so I just deleted my .db file before doing it.  I think it's ridiculous that you can't query with a native and operator; you either need to call an and method or make a subsequent filter call.
* *flask*: I've used flask a bit before and am still a big fan.  Their documentation isn't always very percise, but I was generally doing pretty basic stuff. I can't remember what I found telling me to do this, but my app creates weird importing by declaring db for sqlAlchemy in \_\_init\_\_.py. It took a decent amount of time to avoid recursive imports because of that.
* *requests*: This module is very simple and very effective at making http requests.  I'm a little peeved that http headers are just a dictionary.  It seems like the more common headers could be keyword arguments and have whatever python's closest equivalent to an enum for common values.  Reading json objects back creates a lot of dictionaries and all around too many square brackets in my client.  One trick I saw for this was to override an objects .\_\_dict\_\_ property which doesn't seem great.  Writing a custom deserialize method in a class also doesn't seem as convenient as it could be. 

#### What could be done to improve this
* The database could include things like comments.  I could add moderators or a user saved section.  Most forums don't have a ton of features, but a few things would flesh out my forum a lot.
* My flask api is pretty lacking in flexibility.  I should add filtering and sorting to all generic get requests using querystring parameters.  Using some form of user authentication (OAuth2 would be a good exercise) would be much better than passing user_ids around everywhere.
* I think the test client is pretty alright.  If I added any functionality to the server I would have to add more methods to the client, but it can do everything the server supports right now.
* Not so much a python task but moving it to an actual server with nginc / uWSGI would be good.

#### How to demo
1. initialize a virtual environment with the requirements.txt file
2. run create_tables.py
3. export FLASK_APP = main (The could maybe be improved by me making a .flaskenv file)
4. flask run
5. run apiTester.py

For more flexible testing, you can import apiTester.py and call any of its methods.  It has CRUD methods for all entities that will make the appropriate API calls.

The default flask server runs on 127.0.0.1:5000

API endpoints are:
* /topics
* /topics/{id}
* /topics/{id}/posts
* /topics/{id}/posts/{id}
* /topics/{id}/posts/{id}/votes
* /topics/{id}/posts/{id}/votes/{user_id}
* /users
* /users/{id}
