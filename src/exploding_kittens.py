

card_deck = []

player1_hand = []
player2_hand = []

def create_deck():
    print "Creating Deck"
    card_deck = range(51)

def shuffle_deck():
    // TODO shuffle
    print "Shuffling Deck"
    pass

def deal():
    print "Dealing..."  
    CARDS_PER_PLAYER = 4
    // TODO deal cards to players

def start_new_game():
    create_deck()
    shuffle_deck()
    deal()

def is_game_over():
    return True

def draw_card():
    //TODO pull card from the top and return
    pass

def main():
    start_new_game()

    NUMBER_OF_PLAYERS = 2
    current_player = 0

    while not is_game_over():
        // TODO take turn 

    // TODO who won?
    print "Game Over"

if __name__ == "__main__":
    main()

