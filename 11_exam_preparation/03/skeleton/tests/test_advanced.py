from unittest import TestCase, main

from project.player.advanced import Advanced


class TestAdvanced(TestCase):

    def setUp(self):
        self.advanced_player = Advanced('User1')

    def test_attributes_are_set(self):
        self.assertEqual('User1', self.advanced_player.username)
        self.assertEqual(250, self.advanced_player.health)

    def test_set_username_with_empty_string__raises(self):
        with self.assertRaises(ValueError) as ex:
            self.advanced_player.username(player=Advanced(""))
        self.assertEqual("Player's username cannot be an empty string.", str(ex.exception))

    def test_check_class_name(self):
        self.assertEqual("Advanced", self.advanced_player.__class__.__name__)


if __name__ == '__main__':
    main()
