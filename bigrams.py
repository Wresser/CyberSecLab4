import sys
import os
import string
import numpy as np
import pandas as pd

file_name = sys.argv[1]

bigrams = dict()
with open(file_name, encoding="utf-8") as f:
    text = f.read()
    text = text.translate(str.maketrans('', '', string.punctuation))   # remove punctuation
    text = text.replace(" ", "")
    text_len = len(text) - 1
    for i in range(len(text)):
        try:
            b = text[i:i+2]
            if b in bigrams:
                bigrams[b] += 1 # increment if exists
            else:
                bigrams[b] = 1  # initiate if new
        except:
            break

rows_list = []
for letter in bigrams:
    row = {}
    row.update(Bigram = letter, Count = bigrams[letter],Frequency = bigrams[letter] / text_len)
    rows_list.append(row)

frequencies = pd.DataFrame(rows_list)
frequencies.to_csv(f"{os.path.splitext(file_name)[0]}_bigrams.csv")

print(f"Analysis outputed to {os.path.splitext(file_name)[0]}_bigrams.csv")