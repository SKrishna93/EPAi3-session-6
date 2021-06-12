# Session-6
# EPAi Assignment 6 - First Class Functions
# Assignment 1
import random
from collections import Counter
# Creating a suit of cards
vals = ['2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace']
suits = ['spades' , 'clubs' , 'hearts' , 'diamonds']
deck_of_cards = [] # Created using lambda and zip functions
normal_deck_of_cards = [] # Created using for loops
# Deck of Cards using for loops
def make_deck_of_cards_loops(vals : list, suits : list) -> "returns a deck 52 cards using for loops":
    '''Function creates a deck of cards using for loops
    Input:-
        vals: list of card values
        suits: list of suit values
    Return:-
        deck: list of deck of cards, where each card is represented as a tuple of (vals,suit)
    '''
    deck = []
    for suit in suits:
        for val in vals:
            deck.append(tuple([val,suit]))
    return deck
# Creating deck of cards in a single line of code using lambda and zip functions
# Defining lambda functions to create a list of vals and suits
fn_val = lambda x : x * 4
fn_suit = lambda x : x * 13
# Create a deck of cards using lambda and zip functions
def make_deck_of_cards(vals : list, suits : list) -> "returns a deck 52 cards using lambda and zip functions":
    '''Function creates a deck of cards using lambda and Zip function
    Input:-
        vals: list of card values
        suits: list of suit values
    Return:-
        my_deck: list of deck of cards, where each card is represented as a tuple of (vals,suit)
    '''
    my_deck = list(zip(fn_val(vals),fn_suit(suits)))
    return my_deck
# Shuffle and Deal the cards to players
def deal_cards(number_cards: "int (3 or 4 or 5)" = 3, deck: "list of cards (deck)" = deck_of_cards) -> "returns Two sets of (3 or 4 or 5) randomly dealt cards":
    '''Functions returns 2 sets of randomly dealt 3, 4 or 5 cards
    Input:-
        number_cards: Integer 3 or 4 or 5. Default: 3 per player
        deck: A list of deck of cards. Default: deck_of_cards 
    Return:-
        set1 and set2: Two sets of (3 or 4 or 5) randomly dealt cards
    '''
    if not (isinstance(number_cards,int)):
        raise TypeError ("number_cards should be integer type")
    if not (number_cards >=3 and number_cards <=5):
        raise ValueError("number_cards dealt should be between 3 and 5")
    deal1=[]
    deal2=[]
    random.shuffle(deck)
    for i in range(number_cards):
        deal1.append(deck.pop())
        deal2.append(deck.pop())
    return deal1, deal2
# Function used to transform the value list into integers
def transform_value_list(player_list:list)->list:
    '''
    This function converts the list to integer format 
    Input
        player1_list: List of cards without suits.
    Returns
        Returns a list of cards converted to integer type for each player
    '''
    for i in range(len(player_list)):
        if player_list[i]=='jack':
            player_list[i] = 11
        elif player_list[i]=='queen':
            player_list[i] = 12
        elif player_list[i]=='king':
            player_list[i] = 13
        elif player_list[i]=='ace':
            player_list[i] = 14
    return list(map(lambda x: int(x),player_list))
# Check for the suits dealt to the player
def check_for_suit(suit_set_list: list) -> bool:
    '''
    This function checks if the list contains the suits of the hands are all same or not
    Input
        suit_set_list: list of suits of cards that a player is holding
    Returns
        It returns a bool value which says whether they are of same color or not
    '''
    if len(set(suit_set_list)) == 1:
        return True
    else:
        return False
# Check for sequence in the card sequence
def check_for_number_sequence(value_set_list:list) -> bool:
    '''
    This function checks if the list caontaining all numeric value of card are in sequence
    Input:
        value_set_list: List containing all the numeric value of cards
    Output:
        It returns a bool value indicating whether they are in sequence or not.
    '''
    return sorted(value_set_list) == list(range(min(value_set_list),max(value_set_list)+1))
