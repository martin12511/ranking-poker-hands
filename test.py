#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from poker import PokerHand

class TestCase(unittest.TestCase):
    def test_higher_two_pair_wins(self):
        hand = PokerHand("TD 9S QS QH TH")
        opponent = PokerHand("5D 5S QC 9H QH")
        # Testing two pairs: True
        self.assertEqual(hand.compare_with(opponent), 1)

    def test_low_ace(self):
        # Testing low ace straight against 3 of kind: Win
        hand = PokerHand("AD 2S 3S 4H 5H")
        opponent = PokerHand("5D 5S 5C 9H QH")
        self.assertEqual(hand.compare_with(opponent), 1)

    def test_high_ace(self):
        # Testing high ace straight against 3 of kind: Win
        hand = PokerHand("AD AS AH 4H 5H")
        opponent = PokerHand("5D 5S 5C 9H QH")
        self.assertEqual(hand.compare_with(opponent), 1)

    def test_royal(self):
        # Testing royal flush and straight flush: Win
        hand = PokerHand("AD KD QD JD TD")
        opponent = PokerHand("3D 4D 5D 6D 7D")
        self.assertEqual(hand.compare_with(opponent), 1)

    def test_high_card(self):
        # Testing high card against pair: Lose
        hand = PokerHand("KD 3D QC 5D 6H")
        opponent = PokerHand("3D 4D 5D 5H 7D")
        self.assertEqual(hand.compare_with(opponent), 2)

    def test_tie(self):
        # Testing for a high card draw: Tie
        hand = PokerHand("KD 3D QC 5D 6H")
        opponent = PokerHand("KC 3D QH 5D 6D")
        self.assertEqual(hand.compare_with(opponent), 0)


if __name__ == '__main__':
    unittest.main()

