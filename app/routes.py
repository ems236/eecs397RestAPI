from flask import abort, request
from app.models import * 
from app import app
import json

GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'

@app.route('/topics', methods=[GET, POST])
def topics():
    return json.dumps(Topic.query.all())

@app.route('/topics/<int:topic_id>', methods=[GET, PUT, DELETE])
def topic_id():
    pass

@app.route('/topics/<int:topic_id>/posts', methods=[GET, POST])
def posts():
    pass

@app.route('/topics/<int:topic_id>/posts/<int:post_id>', methods=[GET, PUT, DELETE])
def post_id():
    pass

@app.route('/topics/<int:id>/posts/<int:post_id>/comments', methods=[GET, POST])
def comments():
    pass

@app.route('/topics/<int:topic_id>/posts/<int:post_id>/comments/<int:comment_id>', methods=[GET, PUT, DELETE])
def comment_id():
    pass

@app.route('/users', methods=[GET, POST])
def users():
    pass

@app.route('/users/<int:user_id>', methods=[GET, PUT, DELETE])
def user_id():
    pass