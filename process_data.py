import sqlite3
import pandas as pd
import numpy as np

from xml_events_parsing import get_foulcommit_events, get_goal_events, get_shoton_events, get_shotoff_events, get_cards


def getData():
    database = 'database.sqlite'
    conn = sqlite3.connect(database)
    player_data = pd.read_sql("SELECT * FROM Player;", conn)
    player_stats_data = pd.read_sql("SELECT * FROM Player_Attributes;", conn)
    team_data = pd.read_sql("SELECT * FROM Team;", conn)
    match_data = pd.read_sql("SELECT * FROM Match where goal is not null ;", conn)
    match_data['date'] = pd.to_datetime(match_data['date'], format='%Y-%m-%d 00:00:00')

    return player_data, player_stats_data, team_data, match_data


def add_cards(match_data):
    # Initialize empty lists for each new column
    home_yellow_before_half = []
    home_yellow_after_half = []
    away_yellow_before_half = []
    away_yellow_after_half = []
    total_yellow_before_half = []
    total_yellow_after_half = []
    home_red_before_half = []
    home_red_after_half = []
    away_red_before_half = []
    away_red_after_half = []
    total_red_before_half = []
    total_red_after_half = []
    home_card_score = []
    away_card_score = []
    card_score = []
    # Iterate over each row in the DataFrame
    for index, row in match_data.iterrows():
        # Extract the necessary values from the row


        xml_card_data = row['card']
        home_team_id = row['home_team_api_id']
        away_team_id = row['away_team_api_id']

        # Get the card data
        card_data = get_cards(xml_card_data, home_team_id, away_team_id)

        # Add the card data to the respective lists
        home_yellow_before_half.append(card_data[0])
        home_yellow_after_half.append(card_data[1])
        away_yellow_before_half.append(card_data[2])
        away_yellow_after_half.append(card_data[3])
        total_yellow_before_half.append(card_data[4])
        total_yellow_after_half.append(card_data[5])
        home_red_before_half.append(card_data[6])
        home_red_after_half.append(card_data[7])
        away_red_before_half.append(card_data[8])
        away_red_after_half.append(card_data[9])
        total_red_before_half.append(card_data[10])
        total_red_after_half.append(card_data[11])
        home_card_score.append(card_data[12])
        away_card_score.append(card_data[13])
        card_score.append(card_data[14])

    # Add the new columns to the DataFrame
    match_data['home_yellow_before_half'] = home_yellow_before_half
    match_data['home_yellow_after_half'] = home_yellow_after_half
    match_data['away_yellow_before_half'] = away_yellow_before_half
    match_data['away_yellow_after_half'] = away_yellow_after_half
    match_data['total_yellow_before_half'] = total_yellow_before_half
    match_data['total_yellow_after_half'] = total_yellow_after_half
    match_data['home_red_before_half'] = home_red_before_half
    match_data['home_red_after_half'] = home_red_after_half
    match_data['away_red_before_half'] = away_red_before_half
    match_data['away_red_after_half'] = away_red_after_half
    match_data['total_red_before_half'] = total_red_before_half
    match_data['total_red_after_half'] = total_red_after_half
    match_data['home_card_score'] = home_card_score
    match_data['away_card_score'] = away_card_score
    match_data['card_score'] = card_score

    return match_data


def add_fouls(match_data):
    # Iterate over each row in the DataFrame
    for index, row in match_data.iterrows():
        # Initialize empty lists for each new column
        home_fouls_before_half = []
        home_fouls_after_half = []
        away_fouls_before_half = []
        away_fouls_after_half = []
        total_fouls_before_half = []
        total_fouls_after_half = []
        # Extract the necessary values from the row
        xml_foulcommit_data = row['foulcommit']
        home_team_id = row['home_team_api_id']
        away_team_id = row['away_team_api_id']

        # Get the fouls data
        fouls_data = get_foulcommit_events(xml_foulcommit_data, home_team_id, away_team_id)

        # Add the fouls data to the respective lists
        home_fouls_before_half.append(fouls_data[0])
        home_fouls_after_half.append(fouls_data[1])
        away_fouls_before_half.append(fouls_data[2])
        away_fouls_after_half.append(fouls_data[3])
        total_fouls_before_half.append(fouls_data[4])
        total_fouls_after_half.append(fouls_data[5])

    # Add the new columns to the DataFrame
    match_data['home_fouls_before_half'] = home_fouls_before_half
    match_data['home_fouls_after_half'] = home_fouls_after_half
    match_data['away_fouls_before_half'] = away_fouls_before_half
    match_data['away_fouls_after_half'] = away_fouls_after_half
    match_data['total_fouls_before_half'] = total_fouls_before_half
    match_data['total_fouls_after_half'] = total_fouls_after_half

    return match_data


