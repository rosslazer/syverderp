from flask import Flask, jsonify


from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)



@app.route("/")
def index():
#Render static html

@app.route("/supersecurevote", methods=['POST'])
def vote():
	if request.method == 'POST':
		responseVote = request.form['vote']
		newVote = Vote(responseVote)
		db.session.add(newVote)
		 db.session.commit()
		return jsonify(response="OK")
	else:
		return jsonify(response="FAILED")		




@app.route("/supersecurevote", methods=['GET'])
def stats():
	



if __name__ == "__main__":
    app.run()




class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    facebookID = db.Column(db.String(120), unique=True)
    #True is deer false is bear
    vote = db.Column(db.Boolean)



    def __init__(self, theirvote):
        self.vote = theirvote

    # def __repr__(self):
    #     return '<User %r>' % self.username



