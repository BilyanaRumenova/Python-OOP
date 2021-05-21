from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        try:
            card_to_add = [c for c in self.cards if c.name == card.name][0]
            raise ValueError(f"Card {card_to_add.name} already exists!")
        except IndexError:
            self.count += 1
            self.cards.append(card)

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        card_to_remove = [c for c in self.cards if c.name == card][0]
        self.cards.remove(card_to_remove)
        self.count -= 1

    def find(self, name: str):
        card = [card for card in self.cards if card.name == name][0]
        return card