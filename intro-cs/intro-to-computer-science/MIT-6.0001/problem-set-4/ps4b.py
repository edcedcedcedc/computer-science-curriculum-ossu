# Problem Set 4B
# Name: Eurodollarclub
# Collaborators: None
# Time Spent: x:xx

import string


### HELPER CODE ###
def load_words(file_name):
    """
    file_name (string): the name of the file containing
    the list of words to load
    Returns: a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, "r")
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(" ")])
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def is_word(word_list, word):
    """
    Determines if word is a valid word, ignoring
    capitalization and punctuation
    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    Returns: True if word is in word_list, False otherwise
    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


WORDLIST_FILENAME = "words.txt"


class Message(object):
    def __init__(self, text):
        """
        Initializes a Message object
        text (string): the message's text
        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        self.message_text = text
        self.valid_words = load_words("words.txt")

    def get_message_text(self):
        """
        Used to safely access self.message_text outside of the class
        Returns: self.message_text
        """
        return self.message_text

    def get_valid_words(self):
        """
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        Returns: a COPY of self.valid_words
        """
        return self.valid_words.copy()

    def build_shift_dict(self, shift):
        """
        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26
        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        """
        assert 0 <= shift < 26 or shift == None, f"0 <={shift}< 26 or None"
        letters_list_lowercase = list(string.ascii_lowercase)
        letters_list_uppercase = list(string.ascii_uppercase)
        encryption_dict = dict()
        for k in range(len(letters_list_lowercase)):
            shift_k = k + shift
            if shift_k > 25:
                shift_k = abs(shift_k - 26)
            encryption_dict[letters_list_lowercase[k]] = letters_list_lowercase[shift_k]
            encryption_dict[letters_list_uppercase[k]] = letters_list_uppercase[shift_k]
        return encryption_dict

    def apply_shift(self, shift):
        """
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26
        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        """
        shift_dict = self.build_shift_dict(shift)
        shifted_message = ""

        for i in self.message_text:
            for k, v in shift_dict.items():
                if i == k:
                    shifted_message += v
                elif i == " ":
                    shifted_message += " "
                    break
        return shifted_message


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        """
        Initializes a PlaintextMessage object
        text (string): the message's text
        shift (integer): the shift associated with this message
        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)
        """
        assert 0 <= shift < 26
        assert isinstance(text, str)
        self.shift = shift
        self.message_text = text
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        """
        Used to safely access self.shift outside of the class
        Returns: self.shift
        """
        return self.shift

    def get_encryption_dict(self):
        """
        Used to safely access a copy self.encryption_dict outside of the class
        Returns: a COPY of self.encryption_dict
        """

        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        """
        Used to safely access self.message_text_encrypted outside of the class
        Returns: self.message_text_encrypted
        """
        return self.message_text_encrypted

    def change_shift(self, shift):
        """
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift.
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26
        Returns: nothing
        """
        self.shift = shift


class CiphertextMessage(Message):
    def __init__(self, text):
        """
        Initializes a CiphertextMessage object
        text (string): the message's text
        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        self.message_text = text
        self.valid_words = load_words("words.txt")

    def decrypt_message(self):
        """
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one.
        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        """
        comparable_dict = dict()
        for j in range(0, 26):
            v = 0
            comparable_dict[f"{j}"] = v
            potentially_decrypted_message = self.apply_shift(j).split()
            for i in range(len(potentially_decrypted_message)):
                if potentially_decrypted_message[i] in self.valid_words:
                    v += 1
                    comparable_dict[f"{j}"] = v
        key = int(
            list(
                filter(
                    lambda item: (
                        item
                        if item[1] == max(comparable_dict.values(), key=lambda v: v)
                        else None
                    ),
                    comparable_dict.items(),
                )
            )[0][0]
        )
        return (key, self.apply_shift(key))



decrypt = CiphertextMessage("Xoqy Tzcfsm wg o amhvwqoz qvofoqhsf qfsohsr cb hvs gdif ct o acasbh hc vszd qcjsf ob wbgittwqwsbhzm dzobbsr voqy. Vs vog pssb fsuwghsfsr tcf qzoggsg oh AWH hkwqs pstcfs, pih vog fsdcfhsrzm bsjsf doggsr oqzogg. Wh vog pssb hvs hforwhwcb ct hvs fsgwrsbhg ct Sogh Qoadig hc psqcas Xoqy Tzcfsm tcf o tsk bwuvhg soqv msof hc sriqohs wbqcawbu ghirsbhg wb hvs komg, asobg, obr shvwqg ct voqywbu.")
print(decrypt.decrypt_message())


if __name__ == "__main__":
    plaintext = PlaintextMessage('abc', 1)
    print('Expected Output:', 'bcd')
    print('Actual Output:', plaintext.get_message_text_encrypted())