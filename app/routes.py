from flask import abort, request, jsonify, make_response
from app.models import * 
from app import app, db
from sqlalchemy import func, sum

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
    topic = model_by_id(Topic, topic_id)
    if topic is None:
        return abort(400)
    
    if request.method == GET:
        return success_response(topic.serialize())

    if request.method == PUT:
        if not request.json or not request.json["name"]:
            return abort(400)
        topic.name = request.json["name"]
        db.session.commit()
        return success_response({"success": True})

    if request.method == DELETE:
        db.session.delete(topic)
        db.session.commit()
        return success_response({"success": True})


@app.route('/topics/<int:topic_id>/posts', methods=[GET])
def posts_get(topic_id):
    posts = Post.query.filter(Post.topic_id == topic_id).all()
    return success_response(serialize_models(posts))

@app.route('/topics<int:topic_id>/posts', methods=[POST])
def posts_post(topic_id):
    if not request.json or not request.json["user_id"] or not request.json["title"] or not request.json["detail"]:
        return abort(400)

    topic = model_by_id(Topic, topic_id)
    user = model_by_id(User, request.json["user_id"])
    if topic is None or user is None:
        return abort(400)
    
    new_post = Post()
    new_post.topic_id = topic_id 
    new_post.title = request.json["title"]
    new_post.detail = request.json["detail"]
    new_post.user_id = request.json["user_id"]

    db.session.add(new_post)
    db.session.commit()

    return success_response({"id": new_post.id})

@app.route('/topics/<int:topic_id>/posts/<int:post_id>', methods=[GET, PUT, DELETE])
def post_id(topic_id, post_id):
    post = Post.query.filter(Post.id == post_id and topic_id == topic_id).first()

    if post is None:
        return abort(400)
    
    if request.method == GET:
        return success_response(post.serialize())

    if request.method == PUT:
        if not request.json or not request.json["user_id"] or not request.json["title"] or not request.json["detail"]:
            return abort(400)
        post.user_id = request.json["user_id"]
        post.title = request.json["title"]
        post.detail = request.json["detail"]
        db.session.commit()
        return success_response({"success": True})

    if request.method == DELETE:
        db.session.delete(post)
        db.session.commit()
        return success_response({"success": True})


@app.route('/topics/<int:topic_id>/posts/<int:post_id>/votes', methods=[GET])
def votes_get(topic_id, post_id):
    post = Post.query.filter(Post.id == post_id and topic_id == topic_id).first()

    if post is None:
        return abort(400)

    count = db.session.query(func.sum(UserPostVote.vote)).filter(UserPostVote.post_id == post_id).scalar()
    users = list(map(lambda x: x.user_id, post.votes))
    return success_response({"count": count, "users": users})


@app.route('/topics/<int:topic_id>/posts/<int:post_id>/votes/<int:user_id>', methods=[GET, PUT, DELETE, POST])
def votes_user_id(topic_id, post_id, user_id):
    post = Post.query.filter(Post.id == post_id and topic_id == topic_id).first()
    user = model_by_id(User, user_id)
    if post is None or user is None:
        return abort(400)

    current_vote = UserPostVote.query.filter(UserPostVote.post_id == post_id and UserPostVote.user_id == user_id)

    if request.method == POST:
        if not request.json or not request.json["value"] or current_vote is not None:
            return abort(400)
        
        new_vote = UserPostVote()
        new_vote.vote = request.json["value"]
        new_vote.post = post
        new_vote.user = user

        db.session.add(new_vote)
        db.session.commit()
    
    
    current_vote = UserPostVote.query.filter(UserPostVote.post_id == post_id and UserPostVote.user_id == user_id)
    if current_vote is None:
        return abort(400)
    if request.method == PUT:
        if not request.json or not request.json["value"]:
            return abort(400)
        
        current_vote.vote = request.json["value"]

        db.session.commit()
        return success_response({"success": True})

    if request.method == DELETE:
        db.session.delete(post)
        db.session.commit()
        return success_response({"success": True})

    if request.method == GET:
        return success_response({"vote": current_vote.vote})



@app.route('/users', methods=[GET])
def users_get():
    users = User.query.all()
    return success_response(serialize_models(users))

@app.route('/users', methods=[POST])
def users_post():
    if not request.json or not request.json["name"]:
        return abort(400)
    
    new_user = User()
    new_user.name = request.json["name"]

    db.session.add(new_user)
    db.session.commit()

    return success_response({"id": new_user.id})

@app.route('/users/<int:user_id>', methods=[GET, PUT, DELETE])
def user_id(user_id):
    user = model_by_id(User, topic_id)
    if user is None:
        return abort(400)
    
    if request.method == GET:
        return success_response(user.serialize())

    if request.method == PUT:
        if not request.json or not request.json["name"]:
            return abort(400)
        user.name = request.json["name"]
        db.session.commit()
        return success_response({"success": True})

    if request.method == DELETE:
        db.session.delete(user)
        db.session.commit()
        return success_response({"success": True})


"""
@app.route('/topics/<int:id>/posts/<int:post_id>/comments', methods=[GET, POST])
def comments(topic_id, post_id):
    pass

@app.route('/topics/<int:topic_id>/posts/<int:post_id>/comments/<int:comment_id>', methods=[GET, PUT, DELETE])
def comment_id(topic_id, post_id, comment_id):
    pass
"""
