from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        try:
            player_to_add = [p for p in self.players if p.username == player.username][0]
            raise ValueError(f"Player {player_to_add.username} already exists!")
        except IndexError:
            self.players.append(player)
            self.count += 1

    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        player_to_remove = [p for p in self.players if p.username == player][0]
        self.players.remove(player_to_remove)
        self.count -= 1

    def find(self, username: str):
        return [player for player in self.players if player.username == username][0]
