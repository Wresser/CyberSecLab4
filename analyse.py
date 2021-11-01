import collections
import sys
import os
import string
import numpy as np
import pandas as pd

file_name = sys.argv[1]

c = None
with open(file_name, encoding="utf-8") as f:
    text = f.read()
    text_len = len(text)
    text = text.translate(str.maketrans('', '', string.punctuation))   # remove punctuation
    c = collections.Counter(text)

rows_list = []
for letter in c:
    row = {}
    row.update(Letter = letter, Count = c[letter],Frequency = c[letter] / text_len)
    rows_list.append(row)

frequencies = pd.DataFrame(rows_list)
frequencies.to_csv(f"{os.path.splitext(file_name)[0]}_letters.csv")

print(f"Analysis outputed to {os.path.splitext(file_name)[0]}_letters.csv")