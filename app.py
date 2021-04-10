from flask import Flask, request, url_for, redirect, render_template
from prediction import random_forest, neural_networks, decision_tree, k_nearest_neighbors
from prediction import prediction_of_score
from prediction import MODEL_INFO

app = Flask(__name__)

MODELS = { 
	'Random Forest' : random_forest,
	'Neural Networks' : neural_networks,
	'Decision Tree' : decision_tree,
	'K-Nearest Neighbors' : k_nearest_neighbors
}

TEAM_CODE = ['Chennai Super Kings','Mumbai Indians','Rajasthan Royals','Kolkata Knight Riders',
			'Kings XI Punjab','Sunrisers Hyderabad','Delhi Daredevils','Royal Challengers Bangalore']

score_predicted = None

@app.route('/')
def home_page():
	return render_template('home_page.html', models=MODELS, teams=TEAM_CODE,  info=MODEL_INFO, score=score_predicted)

@app.route('/prediction', methods=['GET', 'POST'])
def prediction_page():
	global score_predicted
	global total
	if request.method == 'POST':
		requests = request.form
		batting_team = requests['batting_team']
		bowling_team = requests['bowling_team']
		runs = int(requests['runs'])
		overs = float(requests['overs'])
		wickets = int(requests['wickets'])
		runs_last_5 = int(requests['runs_last_5'])
		wickets_last_5 = int(requests['wickets_last_5'])
		model = MODELS[requests['model']]
		score_predicted = str(prediction_of_score(batting_team, bowling_team, runs, wickets, overs, runs_last_5, wickets_last_5, model))
		return render_template('prediction_page.html', score=score_predicted, info=dict(requests), model=MODEL_INFO)

@app.errorhandler(404)
def error(e):
	return render_template("error_page.html", msg=e)

if __name__ == '__main__':
	app.run(debug=True, port=1000)