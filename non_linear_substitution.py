from exceptions import UnsupportedCharacterError

#This function assumes that the given text is a single word.
#No spaces, digits, or non-English characters will be 
#accepted as input.

def non_linear_encoder(message, key = 'secret'):
    alphabet_dict = {letter: '' for letter in range(26)}

    occured_chars = []

    for character in key:
        if ord(character) < 97 or ord(character) > 122:
            raise UnsupportedCharacterError
        elif character not in occured_chars:
            occured_chars.append(character)
        else:
            continue 
    
    key = ''.join(occured_chars)
    
    for characters in range(len(key)):
        alphabet_dict[characters] = key[characters]

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = list(alphabet)

    for letter in range(len(alphabet) - 1, -1, -1):
        if alphabet[letter] in occured_chars:
            alphabet.pop(letter)
    
    for i in range(len(key), len(alphabet_dict)):
        alphabet_dict[i] = alphabet[i - len(key)]

    message = list(message)

    for character in range(len(message)):
        message[character] = alphabet_dict[ord(message[character]) - 97]

    return ''.join(message)

#I will follow up and document this on Confluence.
#This took me way too long.
