import random
import logging
from art import logo, faces

logging.basicConfig(level = logging.DEBUG)


def new_deck( number_of_packs ):
    cards = []
    for x in range(52 * number_of_packs):
        cards.append(x)

    random.shuffle(cards)

    return cards


def display( cards ):
    display = ""

    for y in range(6):
        for card in cards:
            display += faces[card].split('\n')[y] + ' '
        display += '\n'

    return display


def remaining_cards():
    return len(deck)


def hand_total( hand ):
    hand_total = 0

    for x in hand:
        card_value = x % 13 + 1
        if card_value > 10:
            card_value = 10

        hand_total += card_value

    return hand_total


def show_table( dealers_hand, players_hand ):
    global end_of_game
    player_total = hand_total(players_hand)
    dealer_total = hand_total(dealers_hand)
    hidden_hand = dealers_hand.copy()
    hidden_hand.append(card_back)

    print(f"dealer's hand ({dealer_total})")
    print(display(hidden_hand))
    print(f"your hand ({player_total})")
    print(display(players_hand))

    if player_total > 21:
        print(f"({player_total}) you went BUST, dealer WINS. :(\n")
        end_of_game = True
    elif dealer_total > 21:
        print(f"({dealer_total}) dealer went BUST, you WIN :)\n")
        end_of_game = True
    elif dealer_total > player_total and dealer_total < 22 and end_of_game:
        print(f"({dealer_total}) dealer WINS.\n")
        end_of_game = True
    elif dealer_total < player_total and player_total < 22 and end_of_game:
        print(f"({player_total}) player WINS.\n")
        end_of_game = True
    elif dealer_total == player_total and end_of_game:
        print(f"({dealer_total}-{player_total}) its a draw.")
        end_of_game = True
    elif player_total == 21:
        print(f"({player_total}) B L A C K J A C K, you WIN :)\n")
        end_of_game = True
    elif dealer_total == 21:
        print(f"({dealer_total}) B L A C K J A C K, dealer WINS :)\n")
        end_of_game = True

    if end_of_game:
        print(f"{remaining_cards()} cards remaining.\n")
        instruction = input("(n)ew or (q)uit?\n  > ").lower()
    else:
        print(f"{remaining_cards()} cards remaining.\n")
        instruction = input("(s)tick, (h)it, (n)ew or (q)uit?\n  > ").lower()

    return instruction


def dealer_turn( dealers_hand ):
    global end_of_game
    dealer_total = hand_total(dealers_hand)
    while dealer_total < 17:
        dealers_hand.append(deck.pop())
        dealer_total = hand_total(dealers_hand)

    end_of_game = True
    return dealers_hand


def deal_card( hand, number = 1 ):
    if remaining_cards() < 1:
        new_deck(number_of_packs)

    for x in range(number):
        hand.append(deck.pop())

    return hand


def main():
    global end_of_game
    end_of_game = False

    print(logo)
    dealers_hand = deal_card([], 1)
    players_hand = deal_card([], 2)

    while True:
        instruction = show_table(dealers_hand, players_hand)

        if instruction == 'h':
            players_hand.append(deck.pop())
        if instruction == 's':
            dealers_hand = dealer_turn(dealers_hand)
        if instruction == 'n':
            main()
        elif instruction == 'q':
            exit(0)


end_of_game = False
number_of_packs = 1
deck = new_deck(number_of_packs)
card_back = 52

if __name__ == '__main__':
    main()
