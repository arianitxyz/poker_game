import random


class Deck:
    def __init__(self):
        self.suits = ['spade', 'heart', 'diamond', 'club']
        self.ranks = range(2, 15)
        self.deck = []
        self.create_deck()
        self.shuffle_deck()
        self.hand = []

    def create_deck(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append((rank, suit))
        return self.deck

    def shuffle_deck(self):
        self.deck = random.sample(self.deck, len(self.deck))
        print(self.deck)

        return self.deck

    def get_hand(self):
        self.hand = []
        for count in range(5):
            self.hand.append(self.deck[0])
            self.deck.remove(self.deck[0])
        return self.hand


my_deck = Deck()
for i in range(10):
    print()
    my_deck.get_hand()
    print(my_deck.hand)
    print(len(my_deck.deck))
