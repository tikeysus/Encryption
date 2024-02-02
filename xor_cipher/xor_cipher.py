from exceptions import BadKeyLengthError
from exceptions import UnsupportedCharacterError

def char_checker(plaintext, key):
    for char in plaintext:
        if ord(char) < 65 or ord(char) > 122 or 90 < ord(char) < 97:
            raise UnsupportedCharacterError
    for char in key:
        if ord(char) < 65 or ord(char) > 122 or 90 < ord(char) < 97:
            raise UnsupportedCharacterError 

def len_checker(plaintext, key):
    if len(key) < len(plaintext):
        raise BadKeyLengthError
    return char_checker(plaintext, key)
    
