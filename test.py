
game_features = {
    'home_team_api_id': [10269],
    'away_team_api_id': [9823],
    'home_team_goal': [0],
    'away_team_goal': [1],
}


pred = model.predict(pd.DataFrame(game_features))
print(pred)
