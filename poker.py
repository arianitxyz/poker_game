from collections import defaultdict
from random import shuffle


class Deck(object):
    def __init__(self):
        # self.suits = ['spade', 'heart', 'diamond', 'club']
        self.suits = ['S', 'H', 'D', 'C']
        self.ranks = range(2, 15)
        deck = [str(r) + s for r in self.ranks for s in self.suits]
        shuffle(deck)
        self.deck = deck
        self.hand = []

    def get_card(self):
        return self.deck.pop()

    def get_n_cards(self, n):
        return (self.get_card() for i in range(n))


class Hand(object):

    def __init__(self):
        self.hand = Deck.get_n_cards(5)

    def check_straight_flush(self):
        if self.check_flush(self.hand) and self.check_straight(self.hand):
            return True
        else:
            return False

    card_order_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12,
                       "K": 13,
                       "A": 14}

    def check_four_of_a_kind(self):
        values = [i[0] for i in self.hand]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        if sorted(value_counts.values()) == [1, 4]:
            return True
        return False

    def check_full_house(self):
        values = [i[0] for i in self.hand]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        if sorted(value_counts.values()) == [2, 3]:
            return True
        return False

    def check_flush(self):
        suits = [i[1] for i in self.hand]
        if len(set(suits)) == 1:
            return True
        else:
            return False

    def check_straight(self):
        values = [i[0] for i in self.hand]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        rank_values = [self.card_order_dict[i] for i in values]
        value_range = max(rank_values) - min(rank_values)
        if len(set(value_counts.values())) == 1 and (value_range == 4):
            return True
        else:
            # check straight with low Ace
            if set(values) == set(["A", "2", "3", "4", "5"]):
                return True
            return False

    def check_three_of_a_kind(self):
        values = [i[0] for i in self.hand]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        if set(value_counts.values()) == set([3, 1]):
            return True
        else:
            return False

    def check_two_pair(self):
        values = [i[0] for i in self.hand]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        if sorted(value_counts.values()) == [1, 2, 2]:
            return True
        else:
            return False

    def check_pair(self):
        values = [i[0] for i in self.hand]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        if 2 in value_counts.values():
            return True
        else:
            return False

    def check_high_card(hand):
        pass

    def check_straight(hand):
        pass

    def check_hand(self):
        if self.check_straight():
            return 10
        if self.check_flush():
            return 9
        if self.check_four_of_a_kind():
            return 8
        if self.check_full_house():
            return 7
        if self.check_flush():
            return 6
        if self.check_straight():
            return 5
        if self.check_three_of_a_kind():
            return 4
        if self.check_two_pair():
            return 3
        if self.check_pair():
            return 2
        if self.check_high_card():
            return 1


hand = Hand.check_hand(Deck.get_n_cards('test', 5))
print(hand)
