from card import Card
from card import suits
from card import ranks
from random import shuffle


class Deck:
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card