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

def get_card_definition(card_id):
    try:
        return card_defs[card_id]
    except:
        return UNKNOWN_CARD_DEFINITION
