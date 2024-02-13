import sqlite3
import pandas as pd
import numpy as np


def getData():
    database = 'database.sqlite'
    conn = sqlite3.connect(database)
    player_data = pd.read_sql("SELECT * FROM Player;", conn)
    player_stats_data = pd.read_sql("SELECT * FROM Player_Attributes;", conn)
    team_data = pd.read_sql("SELECT * FROM Team;", conn)
    match_data = pd.read_sql("SELECT * FROM Match;", conn)
    match_data['date'] = pd.to_datetime(match_data['date'], format='%Y-%m-%d 00:00:00')

    return player_data, player_stats_data, team_data, match_data


def add_overall_rating(match_data, player_stats_data):
    home_players = ["home_player_" + str(x) for x in range(1, 12)]
    away_players = ["away_player_" + str(x) for x in range(1, 12)]

    for player in home_players:
        match_data = pd.merge(match_data, player_stats_data[["id", "overall_rating"]], left_on=[player],
                              right_on=["id"],
                              suffixes=["", "_" + player])
    for player in away_players:
        match_data = pd.merge(match_data, player_stats_data[["id", "overall_rating"]], left_on=[player],
                              right_on=["id"],
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

    return match_data


def add_outcome(match_data):
    match_data['goal_difference'] = match_data['home_team_goal'] - match_data['away_team_goal']
    match_data['home_status'] = 'D'
    match_data['home_status'] = np.where(match_data['goal_difference'] > 0, 'W', match_data['home_status'])
    match_data['home_status'] = np.where(match_data['goal_difference'] < 0, 'L', match_data['home_status'])

    # print percentage of home wins and losses and draws
    print(f"Percentage of home wins: {len(match_data[match_data['home_status'] == 'W']) / len(match_data) * 100}")
    print(f"Percentage of home losses: {len(match_data[match_data['home_status'] == 'L']) / len(match_data) * 100}")
    print(f"Percentage of home draws: {len(match_data[match_data['home_status'] == 'D']) / len(match_data) * 100}")

    return match_data

