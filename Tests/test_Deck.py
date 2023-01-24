import unittest
import random
import poker


class TestDeck(unittest.TestCase):
    def test_create_deck(self):
        deck = poker.Deck()
        self.assertEqual(len(deck.deck), 52)
        # self.assertEqual(deck.deck[0], (2, 'spade'))