def show_of_hands(set1: "List", set2: "List") -> "returns which hands wins":
    '''Function checks the players card dealt and determines who wins
    Input:- 
        set1: list of cards dealt to player 1
        set2: list of cards dealt to player 2
    Return:-
        winning_hand: list
    '''
    number_of_cards = len(set1)
    #Unpacking cards
    player1_vals, player1_suits, color_check_player1, sequence_check_player1 = processing_players_hand(set1, number_of_cards)
    player2_vals, player2_suits, color_check_player2, sequence_check_player2 = processing_players_hand(set2, number_of_cards)
    player1_vals_counter = Counter(player1_vals)
    player2_vals_counter = Counter(player2_vals)
    player1_win_flag = False
    player2_win_flag = False
    # 3 Card Poker game
    if number_of_cards == 3:
        # Checking for Winning hand
        # Check for straight flush
        if (color_check_player1 and sequence_check_player1):
            return set1, "Straight Flush, Player 1 Wins!"
        elif(color_check_player2 and sequence_check_player2):
            return set2, "Straight Flush, Player 2 Wins!"
        # Check for '3 of a kind'
        if (all(x == player1_vals[0] for x in player1_vals)):
            return set1, "3 of Kind, Player 1 Wins!"
        elif(all(x == player2_vals[0] for x in player2_vals)):
            return set2, "3 of Kind, Player 2 Wins!"
        # Check for 'Straights'
        if (sequence_check_player1 and not color_check_player1):
            return set1, "Straights, Player 1 Wins!"
        elif(sequence_check_player2 and not color_check_player2):
            return set2, "Straights, Player 2 Wins!"
        # Check for 'Flush'
        if (color_check_player1):
            return set1, "Flush, Player 1 Wins!"
        elif(color_check_player2):
            return set2, "Flush, Player 2 Wins!"
        # Check for 'Pair'
        if (player1_vals[0] == player1_vals[1] or player1_vals[1] == player1_vals[2] or player1_vals[2] == player1_vals[0]):
            return set1, "Pair, Player 1 Wins!"
        elif(player2_vals[0] == player2_vals[1] or player2_vals[1] == player2_vals[2] or player2_vals[2] == player2_vals[0]):
            return set2, "Pair, Player 2 Wins!"
        # Check for 'High'
        if not (color_check_player1 and sequence_check_player1):
            if (max(player1_vals) > max(player2_vals)):
                return set1, "High Card, Player 1 Wins!"
            else:
                return set2, "High, Player 2 Wins!"
    # 4 Card Poker game
    elif number_of_cards == 4:
        # Checking for Winning hand
        # Check for royal flush
        if (color_check_player1 and sequence_check_player1):
            if (sorted(player1_vals) == [11, 12, 13, 14]):
                player1_win_flag = True
        elif(color_check_player2 and sequence_check_player2):
            if (sorted(player2_vals) == [11, 12, 13, 14]):
                player1_win_flag = True
        if (player1_win_flag and player2_win_flag):
            return set1, "Tie on a Royal Flush"
        elif player1_win_flag:
            return set1, "Royal Flush, Player 1 Wins!"
        elif player2_win_flag:
            return set2, "Royal Flush, Player 2 Wins!"
        # Check for straight flush
        if (color_check_player1 and sequence_check_player1):
            return set1, "Straight Flush, Player 1 Wins!"
        elif(color_check_player2 and sequence_check_player2):
            return set2, "Straight Flush, Player 2 Wins!"
        # Check for '4 of a kind'
        if (len(player1_vals_counter) == 1):
            return set1, "4 of Kind, Player 1 Wins!"
        elif(len(player2_vals_counter) == 1):
            return set2, "4 of Kind, Player 2 Wins!"
        # Check for '3 of a kind'
        if (player1_vals_counter.most_common()[0][1] == 3):
            return set1, "3 of Kind, Player 1 Wins!"
        elif(player2_vals_counter.most_common()[0][1] == 3):
            return set2, "3 of Kind, Player 2 Wins!"
        # Check for 'Straights'
        if (sequence_check_player1 and not color_check_player1):
            return set1, "Straights, Player 1 Wins!"
        elif(sequence_check_player2 and not color_check_player2):
            return set2, "Straights, Player 2 Wins!"
        # Check for 'Two Pairs'
        if (player1_vals_counter.most_common()[0][1] == 2 and player1_vals_counter.most_common()[1][1] == 2):
            return set1, "Two Pairs, Player 1 Wins!"
        elif(player1_vals_counter.most_common()[0][1] == 2 and player2_vals_counter.most_common()[1][1] == 2):
            return set2, "Two Pairs, Player 2 Wins!"
        # Check for 'Pair'
        if (player1_vals_counter[list(player1_vals_counter)[0]] == 2 or player1_vals_counter[list(player1_vals_counter)[1]] == 2):
            return set1, "Pair, Player 1 Wins!"
        elif(player2_vals_counter[list(player2_vals_counter)[0]] == 2 or player2_vals_counter[list(player2_vals_counter)[1]] == 2):
            return set2, "Pair, Player 2 Wins!"
        # Check for 'High'
        if not (color_check_player1 and sequence_check_player1):
            if (max(player1_vals) > max(player2_vals)):
                return set1, "High Card, Player 1 Wins!"
            else:
                return set2, "High Card, Player 2 Wins!"
    # 5 Card Poker game
    else:
        # Checking for Winning hand
        # Check for royal flush
        if (color_check_player1 and sequence_check_player1):
            if (sorted(player1_vals) == [10, 11, 12, 13, 14]):
                player1_win_flag = True
        if(color_check_player2 and sequence_check_player2):
            if (sorted(player2_vals) == [10, 11, 12, 13, 14]):
                player2_win_flag = True
        if (player1_win_flag and player2_win_flag):
            return set1, "Tie on a Royal Flush, Player 1 & 2 Win!"
        elif player1_win_flag:
            return set1, "Royal Flush, Player 1 Wins!"
        elif player2_win_flag:
            return set2, "Royal Flush, Player 2 Wins!"
        # Check for straight flush
        if (color_check_player1 and sequence_check_player1):
            player1_win_flag = True
        if (color_check_player2 and sequence_check_player2):
            player2_win_flag = True
        if (player1_win_flag and player2_win_flag):
            if (max(player1_vals) > max(player2_vals)):
                return set1, "Tie on a Straight Flush, Player 1 Wins!"
            else:
                return set2, "Tie on a Straight Flush, Player 2 Wins!"
        elif (player2_win_flag):
            return set2, "Straight Flush, Player 2 Wins!"
        elif (player1_win_flag):
            return set1, "Straight Flush, Player 1 Wins!"
        # Check for '4 of a kind'
        if (player1_vals_counter[list(player1_vals_counter)[0]] == 4 or player1_vals_counter[list(player1_vals_counter)[1]] == 4):
            player1_win_flag = True
        if (player2_vals_counter[list(player2_vals_counter)[0]] == 4 or player2_vals_counter[list(player2_vals_counter)[1]] == 4):
            player2_win_flag = True
        if (player1_win_flag and player2_win_flag):
            if (max(player1_vals) > max(player2_vals)):
                return set1, "Tie on 4 of Kind, Player 1 Wins!"
            else:
                return set2, "Tie on 4 of Kind, Player 2 Wins!"
        elif (player2_win_flag):
            return set2, "4 of Kind, Player 2 Wins!"
        elif (player1_win_flag):
            return set1, "4 of Kind, Player 1 Wins!"
        # Check for 'Full House'
        if (player1_vals_counter.most_common()[0][1] == 3 and player1_vals_counter.most_common()[1][1] == 2 ):
            player1_win_flag = True
        if (player2_vals_counter.most_common()[0][1] == 3 and player2_vals_counter.most_common()[1][1] == 2):
            player2_win_flag = True
        if (player1_win_flag and player2_win_flag):
            if (max(player1_vals) > max(player2_vals)):
                return set1, "Tie on Full House, Player 1 Wins!"
            else:
                return set2, "Tie on Full House, Player 2 Wins!"
        elif (player1_win_flag):
            return set1, "Full House, Player 1 Wins!"
        elif (player2_win_flag):
            return set2, "Full House, Player 2 Wins!"
        # Check for 'Flush'
        if (not sequence_check_player1 and color_check_player1):
            player1_win_flag = True
        if(not sequence_check_player2 and color_check_player2):
            player2_win_flag = True
        if (player1_win_flag and player2_win_flag):
            if (max(player1_vals) > max(player2_vals)):
                return set1, "Tie on Flush, Player 1 Wins!"
            else:
                return set2, "Tie on Flush, Player 2 Wins!"
        elif (player2_win_flag):
            return set2, "Flush, Player 2 Wins!"
        elif (player1_win_flag):
            return set1, "Flush, Player 1 Wins!"
        #Check for 'Straights'
        if (sequence_check_player1 and not color_check_player1):
            player1_win_flag = True
        if(sequence_check_player2 and not color_check_player2):
            player2_win_flag = True
        if (player1_win_flag and player2_win_flag):
            if (max(player1_vals) > max(player2_vals)):
                return set1, "Tie on Straights, Player 1 Wins!"
            else:
                return set2, "Tie on Straights, Player 2 Wins!"
        elif (player2_win_flag):
            return set2, "Straights, Player 2 Wins!"
        elif (player1_win_flag):
            return set1, "Straights, Player 1 Wins!"
        # Check for '3 of a kind'
        if (player1_vals_counter.most_common()[0][1] == 3):
            player1_win_flag = True
        if (player2_vals_counter.most_common()[0][1] == 3):
            player2_win_flag = True
        if (player1_win_flag and player2_win_flag):
            if (player1_vals_counter.most_common()[0][0] > player2_vals_counter.most_common()[1][0]):
                return set1, "Tie on 3 of a Kind, Player 1 Wins!"
            else:
                return set2, "Tie on 3 of a Kind, Player 2 Wins!"
        elif (player2_win_flag):
            return set2, "3 of Kind, Player 2 Wins!"
        elif (player1_win_flag):
            return set1, "3 of Kind, Player 1 Wins!"
        # Check for 'Two Pairs'
        if (player1_vals_counter.most_common()[0][1] == 2 and player1_vals_counter.most_common()[1][1] == 2):
            player1_win_flag = True
        if(player2_vals_counter.most_common()[0][1] == 2 and player2_vals_counter.most_common()[1][1] == 2):
            player2_win_flag = True
        if (player1_win_flag and player2_win_flag):
            if (max(player1_vals_counter.most_common()[0][0], player1_vals_counter.most_common()[1][0])) > (max(player2_vals_counter.most_common()[0][0], player2_vals_counter.most_common()[1][0])):
                return set1, "Tie on Two Pairs, Player 1 Wins!"
            else:
                return set2, "Tie on Two Pairs, Player 2 Wins!"
        elif (player2_win_flag):
            return set2, "Two Pairs, Player 2 Wins!"
        elif (player1_win_flag):
            return set1, "Two Pairs, Player 1 Wins!"
        # Check for 'Pair'
        if (player1_vals_counter.most_common()[0][1] == 2):
            player1_win_flag = True
        if(player2_vals_counter.most_common()[0][1] == 2):
            player2_win_flag = True
        if (player1_win_flag and player2_win_flag):
            if (player1_vals_counter.most_common()[0][0] > player2_vals_counter.most_common()[0][0]):
                return set1, "Tie on Pair, Player 1 Wins!"
            else:
                return set2, "Tie on Pair, Player 2 Wins!"
        elif (player2_win_flag):
            return set2, "A Pair, Player 2 Wins!"
        elif (player1_win_flag):
            return set1, "A Pair, Player 1 Wins!"
        # Check for 'High'
        if not (color_check_player1 and sequence_check_player1):
            if (max(player1_vals) > max(player2_vals)):
                return set1, "High Card, Player 1 Wins!"
            else:
                return set2, "High Card, Player 2 Wins!"
