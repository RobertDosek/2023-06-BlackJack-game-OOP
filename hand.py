from card import values


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, cd):
        self.cards.append(cd)
        self.value += values[cd.rank]

        # track aces
        if cd.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # if total value > and I still have an ace then change my ace to 1 instead of 11
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces += 1