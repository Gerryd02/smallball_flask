import statsapi
import json


def team_lookup(team_name):
    team_info = statsapi.lookup_team(team_name)
    for k, v in team_info[0].items():
        print(f'{k}: {v}')


def load_teams_data():
    with open('../data/teams.json', 'r') as read_json:
        teams_data = read_json
    return read_json

teams_data = load_teams_data()

class Team:
    def __init__(self, team_id: int):
        self.team_id = team_id
        self.teams_data = teams_data


    def get_team_name(self):






class Player:
    def __init__(self, ):