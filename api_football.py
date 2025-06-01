
import requests
from config import API_FOOTBALL_KEY

def get_match_info(team_id):
    url = "https://v3.football.api-sports.io/fixtures"
    headers = {
        "x-apisports-key": API_FOOTBALL_KEY
    }
    params = {
        "team": team_id,
        "next": 1
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()
