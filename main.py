from time import time
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

from model_evaluation import split_match_data, get_model_metrics, get_scores, plot_scores
from process_data import getData, add_outcome, add_overall_rating, add_goals, add_cards, add_shots

models = [
    RandomForestClassifier(),
    GradientBoostingClassifier(),
    LogisticRegression(),
    SVC(),
    LinearSVC(),
    NuSVC(),
    KNeighborsClassifier(n_neighbors=22),
]

list_of_features = [
    'home_goals_before_half', 'away_goals_before_half',
    'total_goals_before_half', 'card_score', 'home_shoton_before_half', 'away_shoton_before_half',
]
target_variable = 'home_status'


def main():
    start = time()
    player_data, player_stats_data, team_data, match_data = getData()
    match_data = add_outcome(match_data)
    print(match_data.head())
    match_data = add_goals(match_data)
    match_data = add_cards(match_data)
    match_data = add_shots(match_data)
    match_data = add_overall_rating(match_data, player_stats_data)
    X_train, X_test, y_train, y_test = split_match_data(match_data, list_of_features, target_variable)
    metrics_df = get_model_metrics(models, X_train, X_test, y_train, y_test)
    get_scores(metrics_df)
    plot_scores(metrics_df)
    end = time()
    print(f"Time taken: {end - start} seconds")


if __name__ == "__main__":
    main()
