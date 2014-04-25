from flask import Flask, jsonify



from flask.ext.sqlalchemy import SQLAlchemy


SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

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


