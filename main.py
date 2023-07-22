from hand import Hand
from deck import Deck
from card import Card
from chips import Chips

playing = True


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips you want to bet?: "))
        except:
            print("Sorry, please, provide a number.")
        else:
            if chips.bet > chips.total:
                print(f"You do not enough chips! You have: {chips.total} ")
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(dck, hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input("Hit or Stand? Enter h or s: ")
        if x[0].lower() == "h":
            hit(dck, hand)
        elif x[0].lower() == "s":
            print("Player stands, Dealers Turn")
            playing = False
        else:
            print("Sorry, I did not understand. Please provide h or s only! ")
            continue
        break


def show_some(player, dealer):

    # show only ONE of the dealers cards
    print("\nDealer's Hand:")
    print("First card hidden!")
    print(dealer.cards[1])

    # show all (2 cards) of the players cards
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    # show all the dealers cards
    print("\nDealer's Hand: ")
    for card in dealer.cards:
        print(card)

    # calculate and display value
    print(f"Value of dealers hand is: {dealer.value}")

    # show all players cards
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)

    # calculate and display value
    print(f"Value of players hand is: {player.value}")


def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")


while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    # Inform Player of their chips total
    print(f"\nPlayer total chips are at: {player_chips.total}")

    # Ask to play again
    new_game = input("Do you want to play another hand? y or n?\n")

    if new_game[0].lower() == "y":
        playing = True
        continue
    else:
        print("Thank you for playing!")
        break