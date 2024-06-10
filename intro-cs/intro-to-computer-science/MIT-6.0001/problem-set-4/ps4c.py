# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: 15+ hours
import random
from ps4a import get_permutations

def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    Returns: a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    """ print("Loading word list from file...") """
    inFile = open(file_name, 'r')
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    """ print("  ", len(wordlist), "words loaded.") """
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation
    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    Returns: True if word is in word_list, False otherwise
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

WORDLIST_FILENAME = 'words.txt'
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
        text (string): the message's text
        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words("words.txt")
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        Returns: a COPY of self.valid_words
        '''
        return load_words("words.txt").copy()
                
    def build_transpose_dict(self, vowels_permutation=random.choice(get_permutations(VOWELS_LOWER))):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"
        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        transpose_dict = dict()
        for i in range(len(VOWELS_LOWER)):
            transpose_dict[VOWELS_LOWER[i]] = vowels_permutation[i]
            transpose_dict[VOWELS_UPPER[i]] = vowels_permutation[i].upper()
        for i in range(len(CONSONANTS_LOWER)):
            transpose_dict[CONSONANTS_LOWER[i]] = CONSONANTS_LOWER[i]
            transpose_dict[CONSONANTS_UPPER[i]] = CONSONANTS_UPPER[i]
        return transpose_dict

    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        Returns: a transposed version of the message text, based 
        on the dictionary
        '''
        transposed_message = ""
        for i in range(len(self.message_text)):
            try:
                transpose_dict[self.message_text[i]]
            except KeyError:
                transposed_message += self.message_text[i]
            else:
                transposed_message += transpose_dict[self.message_text[i]]
        return transposed_message

class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object
        text (string): the encrypted message text
        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        Returns: the best decrypted message 
        Goal:
        Take a string permite vowels to find the correct word or string
        Strategy:
        get permutation list 
        iterate thru each permutation
        apply it to the looked up text 
        if application is true pop the needed element
        when looked up text len is zero quit
        implimentation:
        evaluation:
        '''
        permutations_list = get_permutations(VOWELS_LOWER)
        potentially_decrypted_string = ""
        decrypted_list = list()
        valid_words = self.get_valid_words()
        message_text_copy = self.message_text

        for i in range(len(permutations_list)):
            transpose_dict = self.build_transpose_dict(permutations_list[i])
            potentially_decrypted_string = self.apply_transpose(transpose_dict)
            potentially_decrypted_list = potentially_decrypted_string.split()
            for j in range(len(potentially_decrypted_list)):
                if potentially_decrypted_list[j].lower() in valid_words:
                    decrypted_list.insert(j, potentially_decrypted_list[j])
                    updated_self_message = self.message_text.split(" ")
                    updated_self_message.remove(updated_self_message[j])
                    self.message_text = " ".join(updated_self_message)
            if len(self.message_text) == 0:
                break
        decrypted_message = "" 
        for i in range(len(decrypted_list)):
            decrypted_message += decrypted_list[i]
            if len(decrypted_list) - 1 == i:
                if message_text_copy[-1].isalpha() == False:
                    decrypted_message += " "
                    decrypted_message += message_text_copy[-1]
            else:
                decrypted_message += " " 
        return (decrypted_message, message_text_copy)

if __name__ == '__main__':
    message = SubMessage("Hello World !")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld !")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    print('------------------------------------')
    message = SubMessage("Hello World")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    print('------------------------------------')
    message = SubMessage("Hello")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())

