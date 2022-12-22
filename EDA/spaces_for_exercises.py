import pandas as pd
import seaborn as sns

df = pd.read_csv('/Users/pierreachkar/Downloads/neighborhood_finder/OpenDataBCN/City/spaces_for_exercising.csv', sep=';')

# Group by district
# df = df.groupby(['district_code', 'district_name']).size().reset_index(name='spaces_for_exercising')
# df.to_csv('/Users/pierreachkar/Downloads/neighborhood_finder/OpenDataBCN/Processed/spaces_for_exercising_district.csv', index=False)
#
# # # Plot the data
# sns.set(style="whitegrid")
# ax = sns.barplot(x="district_name", y="spaces_for_exercising", data=df.sort_values(by='spaces_for_exercising', ascending=False))
# ax.set_xticklabels(ax.get_xticklabels(), rotation=25, fontsize=7)
# ax.set_title('Number of spaces for exercising per district')
# ax.set_xlabel('District')
# ax.set_ylabel('Number of spaces for exercising')
# ax.figure.savefig('spaces_for_exercising_by_district.png')

# Group by neighbourhood
df = df.groupby(['district_code', 'district_name', 'neighbourhood_code', 'neighbourhood_name']).size().reset_index(name='spaces_for_exercising')
df.to_csv('/Users/pierreachkar/Downloads/neighborhood_finder/OpenDataBCN/Processed/spaces_for_exercising_neighbourhood.csv', index=False)

#Plot the data
sns.set(style="whitegrid")
ax = sns.barplot(x="neighbourhood_name", y="spaces_for_exercising", data=df.sort_values(by='spaces_for_exercising', ascending=False).head(10))
ax.set_xticklabels(ax.get_xticklabels(), rotation=25, fontsize=7)
ax.set_title('Number of spaces for exercising per neighbourhood (top 10)')
ax.set_xlabel('Neighbourhood')
ax.set_ylabel('Number of spaces for exercising')
ax.figure.savefig('spaces_for_exercising_by_neighbourhood_top_10.png')

