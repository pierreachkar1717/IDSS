import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


df_q = pd.read_csv('/Users/pierreachkar/Downloads/neighborhood_finder/src/test.csv')
df_data = pd.read_csv('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/labeled_num.csv')

# use neighborhood_code as index
df_data = df_data.set_index('neighbourhood_code')

# drop the columns that are not needed
df_data = df_data.drop(['district_code', 'district_name', 'neighbourhood_name'], axis=1)

# use user_name as index
df_q = df_q.set_index('user_id')

# calculate the cosine similarity and store it in a new column in df_data
df_data['similarity'] = cosine_similarity(df_data, df_q)

# sort the dataframe by similarity
df_data = df_data.sort_values(by=['similarity'], ascending=False)

# save the top 10 results
df_data.head(10).to_csv('/Users/pierreachkar/Downloads/neighborhood_finder/src/rec_top10_results.csv', index=True)



df_res = pd.read_csv('/Users/pierreachkar/Downloads/neighborhood_finder/src/quetionary_and_recommendation/rec_top10_results.csv')
df_info = pd.read_csv('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table_all_info.csv')

# merge the two dataframes on neighborhood_code with left join
df_merged = pd.merge(df_res, df_info, on=['neighbourhood_code'], how='left')

# save the merged dataframe
df_merged.to_csv('/Users/pierreachkar/Downloads/neighborhood_finder/src/quetionary_and_recommendation/rec_top10_all_info.csv', index=False)



