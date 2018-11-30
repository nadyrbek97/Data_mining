import csv

with open('my.csv') as file:

    reader = csv.reader(file, delimiter=',')

    count = 0

    for row in reader:
        print(row)
        count += 1

# print(count)

import pandas as pd
from pandas import DataFrame

Stock_Market = pd.read_csv('my.csv')
df = DataFrame(Stock_Market)
print(df)