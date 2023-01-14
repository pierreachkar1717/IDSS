import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('../../data/processed/joined_data/labeled_num.csv')
df = df.set_index('neighbourhood_code')
df = df.drop(["district_code", "district_name", "neighbourhood_name"], axis=1)

user_input = pd.read_csv("../../data/user_input/user_input.csv")
user_input = user_input.set_index("user_id")

df['cosine_similarity'] = cosine_similarity(df, user_input)

# calculate the adjusted cosine similarity
df['cosine_similarity'] = df['cosine_similarity'] / df['cosine_similarity'].max()

df = df.sort_values(by=['cosine_similarity'], ascending=False)
print(df[["cosine_similarity"]].head(10))