import card
from random import shuffle


class Deck():
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in card.suits:
            for rank in card.ranks:
                self.deck.append(card.Card(suit, rank))

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for cd in self.deck:
            deck_comp += '\n '+cd.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        shuffle(self.deck)

    def deal(self):
        return self.deck.pop()