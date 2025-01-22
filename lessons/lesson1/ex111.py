import requests
from pprint import pprint

url = "https://gist.githubusercontent.com/nonZero/b86339d7d97417fff297/raw/e30f0a6b3e62f7707240e03893379f0c97f5b2e9/worldcup.json"

res = requests.get(url)

for game in res.json():
    home_team = game["home_team"]["country"]
    away_team = game["away_team"]["country"]
    home_goals = game["home_team"]["goals"]
    away_goals = game["away_team"]["goals"]
    print(f"{home_team} - {away_team}: {home_goals}-{away_goals}")
