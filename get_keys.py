import collections
import sys
import string
import numpy as np
import pandas as pd


text = sys.argv[1]
letters = (sys.argv[2], sys.argv[3])

text_len = len(text)
text = text.translate(str.maketrans('', '', string.punctuation))   # remove punctuation
c = collections.Counter(text)
most_common = c.most_common(2)

print(most_common)

alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
alphabet += alphabet.upper()
alphabet += ' '
m = len(alphabet)

def inverse(a):
    return pow(a, m-2, m)

x1 = alphabet.index(letters[0])
x2 = alphabet.index(letters[1])

y1 = alphabet.index(most_common[0][0])
y2 = alphabet.index(most_common[1][0])

diffy = y2 - y1
diffx = x2 - x1

if diffy < 0:
    diffy = m + diffy
if diffx < 0:
    diffx = -diffx
    diffy = m - diffy

if diffy % diffx != 0:
    a = (diffy * inverse(diffx)) % m
else:
    a = diffy / diffx

b = (y1 - x1 * a) % m

print(f"a = {a}, b = {b}")