def processing_players_hand(player_set: "List", number_of_cards: "int")-> "player_vals, player_suits, color_check_player, sequence_check_player":
    '''Function takes the player cards as a list and processes them for face suits, value sequence
    Input:-
        player_set: List of cards for the players
        number_of_cards: integer representing number of cards dealt to a player
    Returns:-
        player_vals: List of values of the card dealt in integer
        player_suits: List of values of suits of the card dealt
        color_check_player: Boolean values if the card dealt to the player belong to the same suit
        sequence_check_player: Boolean values if the card dealt to the player are in a sequence
    '''
    # Separting player cards values and suits
    if (number_of_cards == 3):
        player_card1, player_card2, player_card3 = player_set
        player_vals = [player_card1[0], player_card2[0], player_card3[0]]
        player_suits = [player_card1[1], player_card2[1], player_card3[1]]
    elif (number_of_cards == 4):
        player_card1, player_card2, player_card3, player_card4 = player_set
        player_vals = [player_card1[0], player_card2[0], player_card3[0], player_card4[0]]
        player_suits = [player_card1[1], player_card2[1], player_card3[1], player_card4[1]]
    else:
        player_card1, player_card2, player_card3, player_card4, player_card5 = player_set
        player_vals = [player_card1[0], player_card2[0], player_card3[0], player_card4[0], player_card5[0]]
        player_suits = [player_card1[1], player_card2[1], player_card3[1], player_card4[1], player_card5[1]]
    #Converting player Values from string to integer
    player_vals = transform_value_list(player_vals)
    #Checking player suit for same suit
    color_check_player = check_for_suit(player_suits)
    #Checking player cards sequence
    sequence_check_player = check_for_number_sequence(player_vals)    
    return player_vals, player_suits, color_check_player, sequence_check_player