from exceptions import BadKeyLengthError
from exceptions import UnsupportedCharacterError
import random
import string

def algorithm(plaintext, key):
    cypher_text = ""
    for i in range(len(plaintext)):
        if plaintext[i] == " ":
            cypher_text += " "
        else:
            cypher_text += chr((ord(plaintext[i]) ^ ord(key[i]) + 65))
    return cypher_text

def char_checker(plaintext, key):
    for char in plaintext:
        if (0 <= ord(char) < 32 or 32 < ord(char) < 65 or
            ord(char) > 122 or 90 < ord(char) < 97):
            raise UnsupportedCharacterError
    return algorithm(plaintext, key)

def key_generator(plaintext):
    key = (''.join(random.choices(string.ascii_letters, k = len(plaintext))))
    return char_checker(plaintext, key)
