import sys
import os
import string
import numpy as np
import pandas as pd

file_name = sys.argv[1]

trigrams = dict()
with open(file_name, encoding="utf-8") as f:
    text = f.read()
    text = text.translate(str.maketrans('', '', string.punctuation))   # remove punctuation
    text = text.replace(" ", "")
    text_len = len(text) - 2
    for i in range(len(text)):
        try:
            t = text[i:i+3]
            if t in trigrams:
                trigrams[t] += 1 # increment if exists
            else:
                trigrams[t] = 1  # initiate if new
        except:
            break

rows_list = []
for letter in trigrams:
    row = {}
    row.update(Trigram = letter, Count = trigrams[letter],Frequency = trigrams[letter] / text_len)
    rows_list.append(row)

frequencies = pd.DataFrame(rows_list)
frequencies.to_csv(f"{os.path.splitext(file_name)[0]}_trigrams.csv")

print(f"Analysis outputed to {os.path.splitext(file_name)[0]}_trigrams.csv")