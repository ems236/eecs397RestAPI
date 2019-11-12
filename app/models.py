from app import db
import json

class UserPostVote(db.Model):
    __tablename__ = 'user_post_vote'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), primary_key=True)
    vote = db.Column(db.Integer)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    votes = db.relationship("UserPostVote", backref="user", lazy=False)
    posts = db.relationship("Post", backref="user", lazy=True)
    #comments = db.relationship("Comment", backref="user", lazy=True)

    def serialize(self):
        return {"id": self.id, "name": self.name}


class Topic(db.Model):
    __tablename__ = 'topic'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    posts = db.relationship("Post", backref="topic", lazy=False)

    def serialize(self):
        return {"id": self.id, "name": self.name}


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String)
    detail = db.Column(db.String)

    #comments = db.relationship("Comment", backref="post", lazy=False)
    votes = db.relationship("UserPostVote", backref="post", lazy=False)

    def serialize(self):
        return {"id": self.id, "user_id": self.user_id, "title": self.title, "detail": self.detail}
        
"""
class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    text = db.Column(db.String)

    def serialize(self):
        return {"id": self.id, "user_id": self.user_id, "text": self.text}
"""