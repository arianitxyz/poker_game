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


def check_straight_flush(hand):
    if check_flush(hand) and check_straight(hand):
        return True
    else:
        return False


card_order_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13,
                   "A": 14}


def check_four_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1, 4]:
        return True
    return False


def check_full_house(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [2, 3]:
        return True
    return False


def check_flush(hand):
    suits = [i[1] for i in hand]
    if len(set(suits)) == 1:
        return True
    else:
        return False


def check_straight(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    rank_values = [card_order_dict[i] for i in values]
    value_range = max(rank_values) - min(rank_values)
    if len(set(value_counts.values())) == 1 and (value_range == 4):
        return True
    else:
        # check straight with low Ace
        if set(values) == set(["A", "2", "3", "4", "5"]):
            return True
        return False


def check_three_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if set(value_counts.values()) == set([3, 1]):
        return True
    else:
        return False


def check_two_pair(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1, 2, 2]:
        return True
    else:
        return False


def check_pair(hand):
    values = [i[0] for i in hand]
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


class Hand(object):
    def __init__(self):
        self.result = ''

    def check_hand(self, hand):
        if check_straight(hand):
            return 10
        if check_flush(hand):
            return 9
        if check_four_of_a_kind(hand):
            return 8
        if check_full_house(hand):
            return 7
        if check_flush(hand):
            return 6
        if check_straight(hand):
            return 5
        if check_three_of_a_kind(hand):
            return 4
        if check_two_pair(hand):
            return 3
        if check_pair(hand):
            return 2
        if check_high_card(hand):
            return 1
