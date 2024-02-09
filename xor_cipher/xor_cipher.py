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

def key_generator(plaintext):
    key = (''.join(random.choices(string.ascii_letters, k = len(plaintext))))
    return algorithm(plaintext, key)
