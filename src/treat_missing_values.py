import pandas as pd

# read the data
df = pd.read_csv('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table.csv')

# drop rows if district_name is missing
#df = df.dropna(subset=['district_name'])

# drop district_name_x is Desconegut
#df = df[df['district_name_x'] != 'Desconegut']

#replace missing values with 0.0
df.fillna(0.0, inplace=True)

# replace NaN in rent_price with mean
#df['rent_price'] = df['rent_price'].fillna(df['rent_price'].mean())

# save the data
df.to_csv('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table.csv', index=False)
