from hand import Hand
from deck import Deck


game_on = True
test_deck = Deck()
test_deck.shuffle()
# print(test_deck)

test_player = Hand()
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)

