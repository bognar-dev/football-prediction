import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from time import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score

start = time()
## Fetching data
# Connecting to database

database = 'database.sqlite'
conn = sqlite3.connect(database)
print(conn)

# Defining the number of jobs to be run in parallel during grid search
n_jobs = 1  # Insert number of parallel jobs here

# Fetching required data tables
player_data = pd.read_sql("SELECT * FROM Player;", conn)
player_stats_data = pd.read_sql("SELECT * FROM Player_Attributes;", conn)
team_data = pd.read_sql("SELECT * FROM Team;", conn)
match_data = pd.read_sql("SELECT * FROM Match;", conn)

match_data['date'] = pd.to_datetime(match_data['date'], format='%Y-%m-%d 00:00:00')

home_players = ["home_player_" + str(x) for x in range(1, 12)]
away_players = ["away_player_" + str(x) for x in range(1, 12)]

betting_columns = ["B365H", "B365D", "B365A"]

matches_kept_columns = ["id", "date", "home_team_api_id", "away_team_api_id", "home_team_goal", "away_team_goal"]
matches_kept_columns = matches_kept_columns + home_players
matches_kept_columns = matches_kept_columns + away_players
matches_kept_columns = matches_kept_columns + betting_columns

match_data = match_data[matches_kept_columns]

match_data['goal_difference'] = match_data['home_team_goal'] - match_data['away_team_goal']
match_data['home_status'] = 'D'
match_data['home_status'] = np.where(match_data['goal_difference'] > 0, 'W', match_data['home_status'])
match_data['home_status'] = np.where(match_data['goal_difference'] < 0, 'L', match_data['home_status'])

for player in home_players:
    match_data = pd.merge(match_data, player_stats_data[["id", "overall_rating"]], left_on=[player], right_on=["id"],
                          suffixes=["", "_" + player])
for player in away_players:
    match_data = pd.merge(match_data, player_stats_data[["id", "overall_rating"]], left_on=[player], right_on=["id"],
                          suffixes=["", "_" + player])

match_data = match_data.rename(columns={"overall_rating": "overall_rating_home_player_1"})

match_data = match_data[match_data[['overall_rating_' + p for p in home_players]].isnull().sum(axis=1) <= 0]
match_data = match_data[match_data[['overall_rating_' + p for p in away_players]].isnull().sum(axis=1) <= 0]

match_data['overall_rating_home'] = match_data[['overall_rating_' + p for p in home_players]].sum(axis=1)
match_data['overall_rating_away'] = match_data[['overall_rating_' + p for p in away_players]].sum(axis=1)
match_data['overall_rating_difference'] = match_data['overall_rating_home'] - match_data['overall_rating_away']

match_data['min_overall_rating_home'] = match_data[['overall_rating_' + p for p in home_players]].min(axis=1)
match_data['min_overall_rating_away'] = match_data[['overall_rating_' + p for p in away_players]].min(axis=1)

match_data['max_overall_rating_home'] = match_data[['overall_rating_' + p for p in home_players]].max(axis=1)
match_data['max_overall_rating_away'] = match_data[['overall_rating_' + p for p in away_players]].max(axis=1)

match_data['mean_overall_rating_home'] = match_data[['overall_rating_' + p for p in home_players]].mean(axis=1)
match_data['mean_overall_rating_away'] = match_data[['overall_rating_' + p for p in away_players]].mean(axis=1)

match_data['std_overall_rating_home'] = match_data[['overall_rating_' + p for p in home_players]].std(axis=1)
match_data['std_overall_rating_away'] = match_data[['overall_rating_' + p for p in away_players]].std(axis=1)

columns_list = match_data.columns.tolist()
print(columns_list)

X = match_data[['home_team_api_id', 'away_team_api_id', 'home_team_goal', 'away_team_goal',
                 ]]
y = match_data['home_status']  # Assuming 'home_status' is your target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
conf_matrix = confusion_matrix(y_test, predictions)

print("Accuracy:", accuracy)
# Calculate and print precision, recall, and F1-score
precision = precision_score(y_test, predictions, average='weighted')
recall = recall_score(y_test, predictions, average='weighted')
f1 = f1_score(y_test, predictions, average='weighted')

print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1-score: {f1}")


game_features = {
    'home_team_api_id': [10269],
    'away_team_api_id': [9823],
    'home_team_goal': [0],
    'away_team_goal': [1],
}


pred = model.predict(pd.DataFrame(game_features))
print(pred)