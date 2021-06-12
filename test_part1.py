import pytest
import random
import string
import part1
import os
import inspect
import re
import math
import time
from collections import Counter
from part1 import make_deck_of_cards_loops
from part1 import make_deck_of_cards
from part1 import deal_cards
from part1 import processing_players_hand
from part1 import transform_value_list
from part1 import check_for_suit
from part1 import check_for_number_sequence
from part1 import show_of_hands

README_CONTENT_CHECK_FOR = [
    'make_deck_of_cards_loops',
    'make_deck_of_cards',
    'deal_cards',
    'processing_players_hand',
    'transform_value_list',
    'check_for_suit',
    'check_for_number_sequence',
    'show_of_hands',
    'vals',
    'suits'
]

def test_part1_readme_exists():
    """
    Method checks if there is a README.md file. 
    failure_message: "README.md file missing!"  
    """
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_part1_readme_500_words():
    """
    Method checks if there are atleast 500 words in the README.md file
    failures_message: Make your README.md file interesting! Add atleast 500 words
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_part1_readme_proper_description():
    """
    Method checks if all the functions are described in the README.md file
    failures_message: You have not described all the functions/classes well in your README.md file
    """
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_part1_readme_file_for_more_than_10_hashes():
    """
    Method checks if README.md file has atleast 10 '#' (indentations)
    failures_message: You have not described all the functions/classes well in your README.md file 
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_part1_indentations():
    """
    Method checks for proper indentations \
    Returns pass if used four spaces for each level of syntactically significant indenting.
    failures_message_1: Your script contains misplaced indentations
    failures_message_2: Your code indentation does not follow PEP8 guidelines
    """
    lines = inspect.getsource(part1)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_part1_function_name_had_cap_letter():
    """
    Method checks for any Upper case in the function names in part1.py
    failures_message: You have used Capital letter(s) in your function names
    """
    functions = inspect.getmembers(part1, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


############################## Assignment Validations###########################

vals = [ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace' ]
suits = [ 'spades' , 'clubs' , 'heartss' , 'diamonds' ]
deck_of_cards = make_deck_of_cards(vals, suits)

def test_part1_make_deck_of_cards_len():
    """
    This method checks the length of the deck of cards generated
    failures_message: A deck should have 52 cards!
    """    
    assert len(make_deck_of_cards(vals, suits)) == 52, "A deck should have 52 cards!"

def test_part1_make_deck_of_cards_unique_suits():
    """
    This method checks the if the deck generated are unique in value
    failures_message: There should be 13 of each suit
    """
    deck = make_deck_of_cards(vals, suits)
    suits_deck = [y for x,y in deck]
    assert  all(map(lambda x : True if x[1]==13 else False, Counter(suits_deck).most_common())) == True, "There should be 13 of each suit"

def test_part1_make_deck_of_cards_unique_vals():
    """
    This method checks the if the deck generated are unique in value
    failures_message: There should be 13 of each suit
    """
    deck = make_deck_of_cards(vals, suits)
    vals_deck = [y for x,y in deck]
    assert  all(map(lambda x : True if x[1]==4 else False, Counter(vals_deck).most_common())) == True, "There should be 4 of each value"

def test_part1_make_deck_of_cards_loops_len():
    """
    This method checks the length of the deck of cards generated
    failures_message: A deck should have 52 cards! Check your loop!
    """    
    assert len(make_deck_of_cards_loops(vals, suits)) == 52, "A deck should have 52 cards! Check your loop!"

def test_part1_make_deck_of_cards_loops_unique_suits():
    """
    This method checks the if the deck generated are unique in value
    failures_message: There should be 13 of each suit! Check you loop!
    """
    deck = make_deck_of_cards_loops(vals, suits)
    suits_deck = [y for x,y in deck]
    assert  all(map(lambda x : True if x[1]==13 else False, Counter(suits_deck).most_common())) == True, \
        "There should be 13 of each suit! Check you loops!"

def test_part1_make_deck_of_cards_loops_unique_vals():
    """
    This method checks the if the deck generated are unique in value
    failures_message: There should be 4 of each value! Check your loops!
    """
    deck = make_deck_of_cards_loops(vals, suits)
    vals_deck = [y for x,y in deck]
    assert  all(map(lambda x : True if x[1]==4 else False, Counter(vals_deck).most_common())) == True, \
        "There should be 4 of each value! Check your loops!"

def test_part1_deal_cards_len():
    """
    This method checks the number of cards dealt to the two players
    failure_message: Incorrect number of cards dealt
    """
    player1_deck, player2_deck = deal_cards(3, deck_of_cards)
    assert (len(player1_deck) == 3 and len(player2_deck) == 3) == True , "Incorrect number of cards dealt"

def test_part1_deal_cards_num():
    """
    This method checks the number argument of the deal_card function take string, complex numbers and between 3 and 5
    failures_message: ValueError or TypeError raised
    """
    with pytest.raises(TypeError, match=r".*number_cards should be integer type*"):
        deal_cards('3', deck_of_cards)
    with pytest.raises(TypeError, match=r".*number_cards should be integer type*"):
        deal_cards(3+4j, deck_of_cards)
    with pytest.raises(ValueError, match=r".*number_cards dealt should be between 3 and 5*"):
        deal_cards(7, deck_of_cards)

def test_part1_transform_value_list():
    """
    This method checks the tranform value function
    failures_message: Card value transformation not working as expected
    """
    value_check = [x for x in range(2,15)]
    assert sorted(transform_value_list(vals)) == value_check, "Card value transformation not working as expected"

def test_part1_check_for_suit():
    """
    This method checks if the suits are all the same
    failures_message: Handle the suit properly
    """
    input_list = ['Spades','Spades','Spades','Spades','Spades']
    assert check_for_suit(input_list) == True, "Handle the suit properly"

def test_part1_check_for_number_sequence():
    """
    This method checks if the values are in sequence
    failures_message: Handle the sequence function properly
    """
    input_list = [13, 12, 14, 11, 10]
    assert check_for_number_sequence(input_list) == True, "Handle the sequence function properly"

def test_part1_processing_players_hand():
    """
    This method checks if the values are in sequence
    failures_messages
    """
    player_deck = [('10','hearts'), ('jack','hearts'), ('queen', 'hearts'), ('king', 'hearts'), ('ace', 'hearts')]
    player_vals, player_suits, color_check_player, sequence_check_player = processing_players_hand(player_deck,5)
    assert player_vals == [10, 11, 12, 13, 14], "Handle the Player vals properly"
    assert player_suits == ['hearts', 'hearts', 'hearts', 'hearts', 'hearts'], "Handle the Player suits properly"
    assert color_check_player == True, "Handle the Player suits properly"
    assert sequence_check_player == True, "Handle the Player sequence properly"

def test_part1_processing_players_hand_additional():
    """
    This method checks if the values are in sequence
    failures_messages
    """
    player_deck = [('2','hearts'), ('5','spades'), ('queen', 'hearts'), ('7', 'clubs'), ('ace', 'diamonds')]
    player_vals, player_suits, color_check_player, sequence_check_player = processing_players_hand(player_deck,5)
    assert player_vals == [2, 5, 12, 7, 14], "Handle the Player vals properly"
    assert player_suits == ['hearts', 'spades', 'hearts', 'clubs', 'diamonds'], "Handle the Player suits properly"
    assert color_check_player == False, "Handle the Player suits properly"
    assert sequence_check_player == False, "Handle the Player sequence properly"

def test_part1_show_of_hands_3card_straightflush():
    """
    This method checks if straight flush set is recognised
    failures_messages
    """
    player1_deck = [('4','spades'), ('5','spades'), ('6', 'spades')]
    player2_deck = [('2','hearts'), ('5','spades'), ('queen', 'hearts')]
    
    winning_hand, msg = show_of_hands(player1_deck, player2_deck)
    
    assert winning_hand == [('4','spades'), ('5','spades'), ('6', 'spades')], "incorrect winning hand"
    assert msg == "Straight Flush, Player 1 Wins!", "Incorrect winning message"

def test_part1_show_of_hands_3card_3ofakind():
    """
    This method checks if 3 of a kind set is recognised
    failures_messages
    """
    player1_deck = [('4','spades'), ('10','spades'), ('6', 'hearts')]
    player2_deck = [('2','diamonds'), ('10','diamonds'), ('queen', 'diamonds')]
    
    winning_hand, msg = show_of_hands(player1_deck, player2_deck)
    
    assert winning_hand == [('2','diamonds'), ('10','diamonds'), ('queen', 'diamonds')], "incorrect winning hand"
    assert msg == "3 of Kind, Player 2 Wins!", "Incorrect winning message"

def test_part1_show_of_hands_4card_straights():
    """
    This method checks if the straight set is recognised
    failures_messages
    """
    player1_deck = [('9','spades'), ('10','spades'), ('jack', 'hearts'), ('queen', 'hearts')]
    player2_deck = [('2','diamonds'), ('10','diamonds'), ('queen', 'clubs'), ('king', 'clubs')]
    
    winning_hand, msg = show_of_hands(player1_deck, player2_deck)
    
    assert winning_hand == [('9','spades'), ('10','spades'), ('jack', 'hearts'), ('queen', 'hearts')], "incorrect winning hand"
    assert msg == "Straights, Player 1 Wins!", "Incorrect winning message"

def test_part1_show_of_hands_4card_twopairs():
    """
    This method checks if the Two Pairs set is recognised
    failures_messages
    """
    player1_deck = [('10','clubs'), ('10','spades'), ('jack', 'diamonds'), ('jack', 'hearts')]
    player2_deck = [('2','diamonds'), ('10','diamonds'), ('queen', 'clubs'), ('king', 'clubs')]
    
    winning_hand, msg = show_of_hands(player1_deck, player2_deck)
    
    assert winning_hand == [('10','clubs'), ('10','spades'), ('jack', 'diamonds'), ('jack', 'hearts')], "incorrect winning hand"
    assert msg == "Two Pairs, Player 1 Wins!", "Incorrect winning message"

def test_part1_show_of_hands_5card_royalflush():
    """
    This method checks if the Tie on a Royal Flush set is recognised
    failures_messages
    """
    player1_deck = [('10','clubs'), ('jack','clubs'), ('queen', 'clubs'), ('king', 'clubs'), ('ace', 'clubs')]
    player2_deck = [('10','diamonds'), ('jack','diamonds'), ('queen', 'diamonds'), ('king', 'diamonds'), ('ace', 'diamonds')]
    
    winning_hand, msg = show_of_hands(player1_deck, player2_deck)
    
    assert winning_hand == [('10','clubs'), ('jack','clubs'), ('queen', 'clubs'), ('king', 'clubs'), ('ace', 'clubs')], "incorrect winning hand"
    assert msg == "Tie on a Royal Flush, Player 1 & 2 Win!", "Incorrect winning message"

def test_part1_show_of_hands_5card_fullhouse():
    """
    This method checks if the FullHouse set is recognised
    failures_messages
    """
    player1_deck = [('5','clubs'), ('8','hearts'), ('2', 'clubs'), ('king', 'clubs'), ('ace', 'clubs')]
    player2_deck = [('10','diamonds'), ('10','spades'), ('queen', 'clubs'), ('queen', 'hearts'), ('queen', 'spades')]
    
    winning_hand, msg = show_of_hands(player1_deck, player2_deck)
    
    assert winning_hand == [('10','diamonds'), ('10','spades'), ('queen', 'clubs'), ('queen', 'hearts'), ('queen', 'spades')], "incorrect winning hand"
    assert msg == "Full House, Player 2 Wins!", "Incorrect winning message"

def test_part1_show_of_hands_5card_fullhouse():
    """
    This method checks if the FullHouse set is recognised
    failures_messages
    """
    player1_deck = [('5','clubs'), ('8','hearts'), ('2', 'clubs'), ('king', 'clubs'), ('ace', 'clubs')]
    player2_deck = [('10','diamonds'), ('10','spades'), ('queen', 'clubs'), ('queen', 'hearts'), ('queen', 'spades')]
    
    winning_hand, msg = show_of_hands(player1_deck, player2_deck)
    
    assert winning_hand == [('10','diamonds'), ('10','spades'), ('queen', 'clubs'), ('queen', 'hearts'), ('queen', 'spades')], "incorrect winning hand"
    assert msg == "Full House, Player 2 Wins!", "Incorrect winning message"

def test_part1_show_of_hands_5card_pair():
    """
    This method checks if the tied pair set is recognised
    failures_messages
    """
    player1_deck = [('5','clubs'), ('5','hearts'), ('2', 'spades'), ('king', 'clubs'), ('ace', 'clubs')]
    player2_deck = [('10','diamonds'), ('10','spades'), ('3', 'clubs'), ('king', 'hearts'), ('queen', 'spades')]
    
    winning_hand, msg = show_of_hands(player1_deck, player2_deck)
    
    assert winning_hand == [('10','diamonds'), ('10','spades'), ('3', 'clubs'), ('king', 'hearts'), ('queen', 'spades')], "incorrect winning hand"
    assert msg == "Tie on Pair, Player 2 Wins!", "Incorrect winning message"

def test_part1_show_of_hands_5card_high():
    """
    This method checks if high set is recognised
    failures_messages
    """
    player1_deck = [('5','clubs'), ('8','hearts'), ('2', 'spades'), ('king', 'diamonds'), ('ace', 'clubs')]
    player2_deck = [('10','diamonds'), ('4','spades'), ('3', 'clubs'), ('king', 'hearts'), ('queen', 'spades')]
    
    winning_hand, msg = show_of_hands(player1_deck, player2_deck)
    
    assert winning_hand == [('5','clubs'), ('8','hearts'), ('2', 'spades'), ('king', 'diamonds'), ('ace', 'clubs')], "incorrect winning hand"
    assert msg == "High Card, Player 1 Wins!", "Incorrect winning message"

