from flask import Flask, jsonify, request


from flask.ext.sqlalchemy import SQLAlchemy

from model import db, init_db, Vote


app = Flask(__name__)
app = init_db(app)


app.config.from_object('model')
app = init_db(app)
 
@app.before_first_request
def init():
    db.create_all()


@app.route("/")
def index():
#Render static html
	print "dsfdsf"

@app.route("/supersecurevote", methods=['POST'])
def vote():
	if request.method == 'POST':
		responseVote = request.form['vote']
		if responseVote == True:
			newVote = Vote(True)
		else:
			newVote = Vote(False)
		db.session.add(newVote)
		db.session.commit()

		return jsonify(response="OK")
	else:
		return jsonify(response="FAILED")		




@app.route("/votestats", methods=['GET'])
def stats():
	deerCount = Vote.query.filter_by(vote=True).count()
	bearCount = Vote.query.filter_by(vote=False).count()
	return jsonify(deers = deerCount, bears = bearCount)





if __name__ == "__main__":
	app.debug = True
	app.run()





