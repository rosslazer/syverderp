from flask import Flask


from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)



@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()




class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    facebookID = db.Column(db.String(120), unique=True)
    #True is deer false is bear
    vote = db.Column(db.Boolean)



    def __init__(self, fbid, theirvote):
        self.facebookID = username
        self.vote = theirvote

    # def __repr__(self):
    #     return '<User %r>' % self.username