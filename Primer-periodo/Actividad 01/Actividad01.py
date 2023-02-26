import pandas as pd


with open('Primer-periodo/Actividad 01/data01.txt') as file1:
    lines = file1.readlines()

data = pd.Series(lines)
print(data.value_counts())