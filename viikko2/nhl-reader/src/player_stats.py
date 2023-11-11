class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        returned_players = []
        for player in players:
            if player.nationality == nationality:
                returned_players.append(player)
        returned_players.sort(reverse=True)
        return returned_players
