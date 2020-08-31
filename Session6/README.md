# Game of Poker:

To write a python program to create a deck of 52 cards - (i) With a single expression using lambda, zip & map functions. (ii) without using the above 3 functions. (iii) Docstrings and Annotations must be used when defining the functions.

The following are the considerations.

2 sets of 5 cards each Only one deck of cards The order of ranking is Royal Flush > Straight Flush > Four of a Kind > Full House > Flush > Straight > Three of a Kind > Two Pair > One Pair > High Card.

Royal Flush: a straight flush including ace, king, queen, jack, and ten all in the same suit, which is the hand of the highest possible value. Straight Flush: a hand that contains five cards of sequential rank, all of the same suit. Four of a Kind: a hand that contains four cards of one rank and one card of another rank. Full House: a hand that contains three cards of one rank and two cards of another rank. Flush: a hand that contains five cards all of the same suit, not all of sequential rank. Straight: a hand that contains five cards of sequential rank, not all of the same suit. Three of a Kind: a hand that contains three cards of one rank and two cards of two other ranks. Two Pair: a hand that contains two cards of one rank, two cards of another rank and one card of a third rank. One Pair: a hand that contains two cards of one rank and three cards of three other ranks. High Card: a hand that does not fall into any other category

Functions:

def check_flush: To return True/False for checking flush. def check_hand(hand): To assign values to the type of flush returned. The following functions are used to return True/False for each type of flush. def check_straight_flush: To verify straight flush def check_four_of_a_kind: To verify Four of a Kind def check_full_house: To verify Full House def check_flush: To verify Flush def check_straight: To verify straight def check_three_of_a_kind: To verify Three of a Kind def check_two_pairs: To verify Two Pairs def check_one_pairs: To verify One Pair. def play(cards): returns list of best hand

Test Cases:

def test_readme_exists: Test case to verify if README.md exists

def test_readme_contents: Test case to verify if README.md carries more than 500 words

def test_readme_proper_description: Test case to verify if all the functions have been properly described.

def test_readme_file_for_formatting: Test case to verify if README.md is properly formatted with UTF-8 and there are minimum 10 comments.

def test_indentations: Test case to verify if the code is properly formatted and there are no tabs used.

def test_function_name_had_cap_letter: Test case to verify if the function names do not contain upper case letters.

def test_docstrings_function: Test case to verify if docstrings have been used in the code.

def test_function_annotations: Test case to verify if annotations have been used in the code.
