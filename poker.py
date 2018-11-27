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
    
    def royal_flush_score(self, hand):
        hand_list = hand.split()
        rank_total = sum(self.only_ranks(hand))
        hand_list = sorted(hand_list, key=self.to_number)
        score = 0

        # Check for a high ace and then if straight and flush is True
        if hand_list[-1][0] == 'A' and self.straight_score(hand) and self.flush_score(hand): 
            score = 900 + rank_total
        return score                                         

    def straight_flush_score(self, hand):
        hand_list = hand.split()
        rank_total = sum(self.only_ranks(hand))
        hand_list = sorted(hand_list, key=self.to_number)
        score = 0

        if hand_list[-1][0] != 'A' and self.straight_score(hand) and self.flush_score(hand):
            score = 800 + rank_total  
        return score


    def four_of_kind_score(self, hand):
        only_ranks = self.only_ranks(hand)
        score = 0
        dup_count=[]
        duplicates = Counter(only_ranks)
        most_common = duplicates.most_common()

        # Check if the Counter found four dulicate ranks
        for i in most_common:
            if i[1] == 4:            
                score = 700 + i[0]
        return score

    def full_house_score(self, hand):
        only_ranks = self.only_ranks(hand)
        score = 0
        dup_count=[]
        duplicates = Counter(only_ranks)
        most_common = duplicates.most_common()
        most_common.sort(reverse=True)

        # Check if the Counter found and 3 & 2 dulicate ranks
        if most_common[0][1] == 3 and most_common[1][1] == 2:            
                score = 600 + int(most_common[0][0]) + int(most_common[1][0])
        return score

    def flush_score(self, hand):
        hand_list = hand.split()
        rank_total = sum(self.only_ranks(hand))
        score = 0
        test_suit = hand_list[0][1]

        test = all(card[1] == test_suit for card in hand_list)
        if test : 
            score = 500 + rank_total
        return score


    def straight_score(self, hand):
        hand_list = hand.split()
        hand_list = sorted(hand_list, key=self.to_number)
        rank_total = sum(self.only_ranks(hand))
        score=0

        # Check for low ace
        if hand_list[-1][0] == "A" and hand_list[0][0] == "2":
            # Check that the remaining cards complete the straight
            test = list(map(self.to_number, hand_list[1:-1])) == list(range(3, len(hand_list)+1))
            if test:            
                score = 400 + rank_total
                return score
        else: 
            # Check if list of ranks is accending 1,2,3,4
            test = all(self.to_number(hand_list[i])+1 == self.to_number(hand_list[i+1]) for i in range(len(hand_list)-1))
            if test : score = 400 + rank_total
            return score


    def three_of_kind_score(self, hand):
        only_ranks = self.only_ranks(hand)
        score = 0
        dup_count=[]
        duplicates = Counter(only_ranks)
        most_common = duplicates.most_common()

        # Check if the Counter found 3 duplicates
        for i in most_common:
            if i[1] == 3:            
                score = 300 + i[0]

        return score

    def two_pair_score(self, hand):
        only_ranks = self.only_ranks(hand)
        score=0
        dup_count=0
        duplicates = Counter(only_ranks)
        most_common = duplicates.most_common()

        # Check for 2 duplicate rank
        for i in most_common:
            if i[1] == 2:            
                score += 100 + i[0]
        return score

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
        hand_tests = [self.royal_flush_score, 
        self.straight_flush_score, 
        self.four_of_kind_score,
        self.full_house_score,
        self.flush_score,
        self.straight_score,
        self.three_of_kind_score,
        self.two_pair_score,
        self.pair_score,
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



# hand = "TD TS QS QH TH"
# op_hand = "5D 5S QC 9H QH"


# game = PokerHand(hand)
# opponent = PokerHand(op_hand)
# print(game.compare_with(opponent))


# print(game.pair_score("KS KH 5C JD TD"))
# print(game.two_pair_score("KS KH 5C 5D TD"))
# print(game.three_of_kind_score("KS KH KC 5D TD"))
# print(game.straight_score("KS 9H QC JD TD"))
# print(game.flush_score("KS 9S QS JS TS"))
# print(game.full_house_score("KS KS KS JS JS"))
# print(game.four_of_kind_score("KS KH KC KD TD"))
# print(game.straight_flush_score("8S QS JS 9S TS"))
# print(game.royal_flush_score("KS AS QS JS TS"))


# print(game.pair_score("KS 8H 5C JD TD"))
# print(game.two_pair_score("9S 9H 5C 5D TD"))
# print(game.three_of_kind_score("KS 9H KC 5D TD"))
# print(game.straight_score("AS 2H 3C 4D 5D"))
# print(game.flush_score("KS 9S 9S JS 2C"))
# print(game.full_house_score("KS 6S 6S JS JS"))
# print(game.four_of_kind_score("KS KH QC KD TD"))
# print(game.straight_flush_score("8S QS 2S 9S TC"))
# print(game.royal_flush_score("KS AS QC JS TS"))
