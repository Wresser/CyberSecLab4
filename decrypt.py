import sys
import string

alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
alphabet += alphabet.upper()
alphabet += ' '
m = len(alphabet)

def inverse(a):
    return pow(a, m-2, m)

def affine_decrypt(cypher, key):
    text = ""
    for c in cypher:
        char_num = alphabet.index(c)
        text_num = (inverse(key[0]) * (char_num - key[1])) % m
        text += alphabet[text_num]
    return text

cypher = sys.argv[1]
key = (int(sys.argv[2]), int(sys.argv[3]))

affine_decrypted_text = affine_decrypt(cypher, key)
print(affine_decrypted_text)