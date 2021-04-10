from joblib import load
import numpy as np
import os

random_forest = load(os.path.join(os.getcwd(), 'models', 'random_forest.pkl'))
neural_networks = load(os.path.join(os.getcwd(), 'models', 'neural_networks.pkl'))
decision_tree = load(os.path.join(os.getcwd(), 'models', 'decision_tree.pkl'))
k_nearest_neighbors = load(os.path.join(os.getcwd(), 'models', 'k_nearest_neighbors.pkl'))


MODEL_INFO = {
  'Random Forest' :  {'accuracy' : 94.27, 'error' : 7.14},
  'Neural Networks' : {'accuracy' : 89.46, 'error' : 9.22},
  'Decision Tree' :  {'accuracy' : 88.46, 'error' : 10.12},
  'K-Nearest Neighbors' : {'accuracy' : 85.69, 'error' : 11.30}
} 

def prediction_of_score(batting_team, bowling_team, runs, wickets, overs, runs_last_5, wickets_last_5, model):
  team = []

  # Batting Team
  if batting_team == 'Chennai Super Kings': team = team + [1,0,0,0,0,0,0,0]
  elif batting_team == 'Mumbai Indians': team = team + [0,1,0,0,0,0,0,0]
  elif batting_team == 'Rajasthan Royals': team = team + [0,0,1,0,0,0,0,0]
  elif batting_team == 'Kolkata Knight Riders': team = team + [0,0,0,1,0,0,0,0]
  elif batting_team == 'Kings XI Punjab': team = team + [0,0,0,0,1,0,0,0]
  elif batting_team == 'Sunrisers Hyderabad': team = team + [0,0,0,0,0,1,0,0]
  elif batting_team == 'Delhi Daredevils': team = team + [0,0,0,0,0,0,1,0]
  elif batting_team == 'Royal Challengers Bangalore': team = team + [0,0,0,0,0,0,0,1]

  # Bowling Team
  if bowling_team == 'Chennai Super Kings': team = team + [1,0,0,0,0,0,0,0]
  elif bowling_team == 'Mumbai Indians': team = team + [0,1,0,0,0,0,0,0]
  elif bowling_team == 'Rajasthan Royals': team = team + [0,0,1,0,0,0,0,0]
  elif bowling_team == 'Kolkata Knight Riders': team = team + [0,0,0,1,0,0,0,0]
  elif bowling_team == 'Kings XI Punjab': team = team + [0,0,0,0,1,0,0,0]
  elif bowling_team == 'Sunrisers Hyderabad': team = team + [0,0,0,0,0,1,0,0]
  elif bowling_team == 'Delhi Daredevils': team = team + [0,0,0,0,0,0,1,0]
  elif bowling_team == 'Royal Challengers Bangalore': team = team + [0,0,0,0,0,0,0,1]

  features = team + [runs, wickets, overs, runs_last_5, wickets_last_5]
  features = np.array([features])
  predictions = model.predict(features)
  return int(round(predictions[0]))