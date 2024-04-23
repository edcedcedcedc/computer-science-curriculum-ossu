# Problem Set 2, hangman.py
# Name: eurodollarclub
# Collaborators: -
# Time spent: approx 10 hours+

import random
import string
import sys

def load_words():
    """
    Returns: a list of valid words. Words are strings of lowercase letters;\n
    Depending on the size of the word list, this function may
    take a while to finish.
    """
   
    print("Loading word list from file...")

    try:
        inFile = open('words.txt', "r")
        line = inFile.readline()
        wordlist = line.split()
        print(len(wordlist), "words loaded.")
        return wordlist
    except Exception as message:
        print("Words were not found...i.e",message)
        sys.exit()


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)\n
    Returns: a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    if len(set(secret_word)) != len(set(letters_guessed)):
        return False

    for i in letters_guessed:
        if i not in secret_word:
            return False

    return True

def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    guessed_word = ""
    for i in secret_word:
        if i in letters_guessed:
            guessed_word += i
        else:
            guessed_word += "_ "
    return guessed_word


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    english_letters = string.ascii_lowercase
    updated_english_letters = ""
    for i in english_letters:
        if i not in letters_guessed:
            updated_english_letters += i
    return updated_english_letters


def output_to_console(
    key="", secret_word="", guesses=None, letters=[], warnings=None, score=None
):
    """
    key: string to match the case,
    secret_word: the guessable word,
    guesses: the number of actual guesses,
    letters: the list of guessed letters,
    warnings: actual warnings,
    returns: None, prints whatever the match case was
    """
    match key:
        case "welcome":
            print("Welcome to the game of Hangman!")
        case "thinking":
            print(f"I am thinking of a word that is {len(secret_word)} letters long")
        case "dash":
            print("-------------")
        case "guesses":
            print(f"You have {guesses} guesses left.")
        case "available_letters":
            print(f"Avalable letters {get_available_letters(letters)}")
        case "good_guess":
            print(f"Good guess: {get_guessed_word(secret_word, letters)}")
        case "bad_guess":
            print(
                f"Oop! That letter is not in my word: {get_guessed_word(secret_word, letters)}"
            )
        case "invalid_guess":
            print(
                f"Oop! That is not a valid letter.You have {warnings} warnings left: {get_guessed_word(secret_word, letters)}"
            )
        case "already_guess":
            print(
                f"Oops! You've already guessed that letter.You now have {warnings} warnings\n{get_guessed_word(secret_word, letters)}"
            )
        case "warning":
            print(f"You have {warnings} warnings left")
        case "end_game_win":
            print(f"Congratulations, you won!\nYour total score is {score}")
        case "end_game_lose":
            print(f"Sorry, you ran out of guesses: {secret_word}")


def is_letter_guessed(letter, letters):
    """
    letter: guessed letter,
    assumes the letter is alpha character
    returns: True if letter was guessed, otherwise false
    """
    count = 0
    for i in range(len(letters)):
        if letter == letters[i]:
            count += 1

    if count > 1:
        return True
    else:
        return False


def is_consonant(letter):
    """
    letter: singular letter,
    returns: True if the letter is a consonant
    """
    vowels = "aeio"
    if letter not in vowels:
        return True
    else:
        return False


def compute_score(guesses, secret_word):
    """
    assumes guesses is a string and secret_word is a string,
    returns: score
    """
    secret_word = len(set(secret_word))
    return guesses * secret_word


def hangman(secret_word):
    """
    This is a combination of f hangman and f hangman with hints
    secret_word: string the secret word to guess,
    guesses: the user guessed letters,
    returns: None,
    
    """
    guesses = 6
    warnings = 3
    letters = []


    output_to_console(key="welcome")
    output_to_console(key="thinking", secret_word=secret_word)
    output_to_console(key="dash")

    while True:

        if is_word_guessed(secret_word, letters):
            output_to_console(
                key="end_game_win", score=compute_score(guesses, secret_word)
            )
            break

        output_to_console(key="warning", warnings=warnings)
        output_to_console(key="guesses", guesses=guesses)
        output_to_console(key="available_letters", letters=letters)

        if guesses < 1:
            output_to_console(key="end_game_lose", secret_word=secret_word)
            break

        letter = input("Please guess a letter: ")
        letter = letter.lower()
        
        if not letter.isalpha():
            if letter != "*":
                if warnings != 0:
                    warnings -= 1
                else:
                    guesses -= 1
                output_to_console(key="invalid_guess", warnings=warnings)
                output_to_console(key="dash")
            elif letter == "*":
                if len(letters) > 0:
                    actual_words = possible_matches(get_guessed_word(secret_word,letters))
                
                    if len(actual_words) == 0:
                        print("No Matches Found...")
                        output_to_console(key="dash")
                    else:
                        print("Possible words matches are: \n", actual_words)
                        output_to_console(key="dash")
                else:
                    print("To receive a hint you must guess at least 1 letter")
                    output_to_console(key="dash")
        else:
            letters.append(letter)

            if is_letter_guessed(letter, letters):
                if (
                    is_letter_guessed(letter, letters)
                    and is_consonant(letter)
                    and letter not in secret_word
                    and warnings == 0
                ) or warnings == 0:
                    guesses -= 1
                else:
                    warnings -= 1
                output_to_console(
                    key="already_guess",
                    secret_word=secret_word,
                    letters=letters,
                    warnings=warnings,
                )
                output_to_console(key="dash")
            else:
                if letter in secret_word:
                    output_to_console(
                        key="good_guess", secret_word=secret_word, letters=letters
                    )
                    output_to_console(key="dash")
                else:
                    if is_consonant(letter):
                        guesses -= 1
                    else:
                        guesses -= 2
                    output_to_console(
                        key="bad_guess", secret_word=secret_word, letters=letters
                    )
                    output_to_console(key="dash")

def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word, assume that "_ " contains no whitespace
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """ 
    if len(my_word) != len(other_word):
        return False
    else:
        for i in range(len(my_word)):
            if my_word[i] != other_word[i] and my_word[i] != '_':
                return False
        return True

def possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: actual_words list of words that match my_word, that might be any alpha char or *
    goal/understanding: 
    0.1
    match the guessed word with words in list return the possible matches 
    strategy:
    0.1
    use bisection search to match them by length
    use bisection to match by each letter len 
    accumulate possibile words 
    use enumeration search on possible words to get actual words
    """
    all_words = wordlist[:]
    my_word = "".join(my_word.split())
    high = len(all_words)
    low = 0
    precision = list()
    actual_words = list()
    iterations = 0

    while True:
        
        iterations += 1
        average = int(abs(high + low)/2)
        print('high', high, 'low', low, 'average', average)
        if len(precision) >= int(len(my_word)/2):
            possible_words = all_words[abs(average - 200) : abs(average + 200)][:]

            for i in range(len(possible_words)):
                if match_with_gaps(my_word, possible_words[i]):
                    actual_words.append(possible_words[i])
            return actual_words

        elif len(all_words[average]) > len(my_word):
            high = average
        elif len(all_words[average]) < len(my_word):
            low = average
        else:
            word = all_words[average][:]

            for i in range(len(my_word)):
                if my_word[i] < word[i] and my_word[i] != '_':
                    high = average 
                    break
                elif my_word[i] > word[i] and my_word[i] != '_':
                    low = average
                    break
                elif my_word[i] == word[i] and my_word[i] != '_':
                    precision.append(word[i])  

if __name__ == "__main__":
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)
