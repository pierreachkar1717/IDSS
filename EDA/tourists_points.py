import pandas as pd
import seaborn as sns

df = pd.read_csv('../OpenDataBCN/City/tourist_points.csv', sep=';')

# Group by district
# df = df.groupby(['district_code', 'district_name']).size().reset_index(name='tourists_points')
# df.to_csv('../OpenDataBCN/Processed/tourist_points_district.csv', index=False)
#
# #Plot the data
# sns.set(style="whitegrid")
# ax = sns.barplot(x="district_name", y="tourists_points", data=df.sort_values(by='tourists_points', ascending=False))
# ax.set_xticklabels(ax.get_xticklabels(), rotation=25, fontsize=7)
# ax.set_title('Number of tourists points per district')
# ax.set_xlabel('District')
# ax.set_ylabel('Number of tourists points')
# ax.figure.savefig('tourists_points_by_district.png')

#Group by neighbourhood
# df = df.groupby(['district_code', 'district_name', 'neighbourhood_code', 'neighbourhood_name']).size().reset_index(name='tourists_points')
# df.to_csv('../OpenDataBCN/Processed/tourist_points_neighbourhood.csv', index=False)
#
# #Plot the data
# sns.set(style="whitegrid")
# ax = sns.barplot(x="neighbourhood_name", y="tourists_points", data=df.sort_values(by='tourists_points', ascending=False).head(10))
# ax.set_xticklabels(ax.get_xticklabels(), rotation=25, fontsize=7)
# ax.set_title('Number of tourists points per neighbourhood (top 10)')
# ax.set_xlabel('Neighbourhood')
# ax.set_ylabel('Number of tourists points')
# ax.figure.savefig('tourists_points_by_neighbourhood_top_10.png')
