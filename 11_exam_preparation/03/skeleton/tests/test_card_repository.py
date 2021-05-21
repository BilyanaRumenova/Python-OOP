from unittest import TestCase, main

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(TestCase):

    def setUp(self):
        self.card_repository = CardRepository()
        self.card_repository.cards = ['a', 'b', 'c']
        self.card_repository.count = 3

    def test_check_attributes_are_set(self):
        self.assertEqual(3, self.card_repository.count)
        self.assertListEqual(['a', 'b', 'c'], self.card_repository.cards)
        self.assertIn('a', self.card_repository.cards)

    def test_add_existing_card__raises(self):
        card = MagicCard('a')
        with self.assertRaises(ValueError) as ex:
            self.card_repository.add(card)
        self.assertEqual(f"Card {card.name} already exists!", str(ex.exception))







if __name__ == '__main__':
    main()