import random
from card_definitions import get_card_definition, EXPLODINGKITTEN_CARD_TYPE, get_card_name, DIFFUSE_CARD_TYPE

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


def insert_card_into_deck(deck, card_id, location=None):
    if location is None:
        # Randomally assign index
        location = random.randint(0, len(deck))

    assert isinstance(deck, list)
    deck.insert(location, card_id)

    return deck


def pop_first_from_deck(deck, card_type):
    for idx in range(len(deck)):
        card_id = deck[idx]
        cardtype = get_card_definition(card_id)["type"]
        if cardtype == card_type:
            return deck.pop(idx), idx
    raise IndexError("Card of type %s not found in deck" % str(card_type))


def deal():
    print "Dealing..."
    NUMBER_OF_PLAYERS = 2
    CARDS_PER_PLAYER = 3
    global player_hands
    global active_players

    player_hands = []
    player_hands.append([])
    player_hands.append([])
    active_players = range(NUMBER_OF_PLAYERS)

    for x in range(CARDS_PER_PLAYER):
        for player_id in range(NUMBER_OF_PLAYERS):
            player_hand = player_hands[player_id]
            current_card = None
            while current_card is None:
                current_card = draw_card(card_deck)
                if get_card_definition(current_card)["type"] == EXPLODINGKITTEN_CARD_TYPE:
                    # Need to redraw as we can't have this
                    insert_card_into_deck(card_deck, current_card)
                    current_card = None

            player_hand.append(current_card)

    # All players need to start out with a diffuse
    for player_id in range(NUMBER_OF_PLAYERS):
        player_hand = player_hands[player_id]
        card_id, _ = pop_first_from_deck(card_deck, DIFFUSE_CARD_TYPE)
        player_hand.append(card_id)



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
        currentplayerhand = player_hands[current_player_id]
        print "Drew card = %s" % get_card_name(current_card)
        if get_card_definition(current_card)["type"] == EXPLODINGKITTEN_CARD_TYPE:
            print "Player got exploding kitten!"
            try:
                card_id, card_idx = pop_first_from_deck(currentplayerhand, DIFFUSE_CARD_TYPE)
                active_player_idx += 1
                print "the exploding kitten was nullified!"
                insert_card_into_deck(card_deck, current_card)
            except IndexError:
                print "No diffuse card, so player exploded"
                active_players.pop(active_player_idx)
        else:
            currentplayerhand.append(current_card)
            active_player_idx += 1

        if active_player_idx >= len(active_players):
            active_player_idx = 0

    # TODO who won?
    print "Game Over - Player %s is the winner" % str(active_players[0])

if __name__ == "__main__":
    main()

