from unittest import TestCase, main

from project.card.trap_card import TrapCard


class TestTrapCard(TestCase):
    def setUp(self):
        self.trap_card = TrapCard('Test1')

    def test_attributes_are_set(self):
        self.assertEqual('Test1', self.trap_card.name)
        self.assertEqual(120, self.trap_card.damage_points)
        self.assertEqual(5, self.trap_card.health_points)

    def test_set_card_name_with_empty_string__raises(self):
        with self.assertRaises(ValueError) as ex:
            self.trap_card.name(card=TrapCard(''))
        self.assertEqual("Card's name cannot be an empty string.", str(ex.exception))

    def test_check_class_name(self):
        self.assertEqual("TrapCard", self.trap_card.__class__.__name__)


if __name__ == '__main__':
    main()