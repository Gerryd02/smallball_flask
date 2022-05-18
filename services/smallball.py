import statsapi as sa
import json

import pandas as pd
import os


# def league_leaders():
#     league_leaders_categories = statsapi.meta('leagueLeaderTypes')
#     for i in league_leaders_categories:
#         for k, v in i.items():
#             print(v)
#             print(statsapi.league_leaders(v, season=2022, limit=5))
def main():
    team_info = sa.get("teams", {"sportID": 1})['teams']
    with open('../data/teams.json', 'w') as teams_data:
        json.dump(team_info, teams_data, indent=5)

if __name__ == '__main__':
    main()



