import requests
from player import Player


class PlayerReader:
    def __init__(self, url):
        response = requests.get(url).json()

        self.players = []

        for player_dict in response:
            self.players.append(Player(player_dict))

    def get_players(self):
        return self.players
