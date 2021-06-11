# Session-6
# EPAi Assignment 6 - First Class Functions

# Assignment 2

from random import randint, choice
from math import exp
from re import sub
from functools import reduce, partial
import string


def check_fib_seq(list_number: "list") -> "numbers which are in the fib series":
    '''
    Generate a Fibonacci series upto 10000 and 
    check if the numbers passed in the list belong to the sequence
    Input : list_numbers - list of integers to be checked against the fib sequence
    Output : list of numbers in the fib sequence
    '''
    # Generate Fibonacci sequence using list comprehension
    fib_seq = [0, 1]
    [fib_seq.append(fib_seq[-2] + fib_seq[-1]) for x in range(20)]

    # Using filter
    return list(filter(lambda x : x in fib_seq, list_number))

def add_even_odd(num : "int") -> "list of sum of the even and odd numbers":
    '''Function generates n random integers between 2 and 100 and seperates them into even and odd list
    returns a sum of these lists
    Input: num - a positve integer to generate n random samples
    Output: list of sum of odd and even numbers'''
    
    even_list = list(filter(lambda x : x%2 == 0, [randint(2,100) for x in range(num)]))
    odd_list = list(filter(lambda x : x%2 != 0, [randint(2,100) for x in range(num)]))
    
    print(f"This is the list with even numbers: {even_list}")
    print(f"This is the list with odd numbers: {odd_list}")
    
    return [i + j for i,j in zip(even_list,odd_list)]

def strip_vowel(string: "str")-> "return string without vowels":
    '''Function removes the vowel string literals from any string passed and returns the string
    Input: string
    Output: string without the vowels'''
    string_without_vowels = "".join([x for x in string.lower() if x not in ['a', 'e', 'i', 'o', 'u']])
    return string_without_vowels

def sigmoid_func(input_list: "list")->"retrun list of sigmoid values":
    '''Function takes the input list of values and returns the sigmoid values of the elements
    Input: List of numbers
    Output: list of corresponding sigmoid values
    '''
    sig_list = list(map(lambda x : round(1 / (1 + exp(-x)), 4), input_list))
    return sig_list

def shift_literals(string: "str")-> "return the string shifted by 5 characters":
    '''Function shifts the passed literals in the string by 5 places
    Input: string
    Output: string literals shifted by 5 places
    '''
    alpha_dict = {'a':'f', 'b':'g', 'c':'h', 'd':'i', 'e':'j', 'f':'k', 'g':'l', 'h':'m', 'i':'n', 'j':'o', 'k':'p', 
    'l':'q', 'm':'r', 'n':'s', 'o':'t', 'p':'u', 'q':'v', 'r':'w', 's':'x', 't':'y', 'u':'z', 'v':'a', 'w':'b', 'x':'c',
    'y':'d', 'z':'e', ' ':' '}
    word = "".join(list(map(lambda x: alpha_dict[x.lower()],string)))
    return word

def check_for_profanity(input_para: "str")-> "Checks the input paragraph for any profanity":
    '''Function checks the input paragraph for the profanity using the content_list
    Input: Long string paragraph
    Output: True if any profanity exists in the paragraph
    '''
    my_file = open("E:\\Nikhil\\EPAi\\Assignments\\session-6\\list.txt", "r", newline=None)
    profanity_list = my_file.read().split("\n")
    my_file.close()

    profs=[]

    input_list = [sub(r'[^A-Za-z0-9]+', '', x) for x in input_para.split()]
    profs = list(filter(lambda x : x in profanity_list, input_list))
    
    return bool(profs)

def reduce_add_even(input_list: "list")-> "reduce and return the sum of even numbers":
    '''Function reduces the input list to a list containing even numbers and sum of those numbers
    Input: input_list - list of integers
    Output: integer - sum of the even numbers in the list
    '''
    return reduce(lambda x, y : x+y,list(filter(lambda x : x%2==0,input_list)))

def reduce_biggest_char(input_string: "string")-> "reduce and return largest character in a string":
    '''Function reduces the string to its largest character
    Input: input_string - string
    Output: largest string literal 
    '''
    return reduce(lambda x, y : x if x > y else y, input_string)

def add_third_number(input_list: "list")-> "reduce and return the even numbers":
    '''Function reduces the input list to a list containing every third element and sum of those numbers
    Input: input_list - list of integers
    Output: integer - sum of the every third element in the list
    '''
    return reduce(lambda x, y : x + y, [y for x,y in enumerate(input_list) if (x+3) % 3 == 0])

def number_plates(num: "int")-> "returns a list of 'num' vehicle number plates":
    '''Function returns 'num' number of vehicle number plates starting with KA
    input: num, number of vehicle plates required
    output: list of vehicle number plates
    '''
    return [("KA"+"-"+str(randint(10,99))+"-"+choice(string.ascii_uppercase)+choice(string.ascii_uppercase)+"-"+str(randint(1000,9999))) for x in range(num)]

'''Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided. 
Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided PTS:50'''

def func_num_plate(num: "int", state: "string", num_plate_lower: "int"= 1000, num_plate_upper: "int" = 9999)-> "returns a list of 'num' vehicle number plates":
    '''Function returns 'num' number of vehicle number plates starting with KA
    input:
    num, number of vehicle plates required
    state, 'KA' or 'DL'
    output: list of vehicle number plates
    '''
    return [(state+"-"+str(randint(10,99))+"-"+choice(string.ascii_uppercase)+choice(string.ascii_uppercase)+"-"+str(randint(num_plate_lower,num_plate_upper))) for x in range(num)]

partial_num_plate = partial(func_num_plate,15)