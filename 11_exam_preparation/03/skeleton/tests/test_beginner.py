from unittest import TestCase, main

from project.player.beginner import Beginner


class TestBeginner(TestCase):

    def setUp(self):
        self.beginner_player = Beginner('User2')

    def test_attributes_are_set(self):
        self.assertEqual('User2', self.beginner_player.username)
        self.assertEqual(50, self.beginner_player.health)

    def test_set_username_with_empty_string__raises(self):
        with self.assertRaises(ValueError) as ex:
            self.beginner_player.username(player=Beginner(""))
        self.assertEqual("Player's username cannot be an empty string.", str(ex.exception))

    def test_set_username(self):
        player_2 = Beginner("Bil")
        self.assertEqual("Bil", player_2.username)

    def test_check_class_name(self):
        self.assertEqual("Beginner", self.beginner_player.__class__.__name__)


if __name__ == '__main__':
    main()
