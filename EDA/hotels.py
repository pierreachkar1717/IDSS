import pandas as pd
import seaborn as sns

df = pd.read_csv('../OpenDataBCN/City/hotels.csv', sep=';')

# Group by district
#df = df.groupby(['district_code', 'district_name']).size().reset_index(name='hotels')
#df.to_csv('../OpenDataBCN/Processed/hotels_district.csv', index=False)

# Plot the data
# sns.set(style="whitegrid")
# ax = sns.barplot(x="district_name", y="hotels", data=df.sort_values(by='hotels', ascending=False))
# ax.set_xticklabels(ax.get_xticklabels(), rotation=25, fontsize=7)
# ax.set_title('Number of hotels per district')
# ax.set_xlabel('District')
# ax.set_ylabel('Number of hotels')
# ax.figure.savefig('hotels_by_district.png')

# Group by neighbourhood
#df = df.groupby(['district_code', 'district_name', 'neighbourhood_code', 'neighbourhood_name']).size().reset_index(name='hotels')
#df.to_csv('../OpenDataBCN/Processed/hotels_neighbourhood.csv', index=False)

# Plot the data
# sns.set(style="whitegrid")
# ax = sns.barplot(x="neighbourhood_name", y="hotels", data=df.sort_values(by='hotels', ascending=False).head(10))
# ax.set_xticklabels(ax.get_xticklabels(), rotation=25, fontsize=7)
# ax.set_title('Number of hotels per neighbourhood (top 10)')
# ax.set_xlabel('Neighbourhood')
# ax.set_ylabel('Number of hotels')
# ax.figure.savefig('hotels_by_neighbourhood_top_10.png')


