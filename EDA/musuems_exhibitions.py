import pandas as pd
import seaborn as sns

df = pd.read_csv('../OpenDataBCN/City/museums_exhibitions.csv', sep=';')

#group by district
df = df.groupby(['district_code', 'district_name']).size().reset_index(name='number_of_museums_and_exhibitions')
#df.to_csv('../OpenDataBCN/Processed/museums_exhibitions_district.csv', index=False)

#plot the data
# sns.set(style="whitegrid")
# ax = sns.barplot(x="district_name", y="number_of_museums_and_exhibitions", data=df.sort_values(by='number_of_museums_and_exhibitions', ascending=False))
# ax.set_xticklabels(ax.get_xticklabels(), rotation=25, fontsize=7)
# ax.set_title('Number of museums and exhibitions per district')
# ax.set_xlabel('District')
# ax.set_ylabel('Number of museums and exhibitions')
# ax.figure.savefig('museums_exhibitions_by_district.png')


#group by neighbourhood
#df = df.groupby(['district_code', 'district_name', 'neighbourhood_code', 'neighbourhood_name']).size().reset_index(name='number_of_museums_and_exhibitions')
#df.to_csv('../OpenDataBCN/Processed/museums_exhibitions_neighbourhood.csv', index=False)

#plot the data
# sns.set(style="whitegrid")
# ax = sns.barplot(x="neighbourhood_name", y="number_of_museums_and_exhibitions", data=df.sort_values(by='number_of_museums_and_exhibitions', ascending=False).head(10))
# ax.set_xticklabels(ax.get_xticklabels(), rotation=45, fontsize=7)
# ax.set_title('Number of museums and exhibitions per neighbourhood (top 10) - 2021')
# ax.set_xlabel('Neighbourhood')
# ax.set_ylabel('Number of museums and exhibitions')
# ax.figure.savefig('museums_exhibitions_by_neighbourhood_top_10.png')