def add_shotoff(match_data):
    # Iterate over each row in the DataFrame
    for index, row in match_data.iterrows():
        # Initialize empty lists for each new column
        home_shotoff_before_half = []
        home_shotoff_after_half = []
        away_shotoff_before_half = []
        away_shotoff_after_half = []
        total_shotoff_before_half = []
        total_shotoff_after_half = []
        # Extract the necessary values from the row
        xml_foulcommit_data = row['shotoff']
        home_team_id = row['home_team_api_id']
        away_team_id = row['away_team_api_id']

        # Get the shotoff data
        shotoff_data = get_shotoff_events(xml_foulcommit_data, home_team_id, away_team_id)

        # Add the shotoff data to the respective lists
        home_shotoff_before_half.append(shotoff_data[0])
        home_shotoff_after_half.append(shotoff_data[1])
        away_shotoff_before_half.append(shotoff_data[2])
        away_shotoff_after_half.append(shotoff_data[3])
        total_shotoff_before_half.append(shotoff_data[4])
        total_shotoff_after_half.append(shotoff_data[5])

    # Add the new columns to the DataFrame
    match_data['home_shotoff_before_half'] = home_shotoff_before_half
    match_data['home_shotoff_after_half'] = home_shotoff_after_half
    match_data['away_shotoff_before_half'] = away_shotoff_before_half
    match_data['away_shotoff_after_half'] = away_shotoff_after_half
    match_data['total_shotoff_before_half'] = total_shotoff_before_half
    match_data['total_shotoff_after_half'] = total_shotoff_after_half

    return match_data


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


def add_shoton(match_data):
    # Iterate over each row in the DataFrame
    for index, row in match_data.iterrows():
        # Initialize the lists for this row
        home_shoton_before_half = []
        home_shoton_after_half = []
        away_shoton_before_half = []
        away_shoton_after_half = []
        total_shoton_before_half = []
        total_shoton_after_half = []

        # Extract the necessary values from the row
        xml_shoton_data = row['shoton']
        home_team_id = row['home_team_api_id']
        away_team_id = row['away_team_api_id']

        # Get the shoton on goal data
        shoton_data = get_shoton_events(xml_shoton_data, home_team_id, away_team_id)

        # Add the shoton on goal data to the respective lists
        home_shoton_before_half.append(shoton_data[0])
        home_shoton_after_half.append(shoton_data[1])
        away_shoton_before_half.append(shoton_data[2])
        away_shoton_after_half.append(shoton_data[3])
        total_shoton_before_half.append(shoton_data[4])
        total_shoton_after_half.append(shoton_data[5])

        # Add the new columns to the DataFrame
        match_data['home_shoton_before_half'] = home_shoton_before_half
        match_data['home_shoton_after_half'] = home_shoton_after_half
        match_data['away_shoton_before_half'] = away_shoton_before_half
        match_data['away_shoton_after_half'] = away_shoton_after_half
        match_data['total_shoton_before_half'] = total_shoton_before_half
        match_data['total_shoton_after_half'] = total_shoton_after_half

    return match_data


def add_goals(match_data):
    # Iterate over each row in the DataFrame
    # Initialize empty lists for each new column
    home_goals_before_half = []
    home_goals_after_half = []
    away_goals_before_half = []
    away_goals_after_half = []
    total_goals_before_half = []
    total_goals_after_half = []

    for index, row in match_data.iterrows():

        # Extract the necessary values from the row
        xml_goal_data = row['goal']
        home_team_id = row['home_team_api_id']
        away_team_id = row['away_team_api_id']
        if xml_goal_data is not None:
            goals_data = get_goal_events(xml_goal_data, home_team_id, away_team_id)

            # Add the goals data to the respective lists
            home_goals_before_half.append(goals_data[0])
            home_goals_after_half.append(goals_data[1])
            away_goals_before_half.append(goals_data[2])
            away_goals_after_half.append(goals_data[3])
            total_goals_before_half.append(goals_data[4])
            total_goals_after_half.append(goals_data[5])
        else:
            home_goals_before_half.append(None)
            home_goals_after_half.append(None)
            away_goals_before_half.append(None)
            away_goals_after_half.append(None)
            total_goals_before_half.append(None)
            total_goals_after_half.append(None)

    # Add the new columns to the DataFrame
    match_data['home_goals_before_half'] = home_goals_before_half
    match_data['home_goals_after_half'] = home_goals_after_half
    match_data['away_goals_before_half'] = away_goals_before_half
    match_data['away_goals_after_half'] = away_goals_after_half
    match_data['total_goals_before_half'] = total_goals_before_half
    match_data['total_goals_after_half'] = total_goals_after_half

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
