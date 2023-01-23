suits = ['spade', 'heart', 'diamond', 'club']
cards = ['1', '2', '3', '4', '5', '6', '7', '10', 'J', 'Q', 'K', 'ACE']

deck = set()
for suit in suits:
    for card in cards:
        deck.add((card, suit))


class Player:
    def __init__(self, player_name, budget, hand):
        self.player_name = player_name
        self.budget = budget
        self.hand = hand


current_deck = []
for card_set in deck:
    current_deck.append(card_set)

print(current_deck)


def get_hand():
    player_hand = []
    for count in range(5):
        test = current_deck.pop()
        player_hand.append(test)
    print(player_hand)


get_hand()
get_hand()
get_hand()
get_hand()
get_hand()
get_hand()
get_hand()
get_hand()
get_hand()

print(current_deck)
