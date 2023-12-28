from exceptions import UnsupportedCharacterError

#This function assumes that the given text is a single word.
#No spaces, digits, or non-English characters will be 
#accepted as input.

def non_linear_encoder(message_og, key = 'secret'):
    alphabet_dict = {letter: '' for letter in range(26)}

    occured_chars = []

    #Extract unqiue characters and check that each character qualifies.
    for character in key:
        if ord(character) < 97 or ord(character) > 122:
            raise UnsupportedCharacterError
        elif character not in occured_chars:
            occured_chars.append(character)
        else:
            continue 
    
    key = ''.join(occured_chars)

    occured_values = [] 

    for unique_value in range(len(key)):
        alphabet_dict[unique_value] = key[unique_value]
        occured_values.append(key[unique_value]) 

    alphabet = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']

    for i in range(len(alphabet) - 1, -1, -1):
        if alphabet[i] in occured_values:
            alphabet.pop(i)
        continue 

    for i in range(len(key), len(alphabet_dict)):
        alphabet_dict[i] = alphabet[i - len(key)]

    alphabet = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']

    message_og = list(message_og)

    for i in range(len(message_og)):
        message_og[i] = alphabet_dict[ord(message_og[i]) - 97] 

    return ''.join(message_og) 
 
print(non_linear_encoder('many', 'secret'))