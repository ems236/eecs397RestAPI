The first deliverable is a short write-up where:
1. You will share some of the ways you hope to use Python going forward. Are you hoping
to use it for AI, data analysis, game development, etc.?
2. You will identify Python modules that can help you with what you describe in point 1.
3. Pick a module and describe a short project/prototype you can start to develop. Aim for
something that is beyond the level of a tutorial, but slightly less than a hack-a-thon
project (usually something developed by a small group over a weekend). Aim for
something that can be demonstrated either through running the Python code on its own,
or can be visualized and demonstrated using a Jupyter Notebook.


1: I don't really know how I expect to use python.  It's nice to know a convenient and cross platform scripting language; I may just use it to write small tools for myself.  I have no interest at all in data science or machine learning, so I hopefully can avoid most of the data analysis side of python.  I am interested in iot, so I expect to mostly work on scripts and networking in python.

2: For networking, I would likely need to call web service. This should be pretty easy because python is dynamically typed and deserializing json should be trivial.  
To work with this, I will use the requests module.  
I may also have to write my own REST services in python.  That would most easily be done with Flask.  
For data storage to make my webservice useful, I would need some database client to use with a sqllite database.  The most popular option for this appears to be using SQLAlchemy as an ORM.
Other modules that would be useful would be UWSGI for actual web hosting, paho-mqtt for message passing, and pyOpenSSL for security.
For general scripting, it would be good to know some modules for XML and YAML parsing. ElementTree seems good for xml, and pyYaml would be good for yaml.

3: I will make a flask app that will host a rest api to communicate with a database.