import unittest
import random
import poker
from poker import Deck


class TestDeck(unittest.TestCase):

    def setUp(self) -> None:
        self.deck = Deck()

    def test_get_card(self):
        # def get_card(self):
        #     return self.deck.pop()
        test = self.deck.get_card()
        self.assertIsNot(self.deck.get_card(), None)
        # self.assertIsNot(len(self.deck) None)

    # def test_get_n_cards(self):

# def test_create_deck_size(self):
#
#     self.assertEqual(len(self.deck), 52)
#
# def test_create_deck_suits(self):
#     deck = poker.Deck()
#     deck.create_deck()
#     suits = [card[1] for card in deck.deck]
#     for suit in deck.suits:
#         self.assertIn(suit, suits)
#
# def test_create_deck_ranks(self):
#     deck = poker.Deck()
#     deck.create_deck()
#     ranks = [card[0] for card in deck.deck]
#     for rank in deck.ranks:
#         self.assertIn(rank, ranks)
#
# # def test_get_hand(self):
# #     deck = poker.Deck()
# #     deck.create_deck()
# #     hand = deck.get_hand()
# #     self.assertEqual(len(hand), 5)
#
# def get_card(self):
#     return self.deck.pop()
#
# def get_n_cards(self, n):
#     return (self.get_card() for i in range(n))
#
# def test_get_card(self):
#     deck = poker.Deck()
