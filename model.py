from flask import Flask, jsonify

import os


from flask.ext.sqlalchemy import SQLAlchemy


SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

db = SQLAlchemy()


class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #True is deer false is bear
    vote = db.Column(db.Boolean)



    def __init__(self, theirvote):
        self.vote = theirvote

 
def init_db(app):
    db.init_app(app)
    return app


