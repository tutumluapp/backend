import pandas as pd

df = pd.read_csv('gtin_input.csv')  # Give the input file name here
df = df[df['gtin'] != 'Belirtilmemis']
df['category_id'] = 1  # Give category id here
df = df[['gtin', 'name', 'category_id']]
df = df.drop(['price', 'url'], axis=1, errors='ignore')
df.to_csv('modified_file.csv', index=False)
