import random
import string
import math
from math import isclose

vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

print(list(zip(sorted(suits * len(vals)), vals * len(suits))))

# print(list(map(lambda x,y :sorted(x*len(y)),suits,vals),y*len(x)),suits,vals)))

"""
We use a single expression that includes lambda, zip and map functions to select create 52 cards in a deck 
"""

def check_flush(hand):
    """
    A function verify True or False for flush.
    """
    suits = [h[1] for h in hand]
    if len(set(suits)) == 1:
        return True
    else:
        return False

# Assigning values to 10 types of flush
def check_hand(hand):
    """
    A function to assign values returned basing on the type of flush.
    """
    if check_royal_flush(hand):
        return 10
    if check_straight_flush(hand):
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
    if check_one_pair(hand):
        return 2
    return 1

# Verifying Straight Flush
def check_straight_flush(hand):
    if check_flush(hand) and check_straight(hand):
        return True
    else:
        return False

# Verifying Four of a Kind
def check_four_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,4]:
        return True
    return False

# Verifying Full House
def check_full_house(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [2,3]:
        return True
    return False

# Verifying Flush
def check_flush(hand):
    suits = [i[1] for i in hand]
    if len(set(suits))==1:
        return True
    else:
        return False

# Verifying Straight
def check_straight(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v] += 1
    rank_values = [card_order_dict[i] for i in values]
    value_range = max(rank_values) - min(rank_values)
    if len(set(value_counts.values())) == 1 and (value_range==4):
        return True
    else:
        #check straight with low Ace
        if set(values) == set(["A", "2", "3", "4", "5"]):
            return True
        return False

# Verifying Three of a Kind
def check_three_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if set(value_counts.values()) == set([3,1]):
        return True
    else:
        return False

# Verifying Two Pairs
def check_two_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values())==[1,2,2]:
        return True
    else:
        return False

# Verifying One Pair
def check_one_pair(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if 2 in value_counts.values():
        return True
    else:
        return False


from itertools import combinations

hand_dict = {10: "royal-flush", 9: "straight-flush", 8: "four-of-a-kind", 7: "full-house", 6: "flush", 5: "straight", 4: "three-of-a-kind",
             3: "two-pairs", 2: "one-pair", 1: "highest-card"}



# Identifying the winner
def play(cards):
    """
    A function to find the best hand based on the hand value.
    """
    hand = cards[:5]
    deck = cards[5:]
    best_hand = 0
    for i in range(6):
        possible_combos = combinations(hand, 5 - i)
        for c in possible_combos:
            current_hand = list(c) + deck[:i]
            hand_value = check_hand(current_hand)
            if hand_value > best_hand:
                best_hand = hand_value

    return hand_dict[best_hand]
