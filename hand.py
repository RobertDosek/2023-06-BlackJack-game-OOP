# from card import values
# from card import Card
import card
from deck import Deck


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.values[card.rank]

        # track aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        pass