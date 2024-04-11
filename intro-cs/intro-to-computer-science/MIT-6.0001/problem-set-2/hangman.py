# Problem Set 2, hangman.py
# Name: eurodollarclub
# Collaborators:
# Time spent: 90min +

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import sys

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    try:
        inFile = open(WORDLIST_FILENAME, "r")
        # line: string
        line = inFile.readline()
        # wordlist: list of strings
        wordlist = line.split()
        print(len(wordlist), "words loaded.")
        return wordlist
    except:
        print("words not found...")
        sys.exit()


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
# wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    # secret_word = 'apple'
    # letters_guessed = ['a','p','l','u']
    # end = lambda list_of_letters: len(list_of_letters) - 1

    # goal/understanding:
    # return true if all guessed letters match the word otherwise false
    # how to exactly compare, the words might have repeated letters
    # strategy:
    # convert both objects into a set and compare their length
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
    # goal/understanding:
    #
    # strategy:
    # generate a (_ ) sequence based on the secret word len
    # iterate over the guessed word match it with guessed letters
    # if it's there use letter else use underscore and space
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


def output_to_console(key="", secret_word="", guesses=None, letters=[], warnings=None):
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
                f"Oop! That is not a valid letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters)}"
            )
        case "warning":
            print(f"You have {warnings} warnings left")


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """
    guesses = 6
    warnings = 3
    letters = []

    load_words()
    output_to_console(key="welcome")
    output_to_console(key="thinking", secret_word=secret_word)
    output_to_console(key="dash")

    while guesses > 0:
        output_to_console(key="warning", warnings=warnings)
        output_to_console(key="guesses", guesses=guesses)
        output_to_console(key="available_letters", letters=letters)

        letter = input("Please guess a letter: ")
        letters.append(letter)

        if letter.isalpha():
            letter = letter.lower()
            if letter in secret_word:
                output_to_console(
                    key="good_guess", secret_word=secret_word, letters=letters
                )
                output_to_console(key="dash")
            else:
                output_to_console(
                    key="bad_guess", secret_word=secret_word, letters=letters
                )
                guesses -= 1
                output_to_console(key="dash")
        else:
            if warnings is not 0:
                output_to_console(key="invalid_guess")
                warnings -= 1
            else:
                guesses -= 1

        


hangman("apple")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)
    pass
###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)
