from unittest import TestCase, main

from project.card.magic_card import MagicCard


class TestTrapCard(TestCase):
    def setUp(self):
        self.magic_card = MagicCard('Test2')

    def test_attributes_are_set(self):
        self.assertEqual('Test1', self.magic_card.name)
        self.assertEqual(5, self.magic_card.damage_points)
        self.assertEqual(80, self.magic_card.health_points)

    def test_set_card_name_with_empty_string__raises(self):
        with self.assertRaises(ValueError) as ex:
            self.magic_card.name(card=MagicCard(''))
        self.assertEqual("Card's name cannot be an empty string.", str(ex.exception))

    def test_check_class_name(self):
        self.assertEqual("MagicCard", self.magic_card.__class__.__name__)


if __name__ == '__main__':
    main()