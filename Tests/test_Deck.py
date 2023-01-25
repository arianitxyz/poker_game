import unittest
import random
import poker


class TestDeck(unittest.TestCase):
    def test_create_deck_size(self):
        deck = poker.Deck()
        self.assertEqual(len(deck.deck), 52)

    def test_create_deck_suits(self):
        deck = poker.Deck()
        deck.create_deck()
        suits = [card[1] for card in deck.deck]
        for suit in deck.suits:
            self.assertIn(suit, suits)

    def test_create_deck_ranks(self):
        deck = poker.Deck()
        deck.create_deck()
        ranks = [card[0] for card in deck.deck]
        for rank in deck.ranks:
            self.assertIn(rank, ranks)

    def test_get_hand(self):
        deck = poker.Deck()
        deck.create_deck()
        hand = deck.get_hand()
        self.assertEqual(len(hand), 5)
