### Ellis Saupe ems236 first writeup

1. I don't really know how I expect to use python.  It's nice to know a convenient and cross platform scripting language; I may just use it to write small tools for myself.  I don't have a lot of interesting in data science or machine learning, so I hopefully can avoid most of the data analysis side of python.  I am interested in iot, so I expect to mostly work on scripts and networking in python.

2. 
+ Some nice web hosting modules that I've used are 
    * Flask
    * Django
    * I don't know if it really counts but uwsgi
+ I expect that I'd have to call some web services at some point. This should be pretty easy because python is dynamically typed and deserializing json should be trivial.  
    * requests
    * json
+ I'd expect to use some more permant storage, most likely sql
    * SQLAlchemy
    * flask_sqlalchemy
    * sqlite3
    * pickle / shelve for a nonsql solution
+ other networking
    * paho-mqtt is good for message passing
    * pyOpenSSL is good for security
+ config file parsing
    * json for json
    * ElementTree for xml
    * pyYaml for yaml
+ command line arguments
    * argparse

3. To work with some of these modules, I'll create a REST api for a small forum.  I will run the app locally with a flask debug server.  The site will use a sqlite backend and use sqlalchemy to interact with the database.  I will have the following entities:
* Post
* User
* Topic
* UserPostVotes

_Topics have many posts, users have many posts, UserPostVotes is a relation between users and posts that stores an int for the user vote_

This is more of a demo to meet the scope of this project, but adding authentication to votes would be the next logical step in this project.

I will create a simple client for this service that will execute all the CRUD methods on some demo data.