from unittest import TestCase, main

from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(TestCase):
    username_1 = 'at'
    health_1 = 0
    username_2 = 'enemy'
    health_2 = 50

    def test_fight__check_if_player_is_dead__raises(self):
        self.attacker = Advanced(self.username_1)
        with self.assertRaises(ValueError) as ex:
            self.attacker.health = 0
        self.assertEqual("Player is dead!", str(ex.exception))



    def test_attributes_are_set(self):
        pass






if __name__ == '__main__':
    main()