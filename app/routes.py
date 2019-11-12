from flask import abort, request, jsonify, make_response
from app.models import * 
from app import app, db

GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'

def success_response(data):
    return make_response(jsonify(data), 200)

def model_by_id(Model, id):
    return Model.query.filter(Model.id == id).first()

def serialize_models(models):
    return list(map(lambda x: x.serialze(), models))


@app.route('/topics', methods=[GET])
def topics_get():
    topics = Topic.query.all()
    return success_response(serialize_models(topics))

@app.route('/topics', methods=[POST])
def topics_post():
    if not request.json or not request.json["name"]:
        return abort(400)

    new_topic = Topic()
    new_topic.name = request.json["name"]

    db.session.add(new_topic)
    db.session.commit()

    return success_response({"id": new_topic.id})

@app.route('/topics/<int:topic_id>', methods=[GET, PUT, DELETE])
def topic_id(topic_id):
    pass

@app.route('/topics/<int:topic_id>/posts', methods=[GET])
def posts_get(topic_id):
    pass

@app.route('/topics', methods=[POST])
def topics_post():
    if not request.json or not request.json["name"]:
        return abort(400)

    new_topic = Topic()
    new_topic.name = request.json["name"]

    db.session.add(new_topic)
    db.session.commit()

    return success_response({"id": new_topic.id})

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

