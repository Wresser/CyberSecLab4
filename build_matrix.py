import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

file_name = sys.argv[1]

data = pd.read_csv(file_name)
data = data.drop(columns=['Unnamed: 0','Count'])

matrix = dict()
for index, row in data.iterrows():
    try:
        first = row["Bigram"][0]
        second = row["Bigram"][1]

        if first in matrix:
            matrix[first][second] = row["Frequency"]
        else:
            matrix[first] = { second : row["Frequency"] }
    except:
        continue

data = pd.DataFrame(matrix)
data = data.fillna(0)

matrix = data.to_numpy()

plt.matshow(matrix)

xs = data.columns.values.tolist()
x_pos = np.arange(len(xs))
plt.xticks(x_pos, xs)

ys = data.index.tolist()
y_pos = np.arange(len(ys))
plt.yticks(y_pos, ys)

plt.show()
