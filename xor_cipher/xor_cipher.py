from exceptions import BadKeyLengthError
from exceptions import UnsupportedCharacterError

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
    for char in key:
        if (0 <= ord(char) < 32 or 32 < ord(char) < 65 or
            ord(char) > 122 or 90 < ord(char) < 97):
            raise UnsupportedCharacterError
    return algorithm(plaintext, key)

def len_checker(plaintext, key):
    if len(key) < len(plaintext):
        raise BadKeyLengthError
    return char_checker(plaintext, key)
    
print(len_checker("Lukeysus", "Lithuania"))
