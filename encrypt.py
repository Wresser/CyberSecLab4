import sys
import string

alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
alphabet += alphabet.upper()
alphabet += ' '
m = len(alphabet)

def affine_encrypt(text, key):
    cypher = ""
    for c in text:
        char_num = alphabet.index(c)
        cypher_num = (key[0] * char_num + key[1]) % m
        cypher += alphabet[cypher_num]
    return cypher

text = sys.argv[1]
text = text.translate(str.maketrans('', '', string.punctuation))   # remove punctuation
key = (int(sys.argv[2]), int(sys.argv[3]))

affine_encrypted_text = affine_encrypt(text, key)
print(affine_encrypted_text)