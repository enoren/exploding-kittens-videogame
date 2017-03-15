UNKNOWN_CARD_TYPE = 0
NOPE_CARD_TYPE = 2
DIFFUSE_CARD_TYPE = 1
SHUFFLE_CARD_TYPE = 3
FAVOR_CARD_TYPE = 4
SKIP_CARD_TYPE = 5
ATTACK_CARD_TYPE = 6
SEETHEFUTURE_CARD_TYPE = 7
EXPLODINGKITTEN_CARD_TYPE = 8
PAIR_CARD_TYPE = 9
TACOCAT_CARD_SUBTYPE = 10
BEARDCAT_CARD_SUBTYPE = 11
CATTERMELON_CARD_SUBTYPE = 12
HAIRYPOTATOECAT_CARD_SUBTYPE = 13
RAINBOWRALPHINGCAT_CARD_SUBTYPE = 14
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
    },{ #9
        "type": DIFFUSE_CARD_TYPE
    },{
        #10
        "type": DIFFUSE_CARD_TYPE
    },{
        #11
        "type": DIFFUSE_CARD_TYPE
    },{
        #12
        "type": DIFFUSE_CARD_TYPE
    },{
        #13
        "type": SKIP_CARD_TYPE
    },{
        #14
        "type": SKIP_CARD_TYPE
    },{
        #15

        "type": SKIP_CARD_TYPE
    },{
        #16
        "type": SKIP_CARD_TYPE
    },{   #17

        "type": ATTACK_CARD_TYPE
    },{
        #18

        "type": ATTACK_CARD_TYPE
    },{
        #19
        "type": ATTACK_CARD_TYPE
    },{
        #20
        "type": ATTACK_CARD_TYPE
    },{
        #21
        "type": FAVOR_CARD_TYPE
    },{
        #22
        "type": FAVOR_CARD_TYPE
    },{
        #23
        "type": FAVOR_CARD_TYPE
    },{
        #24
        "type": FAVOR_CARD_TYPE
    },{
        #25
        "type": SEETHEFUTURE_CARD_TYPE
    },{
        #26
        "type": SEETHEFUTURE_CARD_TYPE
    },{
        #27
        "type": SEETHEFUTURE_CARD_TYPE
    },{
        #28
        "type": SEETHEFUTURE_CARD_TYPE
    },{
        #29
        "type": SEETHEFUTURE_CARD_TYPE
    },{
        #30
        "type" : PAIR_CARD_TYPE,
        "subtype": TACOCAT_CARD_SUBTYPE
    },{
        #31
        "type": PAIR_CARD_TYPE,
        "subtype": TACOCAT_CARD_SUBTYPE
    },{
        #32
        "type": PAIR_CARD_TYPE,
        "subtype": TACOCAT_CARD_SUBTYPE
    },{
        #33
        "type": PAIR_CARD_TYPE,
        "subtype": TACOCAT_CARD_SUBTYPE
    },{
        #34
        "type": PAIR_CARD_TYPE,
        "subtype": CATTERMELON_CARD_SUBTYPE
    },{
        #35
        "type": PAIR_CARD_TYPE,
        "subtype": CATTERMELON_CARD_SUBTYPE
    },{
        #36
        "type": PAIR_CARD_TYPE,
        "subtype": CATTERMELON_CARD_SUBTYPE
    },{
        #37
        "type": PAIR_CARD_TYPE,
        "subtype": CATTERMELON_CARD_SUBTYPE
    },{
        #38
        "type": PAIR_CARD_TYPE,
        "subtype": BEARDCAT_CARD_SUBTYPE
    },{
        #39
        "type": PAIR_CARD_TYPE,
        "subtype": BEARDCAT_CARD_SUBTYPE
    },{
        #40
        "type": PAIR_CARD_TYPE,
        "subtype": BEARDCAT_CARD_SUBTYPE
    },{
        #41
        "type": PAIR_CARD_TYPE,
        "subtype": BEARDCAT_CARD_SUBTYPE
    },{
        #42
        "type": PAIR_CARD_TYPE,
        "subtype": HAIRYPOTATOECAT_CARD_SUBTYPE
    },{
        #43
        "type": PAIR_CARD_TYPE,
        "subtype": HAIRYPOTATOECAT_CARD_SUBTYPE
    },{
        #44
        "type": PAIR_CARD_TYPE,
        "subtype": HAIRYPOTATOECAT_CARD_SUBTYPE
    },{ #45
        "type": PAIR_CARD_TYPE,
        "subtype": HAIRYPOTATOECAT_CARD_SUBTYPE
    },{
        #46
        "type": PAIR_CARD_TYPE,
        "subtype": RAINBOWRALPHINGCAT_CARD_SUBTYPE
    },{
        #47
        "type": PAIR_CARD_TYPE,
        "subtype": RAINBOWRALPHINGCAT_CARD_SUBTYPE
    },{
        #48
        "type": PAIR_CARD_TYPE,
        "subtype": RAINBOWRALPHINGCAT_CARD_SUBTYPE
    },{
        #49
        "type": PAIR_CARD_TYPE,
        "subtype": RAINBOWRALPHINGCAT_CARD_SUBTYPE
    },{ #50
        "type": EXPLODINGKITTEN_CARD_TYPE
    }
]

type_to_text = {
    EXPLODINGKITTEN_CARD_TYPE: "Exploding Kitten",
    PAIR_CARD_TYPE: "Pair",
    SKIP_CARD_TYPE: "Skip",
    NOPE_CARD_TYPE: "Nope",
    DIFFUSE_CARD_TYPE: "Diffuse",
    SHUFFLE_CARD_TYPE: "Shuffle",
    UNKNOWN_CARD_TYPE: "Unknown",
    ATTACK_CARD_TYPE: "Attack",
    FAVOR_CARD_TYPE: "Favor",
    SEETHEFUTURE_CARD_TYPE: "See The Future"
}

type_to_keymap = {
    EXPLODINGKITTEN_CARD_TYPE: {
        "text": "<E>xploding Kitten",
        "key": "e"
    },
    PAIR_CARD_TYPE: {
        "text": "<P>air",
        "key": "p"
    },
    SKIP_CARD_TYPE: {
        "text": "<S>kip",
        "key": "s"
    },
    NOPE_CARD_TYPE: {
        "text": "<N>ope",
        "key": "n"
    },
    DIFFUSE_CARD_TYPE: {
        "text": "<D>iffuse",
        "key": "d"
    },
    SHUFFLE_CARD_TYPE: {
        "text": "S<h>uffle",
        "key": "h"
    },
    UNKNOWN_CARD_TYPE: None,
    ATTACK_CARD_TYPE: {
        "text": "<A>ttack",
        "key": "a"
    },
    FAVOR_CARD_TYPE: {
        "text": "Fa<v>or",
        "key": "v"
    },
    SEETHEFUTURE_CARD_TYPE: {
        "text": "See The <F>uture",
        "key": "f"
    }
}


KEYMAP_TO_TYPE = {type_def["key"]: card_type for card_type, type_def in type_to_keymap.items() if type_def}

def get_card_definition(card_id):
    try:
        return card_defs[card_id]
    except:
        return UNKNOWN_CARD_DEFINITION


def get_card_name(card_id):
    card_def = get_card_definition(card_id)
    return type_to_text[card_def["type"]]

def get_type_from_key(key):
    try:
        return KEYMAP_TO_TYPE[key]
    except KeyError:
        return UNKNOWN_CARD_TYPE

def get_card_name_prompt(card_id):
    card_def = get_card_definition(card_id)
    return type_to_keymap[card_def["type"]]["text"]
