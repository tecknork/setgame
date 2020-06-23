import random
from .card import Card
from typing import List


class Deck:
    def __init__(self, n: int = 12):
        self.cards = []
        for number in range(1, n + 1):
            id = random.randint(1, 81)
            card = Card.objects.get(id=id)
            self.cards.append(card)

    def print_deck(self):
        """
      create a function which prints all cards in the deck
      :return:
      """
        for card in self.cards:
            print(card)

    def check_card(self, card_ids: List[int]):
        """
        get 3 card ids find those cards in your list or from datbase
        and then verify those cards
        :param card_ids:
        :return:
        """
        for card_id in card_ids:
            print(card_id)
        return False
