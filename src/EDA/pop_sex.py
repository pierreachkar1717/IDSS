import pandas as pd

df = pd.read_csv('../../data/Population/2022_age_sex.csv', sep=';')

# group by district & sex
df = df.groupby(['district_code', 'district_name', 'Sex'])

# sum the population by district based on Sex
df = df['number'].sum().reset_index()

# pivot the table
df = df.pivot_table(index=['district_code', 'district_name'], columns='Sex', values='number')
df.rename(columns={'Men': 'number_men', 'Women': 'number_women'}, inplace=True)

# reset the index
df.reset_index(inplace=True)

df.to_csv('../data/Processed/2022_sex_by_district.csv', index=False)


# # group by neighbourhood & sex
# df = df.groupby(['district_code', 'district_name', 'neighbourhood_code', 'neighbourhood_name', 'Sex'])
#
# # sum the population by neighbourhood based on Sex
# df = df['number'].sum().reset_index()
#
# # pivot the table
# df = df.pivot_table(index=['district_code', 'district_name', 'neighbourhood_code', 'neighbourhood_name'], columns='Sex', values='number')
# df.rename(columns={'Men': 'number_men', 'Women': 'number_women'}, inplace=True)
#
# # reset the index
# df.reset_index(inplace=True)
#
# df.to_csv('../data/Processed/2022_sex_by_neighbourhood.csv', index=False)
#









