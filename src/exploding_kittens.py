import random
from card_definitions import get_card_definition, EXPLODINGKITTEN_CARD_TYPE, get_card_name

card_deck = []

player_hands = []

active_players = []


def print_cards(cards):
    card_defs = [str(get_card_definition(card)["type"]) for card in cards]
    return ", ".join(card_defs)


def create_deck():
    global card_deck
    print "Creating Deck"
    card_deck = range(51)
    print "Original Deck = %s" % card_deck
    print "Deck = %s" % print_cards(card_deck)


def shuffle_deck(deck):
    # TODO shuffle
    print "Shuffling Deck"
    random.shuffle(deck)


def insert_card_into_deck(deck, location=None):
    if location is None:
        # Randomally assign index
        location = random.randint(0, len(deck))

    assert isinstance(deck, list)
    deck.insert(location, deck)

    return deck


def deal():
    print "Dealing..."  
    CARDS_PER_PLAYER = 4
    # TODO deal cards to players
    global player_hands
    global active_players

    player_hands = []
    player_hands.append([])
    player_hands.append([])
    active_players = range(2)

    for x in range(CARDS_PER_PLAYER):
        for player_id in range(2):
            player_hand = player_hands[player_id]
            current_card = None
            while current_card is None:
                current_card = draw_card(card_deck)
                if get_card_definition(current_card)["type"] == EXPLODINGKITTEN_CARD_TYPE:
                    # Need to redraw as we can't have this
                    insert_card_into_deck(card_deck)
                    current_card = None

            player_hand.append(current_card)


def start_new_game():
    create_deck()
    shuffle_deck(card_deck)
    print "Shuffled Deck = %s" % print_cards(card_deck)
    deal()
    for x in range(2):
        print "Player %d hand: %s" % (x, print_cards(player_hands[x]))


def is_game_over():
    if not card_deck:
        print "No more cards"
        return True
    if len(active_players) <= 1:
        print "Only one player left"
        return True
    return False


def draw_card(deck=None):
    if deck is None:
        deck = card_deck

    return deck.pop(0)


def main():
    start_new_game()

    NUMBER_OF_PLAYERS = 2
    active_player_idx = 0

    while not is_game_over():
        current_player_id = active_players[active_player_idx]
        print "Current player is %s" % current_player_id
        current_card = draw_card(card_deck)
        print "Drew card = %s" % get_card_name(current_card)
        if get_card_definition(current_card)["type"] == EXPLODINGKITTEN_CARD_TYPE:
            print "Player got exploding kitten"
            active_players.pop(active_player_idx)
            # Dont increment the active_player_idx since we just removed one from the list
        else:
            active_player_idx += 1

        if active_player_idx >= len(active_players):
            active_player_idx = 0

    # TODO who won?
    print "Game Over"

if __name__ == "__main__":
    main()

