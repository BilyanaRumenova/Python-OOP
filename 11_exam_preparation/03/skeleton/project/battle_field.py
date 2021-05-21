from project.player.player import Player


class BattleField:

    def fight(self, attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        if self.is_beginner(attacker):
            attacker.beginner_upgrade()
        if self.is_beginner(enemy):
            enemy.beginner_upgrade()

        # attacker.health += sum([card.health_points for card in attacker.card_repository.cards])
        # enemy.health += sum([card.health_points for card in enemy.card_repository.cards])
        attacker.health += self.get_bonus_health_points(attacker)
        enemy.health += self.get_bonus_health_points(enemy)

        for card in attacker.card_repository.cards:
            enemy.take_damage(card.damage_points)
            if enemy.is_dead:
                return

        for card in enemy.card_repository.cards:
            if attacker.is_dead or enemy.is_dead:
                return
            attacker.take_damage(card.damage_points)

    @staticmethod
    def is_beginner(player):
        return player.__class__.__name__ == "Beginner"

    @staticmethod
    def get_bonus_health_points(player):
        bonus_health_points = 0
        for card in player.card_repository.cards:
            bonus_health_points += card.health_points
        return bonus_health_points





