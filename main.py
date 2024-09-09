import pandas as pd

data = pd.read_csv('dataset.csv', on_bad_lines='skip')

print(data)