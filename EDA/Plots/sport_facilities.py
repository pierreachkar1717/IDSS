import pandas as pd
import seaborn as sns

df = pd.read_csv('/Users/pierreachkar/Downloads/neighborhood_finder/OpenDataBCN/City/sports_facilities.csv', sep=';')


# Group by district
# df = df.groupby(['district_code', 'district_name']).size().reset_index(name='sport_facilities')
# df.to_csv('/Users/pierreachkar/Downloads/neighborhood_finder/OpenDataBCN/Processed/sport_facilities_district.csv', index=False)
#
# # Plot the data
# sns.set(style="whitegrid")
# ax = sns.barplot(x="district_name", y="sport_facilities", data=df.sort_values(by='sport_facilities', ascending=False))
# ax.set_xticklabels(ax.get_xticklabels(), rotation=25, fontsize=7)
# ax.set_title('Number of sport facilities per district')
# ax.set_xlabel('District')
# ax.set_ylabel('Number of sport facilities')
# ax.figure.savefig('sport_facilities_by_district.png')

# Group by neighbourhood
# df = df.groupby(['district_code', 'district_name', 'neighbourhood_code', 'neighbourhood_name']).size().reset_index(name='sport_facilities')
# df.to_csv('/Users/pierreachkar/Downloads/neighborhood_finder/OpenDataBCN/Processed/sport_facilities_neighbourhood.csv', index=False)
#
# #Plot the data
# sns.set(style="whitegrid")
# ax = sns.barplot(x="neighbourhood_name", y="sport_facilities", data=df.sort_values(by='sport_facilities', ascending=False).head(10))
# ax.set_xticklabels(ax.get_xticklabels(), rotation=25, fontsize=7)
# ax.set_title('Number of sport facilities per neighbourhood (top 10)')
# ax.set_xlabel('Neighbourhood')
# ax.set_ylabel('Number of sport facilities')
# ax.figure.savefig('sport_facilities_by_neighbourhood_top_10.png')
#
