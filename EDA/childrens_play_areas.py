import pandas as pd
import seaborn as sns

df = pd.read_csv('../OpenDataBCN/City/children_play_areas.csv', sep=';')

#group by district
df = df.groupby(['district_code', 'district_name']).size().reset_index(name='children_play_areas')
#df.to_csv('../OpenDataBCN/Processed/children_play_areas_district.csv', index=False)

#plot the data sorted by number of play areas
# sns.set(style="whitegrid")
# ax = sns.barplot(x="district_name", y="children_play_areas", data=df.sort_values(by='children_play_areas', ascending=False))
# ax.set_xticklabels(ax.get_xticklabels(), rotation=25, fontsize=7)
# ax.set_title('Number of children play areas per district')
# ax.set_xlabel('District')
# ax.set_ylabel('Number of play areas')
# ax.figure.savefig('children_play_areas_by_district.png')

# # group by neighbourhood
# df = df.groupby(['district_code', 'district_name','neighbourhood_code', 'neighbourhood_name', ]).size().reset_index(name='children_play_areas')
# df.to_csv('../OpenDataBCN/Processed/children_play_areas_neighbourhood.csv', index=False)
#
# # plot the data
# sns.set(style="whitegrid")
# ax = sns.barplot(x="neighbourhood_name", y="children_play_areas", data=df.sort_values(by='children_play_areas', ascending=False).head(10))
# ax.set_xticklabels(ax.get_xticklabels(), rotation=25, fontsize=7)
# ax.set_title('Number of children play areas per neighbourhood (top 10)')
# ax.set_xlabel('Neighbourhood')
# ax.set_ylabel('Number of play areas')
# ax.figure.savefig('children_play_areas_by_neighbourhood_top_10.png')


