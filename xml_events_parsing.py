import xml.etree.ElementTree as ET


def get_goal_events(xml_goal_data, home_team_id, away_team_id):
    root = ET.fromstring(xml_goal_data)

    home_goals_before_half = 0
    home_goals_after_half = 0
    away_goals_before_half = 0
    away_goals_after_half = 0
    total_goals_before_half = 0
    total_goals_after_half = 0

    for value in root.findall('value'):
        stats = value.find('stats')
        if stats is not None and stats.find('goals') is not None:
            elapsed = int(value.find('elapsed').text)
            team_id = int(value.find('team').text)
            if team_id == home_team_id:
                if elapsed <= 45:
                    home_goals_before_half += 1
                    total_goals_before_half += 1
                else:
                    home_goals_after_half += 1
                    total_goals_after_half += 1
            elif team_id == away_team_id:
                if elapsed <= 45:
                    away_goals_before_half += 1
                    total_goals_before_half += 1
                else:
                    away_goals_after_half += 1
                    total_goals_after_half += 1

    return home_goals_before_half, \
        home_goals_after_half, \
        away_goals_before_half, \
        away_goals_after_half, \
        total_goals_before_half, \
        total_goals_after_half


def get_shoton_events(xml_shoton_data, home_team_id, away_team_id):
    root = ET.fromstring(xml_shoton_data)

    home_shots_before_half = 0
    home_shots_after_half = 0
    away_shots_before_half = 0
    away_shots_after_half = 0
    total_shots_before_half = 0
    total_shots_after_half = 0

    for value in root.findall('value'):
        stats = value.find('stats')
        if stats is not None and stats.find('shoton') is not None:
            elapsed = int(value.find('elapsed').text)
            if value.find('team') is None:
                team_id = home_team_id
            else:
                team_id = int(value.find('team').text)
            if team_id == home_team_id:
                if elapsed <= 45:
                    home_shots_before_half += 1
                    total_shots_before_half += 1
                else:
                    home_shots_after_half += 1
                    total_shots_after_half += 1
            elif team_id == away_team_id:
                if elapsed <= 45:
                    away_shots_before_half += 1
                    total_shots_before_half += 1
                else:
                    away_shots_after_half += 1
                    total_shots_after_half += 1

    return home_shots_before_half, \
        home_shots_after_half, \
        away_shots_before_half, \
        away_shots_after_half, \
        total_shots_before_half, \
        total_shots_after_half


def get_shotoff_events(xml_shotoff_data, home_team_id, away_team_id):
    root = ET.fromstring(xml_shotoff_data)

    home_shots_off_before_half = 0
    home_shots_off_after_half = 0
    away_shots_off_before_half = 0
    away_shots_off_after_half = 0
    total_shots_off_before_half = 0
    total_shots_off_after_half = 0

    for value in root.findall('value'):
        stats = value.find('stats')
        if stats is not None and stats.find('shotoff') is not None:
            elapsed = int(value.find('elapsed').text)
            if value.find('team') is None:
                team_id = home_team_id
            else:
                team_id = int(value.find('team').text)
            if team_id == home_team_id:
                if elapsed <= 45:
                    home_shots_off_before_half += 1
                    total_shots_off_before_half += 1
                else:
                    home_shots_off_after_half += 1
                    total_shots_off_after_half += 1
            elif team_id == away_team_id:
                if elapsed <= 45:
                    away_shots_off_before_half += 1
                    total_shots_off_before_half += 1
                else:
                    away_shots_off_after_half += 1
                    total_shots_off_after_half += 1

    return home_shots_off_before_half, \
        home_shots_off_after_half, \
        away_shots_off_before_half, \
        away_shots_off_after_half, \
        total_shots_off_before_half, \
        total_shots_off_after_half


def get_foulcommit_events(xml_foulcommit_data, home_team_id, away_team_id):
    root = ET.fromstring(xml_foulcommit_data)

    home_fouls_before_half = 0
    home_fouls_after_half = 0
    away_fouls_before_half = 0
    away_fouls_after_half = 0
    total_fouls_before_half = 0
    total_fouls_after_half = 0

    for value in root.findall('value'):
        stats = value.find('stats')
        if stats is not None and stats.find('foulscommitted') is not None:
            elapsed = int(value.find('elapsed').text)
            team_id = int(value.find('team').text)
            if team_id == home_team_id:
                if elapsed <= 45:
                    home_fouls_before_half += 1
                    total_fouls_before_half += 1
                else:
                    home_fouls_after_half += 1
                    total_fouls_after_half += 1
            elif team_id == away_team_id:
                if elapsed <= 45:
                    away_fouls_before_half += 1
                    total_fouls_before_half += 1
                else:
                    away_fouls_after_half += 1
                    total_fouls_after_half += 1

    return home_fouls_before_half, \
        home_fouls_after_half, \
        away_fouls_before_half, \
        away_fouls_after_half, \
        total_fouls_before_half, \
        total_fouls_after_half


def get_cards(xml_card_data, home_team_id, away_team_id):
    root = ET.fromstring(xml_card_data)

    home_yellow_before_half = 0
    home_yellow_after_half = 0
    away_yellow_before_half = 0
    away_yellow_after_half = 0
    total_yellow_before_half = 0
    total_yellow_after_half = 0
    home_red_before_half = 0
    home_red_after_half = 0
    away_red_before_half = 0
    away_red_after_half = 0
    total_red_before_half = 0
    total_red_after_half = 0
    home_card_score = 0
    away_card_score = 0
    card_score = 0

    for value in root.findall('value'):
        if value.find('team') is None:
            team_id = home_team_id
        else:
            team_id = int(value.find('team').text)
        if value.find('card_type') is None:
            card_type = value.find('comment').text
        else:
            card_type = value.find('card_type').text
        elapsed = int(value.find('elapsed').text)

        if card_type == 'y':
            card_score = 10
            if elapsed <= 45:
                if team_id == home_team_id:
                    home_yellow_before_half += 1
                elif team_id == away_team_id:
                    away_yellow_before_half += 1
                total_yellow_before_half += 1
            else:
                if team_id == home_team_id:
                    home_yellow_after_half += 1
                elif team_id == away_team_id:
                    away_yellow_after_half += 1
                total_yellow_after_half += 1
        elif card_type == 'r':
            card_score = 25
            if elapsed <= 45:
                if team_id == home_team_id:
                    home_red_before_half += 1
                elif team_id == away_team_id:
                    away_red_before_half += 1
                total_red_before_half += 1
            else:
                if team_id == home_team_id:
                    home_red_after_half += 1
                elif team_id == away_team_id:
                    away_red_after_half += 1
                total_red_after_half += 1

        if team_id == home_team_id:
            home_card_score += card_score
        elif team_id == away_team_id:
            away_card_score += card_score

    return home_yellow_before_half, home_yellow_after_half, away_yellow_before_half, away_yellow_after_half, total_yellow_before_half, total_yellow_after_half, home_red_before_half, home_red_after_half, away_red_before_half, away_red_after_half, total_red_before_half, total_red_after_half, home_card_score, away_card_score, card_score
