import pandas as pd

df = pd.read_csv('../../data/Raw Data/Population/2022_academic_sex.csv', sep=';')

#remove rows where academic level is No record
df = df[df['academic_level'] != 'No record']

# #group the data by district
# df = df.groupby(['district_code', 'district_name', 'academic_level'])
#
# #pivot the data so that each academic level is a column
# df = df['number'].sum().unstack().reset_index()
#
# df.to_csv('../data/Processed/2022_academic_level_district.csv', index=False)

#group the data by neighbourhood
df = df.groupby(['district_code', 'district_name', 'neighbourhood_code', 'neighbourhood_name', 'academic_level'])

#pivot the data so that each academic level is a column
df = df['number'].sum().unstack().reset_index()

df.to_csv('../../data/Processed/neighbourhood/2022_academic_level_neighbourhood.csv', index=False)


