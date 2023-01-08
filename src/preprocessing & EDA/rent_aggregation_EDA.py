import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('/data/City/rent_price.txt', sep=',')

#keep only the rows where year is 2020 and type is 'average rent'
df = df[(df['year'] == 2021) & (df['type'] == 'average rent (euro/month)')]

df = df[['neighbourhood_name', 'district_name', 'price']]
df = df.dropna()

#group by district
#df = df.groupby(['district_name']).mean().reset_index()

#df.to_csv('../../data/Processed/avg_rent_price_2021_district.csv', index=False)

#plot the data
# sns.set(style="whitegrid")
# ax = sns.barplot(x="district_name", y="price", data=df.sort_values(by='price', ascending=False))
# ax.set_xticklabels(ax.get_xticklabels(), rotation=25, fontsize=7)
# ax.set_title('Average rent price per district')
# ax.set_xlabel('District')
# ax.set_ylabel('Average rent price (euro/month)')
# ax.figure.savefig('avg_rent_price_2021_district.png')

#groupy by neighbourhood
df = df.groupby(['neighbourhood_name', 'district_name']).mean().reset_index()

df.to_csv('../../data/Processed/avg_rent_price_2021_neighbourhood.csv', index=False)

#plot the data
sns.set(style="whitegrid")
ax = sns.barplot(x="neighbourhood_name", y="price", data=df.sort_values(by='price', ascending=False).head(10))
ax.set_xticklabels(ax.get_xticklabels(), rotation=25, fontsize=7)
ax.set_title('Average rent price per neighbourhood (top 10)')
ax.set_xlabel('Neighbourhood')
ax.set_ylabel('Average rent price (euro/month)')
ax.figure.savefig('avg_rent_price_2021_neighbourhood_top_10.png')
