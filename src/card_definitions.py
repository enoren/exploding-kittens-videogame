UNKNOWN_CARD_TYPE = 0
NOPE_CARD_TYPE = 2
DIFFUSE_CARD_TYPE = 1
SHUFFLE_CARD_TYPE = 3
FAVOR_CARD_TYPE = 4
SKIP_CARD_TYPE = 5
ATTACK_CARD_TYPE = 6
SEETHEFUTURE_CARD_TYPE = 7
EXPLODINGKITTEN_CARD_TYPE = 8

UNKNOWN_CARD_DEFINITION = {
    "type": UNKNOWN_CARD_TYPE
}

card_defs = [
    { # Card 0
        "type": NOPE_CARD_TYPE
    },{  # Card 1
        "type": NOPE_CARD_TYPE
    },{ # Card 2
        "type": NOPE_CARD_TYPE
    },{# Card 3
        "type": NOPE_CARD_TYPE
    },{ # Card 4
        "type": NOPE_CARD_TYPE
    },{
        # Card 5
        "type": SHUFFLE_CARD_TYPE
    },{
        # Card 6...
        "type": SHUFFLE_CARD_TYPE
    },{ #7
        "type": SHUFFLE_CARD_TYPE
    },{ #8
        "type": SHUFFLE_CARD_TYPE
    },{

    }
]

def get_card_definition(card_id):
    try:
        return card_defs[card_id]
    except:
        return UNKNOWN_CARD_DEFINITION
