#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Class to compare two poker hands. 
# The PokerHand object is initialised with one argument which is the poker hand string.
# The compare_with() function takes the opponent's poker hand string. The function then loops over possible winning hands returning a score.
# The score will be greater depending on how rare the hand is, and also how high the rank of the winning card is.
# 
# Martin Rogers - martin.rog0404@gmail.com

from collections import Counter

face_cards = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

class PokerHand(object):

    def __init__(self, arg):
        self.hand=arg
        self.score=0
        self.op_score=0

    def to_number(self, card):
        if card[0].isnumeric():
              return int(card[0])
        else:
            return face_cards[card[0]]

    def only_ranks(self, hand):
        hand_list = hand.split()
        rank_list = []
        for card in hand_list:
            rank_list.append(self.to_number(card[0]))

        rank_list.sort(reverse=True)
        return rank_list
    
    #######################
    # Test for winning hand
    #######################


    def pair_score(self, hand):
        only_ranks = self.only_ranks(hand)
        score=0
        dup_count=[]
        duplicates = Counter(only_ranks)
        most_common = duplicates.most_common()
        # 
        for i in most_common:
            if i[1] == 2:            
                score = 100 + i[0]
        return score

    def high_card_score(self, hand):
        only_ranks = self.only_ranks(hand)
        score=0
        return max(only_ranks)


    def compare_with(self, op_hand_object):

        op_hand = op_hand_object.hand

        self.score=0
        self.op_score=0

        #Loop over all possible winning hands and return the scores
        hand_tests = [self.pair_score,
        self.high_card_score] 

        for test in hand_tests:     
            
            self.op_score+=test(op_hand)
            if self.op_score > 0:
                break
        #print(self.op_score)

        for test in hand_tests:
            self.score+=test(self.hand)
            if self.score > 0:
                break
        #print(self.score)

        
        if self.score > self.op_score:
            return 1
        elif self.score == self.op_score:
            return 0
        else:
            return 2



