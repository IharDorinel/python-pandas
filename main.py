import pandas as pd

df = pd.read_csv('football_players_value_dataset.csv')
print(df.head())
print(df.info())
print(df.describe())

dfs = pd.read_csv('dz.csv')
print(dfs.head())

group = dfs.groupby('City')['Salary'].mean()
print(group)