# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by:    and Jenna Wiens <jwiens>
#
# Name          : eurodollarclub
# Collaborators : None
# Time spent    : 10+ hours

import math
import random
import sys

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10,
}

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, "r")
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq

def get_word_score(word, n):
    """
    word: string, the word to be scored 
    n: int >= 0, the number of letters in the current hand
    returns: int >= 0, the score
    """
    assert isinstance(word, str), f"{word} not a str"
    assert isinstance(n, int) and n > 0, f"{n} not an int or {n} < 0"

    word = word.lower()
    first_component = 0
    for i in word:
        for k, v in SCRABBLE_LETTER_VALUES.items():
            if k == i:
                first_component += v
    second_component = 7 * len(word) - 3 * (n - len(word))
    if second_component < 0:
        second_component = 1
    return first_component * second_component

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for key in hand.keys():
        for _ in range(hand[key]):
            print(key, end=" ")
    print()

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int > 0
    returns: dictionary (string -> int)
    """
    assert n > 0, f"{n} <= 0"

    hand = {}
    num_vowels = int(math.ceil(n / 3))
    random_i = random.choice(range(num_vowels))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        if random_i == i:
            x = "*"
        hand[x] = hand.get(x, 0) + 1

    for _ in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand

def update_hand(hand, word):
    """
    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    Has no side effects: does not modify hand.
    """
    assert isinstance(hand, dict), f"type of {hand} not dict"
    assert isinstance(word, str), f"type of {word} not str"

    word = word.lower()
    new_hand = hand.copy()

    for i in range(len(word)):
        for k, v in new_hand.items():
            if k == word[i]:
                new_hand[k] = v - 1
                if new_hand[k] < 1:
                    new_hand[k] = 0
    return new_hand

def is_valid_word(word, hand, word_list):
    """
    * if word doesn't contain a wildcard,
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    * if word contains a wildcard,
    Returns True if at least one valid word can be formed,
    with the wildcard as a vowel

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    assert isinstance(word, str), f"{word} not a str"
    assert isinstance(hand, dict), f"{hand} not a dict"
    assert isinstance(word_list, list), f"{word_list} not a list"

    word = word.lower()
    new_hand = hand.copy()
 
    if "*" not in word:
        for k in word:
            try:
                v = new_hand[k]
            except(KeyError):
                pass
            if k not in new_hand:
                return False
            elif k in new_hand and v < 1:
                return False
            else:
                new_hand[k] = v - 1
        if word in word_list:
            return True
    else:
        for i in word:
            if i not in hand:
                return False
            
        for i in VOWELS:
            for j in word:
                if j == "*":
                    if (lambda i: word.replace("*", i))(i) in word_list:
                        return True
                    break
        return False   

def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string-> int)
    returns: integer
    """
    assert isinstance(hand, dict), f'{hand} not a dict'

    length = 0
    for v in hand.values():
        length += v
    return length

def play_hand(hand, word_list):
    """
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: the total score for the hand

    goal/understanding:
    total score as a function of hand(dict), word_list(string)

    strategy:
    Keep track of the total score
    As long as there are still letters left in the hand:
    Display the hand
    Ask user for input
    If the input is two exclamation points:
    End the game (break out of the loop)
    Otherwise (the input is not two exclamation points):
    If the word is valid:
    Tell the user how many points the word earned,
    and the updated total score
    Otherwise (the word is not valid):
    Reject invalid word (print a message)
    update the user's hand by removing the letters of their inputted word
    Game is over (user entered '!!' or ran out of letters),
    so tell user the total score
    Return the total score as result of function

    implimentation:

    evaluation:
    """
    assert isinstance(hand, dict),f'{hand} is not dict'
    assert isinstance(word_list, list), f'{word_list}, is not a list'

    total_score = 0

    while True:
        if calculate_handlen(hand) < 1:
            print(f"Run out of letters. Total score for this hand: {total_score}", "\n")
            return total_score

        print("Current Hand:", end=" ")
        display_hand(hand)
        word = input('Enter word or "!!" to indicate that you are finished: ')

        if word != "!!" and calculate_handlen(hand) > 1:
            if is_valid_word(word, hand, word_list):
                current_score = get_word_score(word, calculate_handlen(hand))
                total_score += current_score
                hand = update_hand(hand, word)
                print(f'"{word}" earned {current_score} points. Total: {total_score} points', "\n")
            else:
                hand = update_hand(hand, word)
                print("This is not a valid word. Please choose another word.", "\n")
        else:
            print("Total score for this hand ", total_score)
            print('---------------')
            return total_score 

def substitute_hand(hand, letter):
    """
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.
    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    assert isinstance(hand, dict), f'{hand} is not dict'
    assert isinstance(letter, str), f'{letter} is not str'

    vowels_consonants = list(VOWELS + CONSONANTS)
    vowels_consonants.remove(letter)
    random.shuffle(vowels_consonants)
    r_letter = random.choice(vowels_consonants)
    new_hand = hand.copy()

    if letter not in hand:
        return hand 
    else:
        for k in hand.keys(): 
            if k == letter:
                while r_letter in new_hand:
                    r_letter = random.choice(vowels_consonants)
                new_hand[r_letter] = new_hand.pop(k)
                break

    return new_hand

def print_hand(hand):
    print("Current Hand:", end=" ")
    display_hand(hand)

def play_game(word_list):
    """
    Allow the user to play a series of hands
    word_list: list of lowercase strings
    """
    assert isinstance(word_list, list), f'{word_list} not list'
    total_score_each_hand = 0

    total_number_hands = input("Enter total number of hands: ")
    assert total_number_hands.isdigit(), f'NaN' 
    
    for _ in range(int(total_number_hands)):
        random_int = random.randint(2,8)
        current_hand = deal_hand(random_int)
        print_hand(current_hand)

        while input("Would you like to substitute a letter ? ") == 'yes':
            substitute_letter = input("Which letter would you like to replace, y for yes n for no")
            current_hand = substitute_hand(current_hand, substitute_letter)
            print_hand(current_hand)
        else:
            print()
            total_score_each_hand += play_hand(current_hand,word_list)
        
    print('Total score over all hands', total_score_each_hand)


if __name__ == "__main__":
    word_list = load_words()
    play_game(word_list)
   