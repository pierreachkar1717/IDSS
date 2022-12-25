import pandas as pd

df = pd.read_csv('../../data/Population/2022_nationality_sex.csv', sep=';')

#Districts
#group by district & sex
df = df.groupby(['district_code', 'district_name', 'nationality'])

#in each district, sum the number of people of each nationality
df = df['number'].sum().reset_index()

#drop Total or Espanya
df = df[df['nationality'].isin(['Total', 'Espanya']) == False]

df.sort_values(by='number', ascending=False, inplace=True)

#top 5 nationalities
df = df.groupby('district_code').head(5)

df = df.sort_values(by='district_code')

#new column with the name of the top 5 nationalities for each district
df['top_5_nationalities'] = df.groupby('district_code')['nationality'].transform(lambda x: ', '.join(x))

#remove the duplicates
df.drop_duplicates(subset=['district_code', 'district_name'], keep='first', inplace=True)

df = df[['district_code', 'district_name', 'top_5_nationalities']]

df.reset_index(drop=True, inplace=True)

df.to_csv('../data/Processed/2022_top_5_foreign_nationalities_district.csv', index=False)



# #Neighbourhoods
#
# # group by neighbourhood
# df = df.groupby(['district_code', 'district_name', 'neighbourhood_code', 'neighbourhood_name', 'nationality'])
#
# #in each neighbourhood, sum the number of people
# df = df['number'].sum().reset_index()
#
# #Drop Total or Espanya
# df = df[df['nationality'].isin(['Total', 'Espanya']) == False]
#
# df.sort_values(by='number', ascending=False, inplace=True)
#
# #top 5 nationalities
# df = df.groupby('neighbourhood_code').head(5)
#
# df = df.sort_values(by='neighbourhood_code')
#
# #new column with the name of the top 5 nationalities for each neighbourhood
# df['top_5_nationalities'] = df.groupby('neighbourhood_code')['nationality'].transform(lambda x: ', '.join(x))
#
# #remove the duplicates
# df.drop_duplicates(subset=['neighbourhood_code', 'neighbourhood_name'], keep='first', inplace=True)
#
# df = df[['district_code', 'district_name', 'neighbourhood_code', 'neighbourhood_name', 'top_5_nationalities']]
#
# df.reset_index(drop=True, inplace=True)
#
# df.to_csv('../data/Processed/2022_top_5_foreign_nationalities_neighbourhood.csv', index=False)
#
#
#
#
#






