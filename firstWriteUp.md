The first deliverable is a short write-up where:
1. You will share some of the ways you hope to use Python going forward. Are you hoping
to use it for AI, data analysis, game development, etc.?
2. You will identify Python modules that can help you with what you describe in point 1.
3. Pick a module and describe a short project/prototype you can start to develop. Aim for
something that is beyond the level of a tutorial, but slightly less than a hack-a-thon
project (usually something developed by a small group over a weekend). Aim for
something that can be demonstrated either through running the Python code on its own,
or can be visualized and demonstrated using a Jupyter Notebook.

#Ellis Saupe ems236 first writeup

1. 
I don't really know how I expect to use python.  It's nice to know a convenient and cross platform scripting language; I may just use it to write small tools for myself.  I don't have a lot of interesting in data science or machine learning, so I hopefully can avoid most of the data analysis side of python.  I am interested in iot, so I expect to mostly work on scripts and networking in python.
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

3. 
To work with some of these modules, I'll create a REST api for a small forum.  I will run the app locally with a flask debug server.  The site will use a sqlite backend and use sqlalchemy to interact with the database.  I will have the following entities:
* Post
* Comment
* User
* Topic
__ Topics have many posts, posts have many comments, users have many posts and comments __
This is more of a demo to meet the scope of this project, but adding authentication and votes would be the next logical step in this project.

I will create a simple client for this service that will execute all the CRUD methods on some demo data.