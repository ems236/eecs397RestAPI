from flask import abort, request, jsonify, make_response
from app.models import * 
from app import app

GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'

SUCCESS_RESPONSE = make_response(jsonify({"success":True}), 200)

@app.route('/topics', methods=[GET])
def topics_get():
    topics = Topic.query.all()


@app.route('/topics', methods=[POST])
def topics_post():
    if not request.json:
        return abort(400)
    
    new_post = json.loads(request

    return 

@app.route('/topics/<int:topic_id>', methods=[GET, PUT, DELETE])
def topic_id(topic_id):
    pass

@app.route('/topics/<int:topic_id>/posts', methods=[GET, POST])
def posts(topic_id):
    pass

@app.route('/topics/<int:topic_id>/posts/<int:post_id>', methods=[GET, PUT, DELETE])
def post_id(topic_id, post_id):
    pass

@app.route('/topics/<int:id>/posts/<int:post_id>/comments', methods=[GET, POST])
def comments(topic_id, post_id):
    pass

@app.route('/topics/<int:topic_id>/posts/<int:post_id>/comments/<int:comment_id>', methods=[GET, PUT, DELETE])
def comment_id(topic_id, post_id, comment_id):
    pass

@app.route('/users', methods=[GET, POST])
def users():
    pass

@app.route('/users/<int:user_id>', methods=[GET, PUT, DELETE])
def user_id(user_id):
    pass

