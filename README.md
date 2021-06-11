# Session 6 Assignment of EPAi3.0

## Higher Order Functions / First Class Functions

### Assignment - 1 

### Objective: Poker game

* Write a single expression that includes lambda, zip, and map functions to select create 52 cards in a deck - 50 pts
* Write a normal function without using lambda, zip, and map function to create 52 cards in a deck - 50 pts
* Write a function that, when given 2 sets of 3 or 4 or 5 cards (1 game can only have 3 cards with each player or 4 cards or 5 cards per player) (1 deck of cards only), (2 players only), can identify who won the game of poker (Links to an external site.)! - 100 pts


#### Poker Game with 3, 4, or 5 cards

* __make_deck_of_cards_loops (vals, suits)__ :
+ The method returns a deck of cards generated using 2 for loops each running on list vals and suits
+ The method takes 2 positional argument _'vals'_ and _'suits'_
+ vals: list containing all the card values from 2-10 and jack, queen, king and ace
+ suits: list containing all the suits in a deck of cards
+ __Algorithm__: Two concurrent for loops are run on the vals and suits iterable to create a deck of cards

* __make_deck_of_cards (vals, suits)__ :
+ The method returns a deck of cards generated using 2 lambda and zip functions
+ The method takes 2 positional argument _'vals'_ and _'suits'_
+ vals: list containing all the card values from 2-10 and jack, queen, king and ace
+ suits: list containing all the suits in a deck of cards
+ __Algorithm__: lambda functions are used to create repeating entries of vals and suits. The zip function ties them togther to
return a deck of cards

 __deal_cards (number_cards = 3, deck)__ :
+ The method randomly deals 2 sets cards to the players based on number of cards in play and the deck of cards passed
+ The method takes 2 positional argument *'number_cards'* and _'deck'_
+ number_cards: Integer which represents the number of cards the player wants to play with (3 or 4 or 5)
+ deck: A list containing the deck of cards generated earlier
+ __Algorithm__: random.shuffle() is used to shuffle the entries if the deck and pop() method is used to assign the last card from the list

 __processing_players_hand (player_set, number_of_cards)__ :
+ The method processes the cards dealt to the players and, it returns 
    + player_vals - A list of values of the cards
    + player_suits - A list of suits of the cards
    + color_check_player - Boolean flag if the player_suits are all the same
    + sequence_check_player - Boolean flag if the player_vals are in a sequence
+ The method takes 2 positional argument *'player_set'* and *'number_of_cards'*
+ number_cards: Integer which represents the number of cards the player wants to play with (3 or 4 or 5)
+ player_set: A list containing the cards dealt to the players 
+ __Algorithm__: Stripping the vals and suits of the cards dealt to the players and calling transform_value_list(), check_for_suit() and check_for_number_sequence()

__transform_value_list (player_vals)__ :
+ The method processes the value of the players cards and returns integer equivalent
    + player_vals - A list of values of the cards in int(), 'jack' = 11, 'queen' = 12, 'king' = 13 and 'ace' = 14
+ The method takes 1 positional argument *'player_vals'*
+ player_vals: A list containing the values of the cards dealt to the players in string format
+ __Algorithm__: casting int() on string elements and hardcoding 'jack' = 11, 'queen' = 12, 'king' = 13 and 'ace' = 14

__check_for_suit (suit_set_list)__ :
+ The method processes the suits of the players cards and returns boolean True or False
    + suit_set_list - True if all the suit values are same else False
+ The method takes 1 positional argument *'suit_set_list'*
+ suit_set_list: A list of suits of the player card in string format
+ __Algorithm__: Create a set out of the suit_set_list and check if 1

__check_for_number_sequence (value_set_list)__ :
+ The method processes the suits of the players cards and returns boolean True or False
    + value_set_list - True if elements are in a sequence
+ The method takes 1 positional argument *'value_set_list'*
+ value_set_list: A list of values of the cards in int()
+ __Algorithm__: sort the list and check if the values are in a sequence

__show_of_hands (set1, set2)__ :
+ The method processes the suits of the players cards and returns boolean True or False
    + set1 or set2 - Winning hand in the round
    + msg - Appropriate message which conveys which hand/player has won and how
+ The method takes 2 positional argument *'set1'* and *'set2'*
+ set1: A list of cards dealt to player 1
+ set2: A list of cards dealt to player 2
+ __Algorithm__: Check the various hands in poker for 3 card, 4 card and 5 card game in their order of precedence and declare winner

------------------------------------------------------------------------------------------------------------------------------------------------


### Assignment - 2

### Objective: Miscellaneous programs

