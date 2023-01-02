from clustering import optimal_clusters_number, cluster_and_plot
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

## Each step should be done separately, so comment the other functions out when running one of them.

# Load your data into a pandas DataFrame
#df = pd.read_csv('../../data/Processed/neighbourhood/2022_top_5_foreign_nationalities_neighbourhood.csv')

# create new set and save all nationalities in it
# nationalities = set()
# for i in range(len(df)):
#     national = df.iloc[i, 4].split(',')
#     for n in national:
#         nationalities.add(n)

#sort nationalities
#nationalities = sorted(nationalities)

# map each nationality to a float number
# nationalities_map = {}
# for i in range(len(nationalities)):
#     nationalities_map[nationalities[i]] = i

# create a new column in the dataframe to store only the mapped nationalities
#df['mapped_nationalities'] = df['top_5_nationalities'].apply(lambda x: [nationalities_map[n] for n in x.split(',')])

#df.to_csv('../../data/Processed/neighbourhood/2022_top_5_nat_mapped.csv', index=False)

df = pd.read_csv('../../data/Processed/neighbourhood/2022_top_5_nat_mapped.csv')

#convert the mapped nationalities to a list of floats
df['mapped_nationalities'] = df['mapped_nationalities'].apply(lambda x: [float(n) for n in x[1:-1].split(',')])

# unpack list of floats in maooed nationalities to comma separated values
df['mapped_nationalities'] = df['mapped_nationalities'].apply(lambda x: ','.join([str(n) for n in x]))

#convert the mapped nationalities to float numbers
df['mapped_nationalities'] = df['mapped_nationalities'].apply(lambda x: [float(n) for n in x.split(',')])


cols = ['mapped_nationalities']
# First: Call the optimal_clusters_number function to determine the optimal number of clusters for your data
# Decide on the best number of clusters for your data by considering both plots
# The elbow method plot is useful for finding the point where the decrease in SSE starts to level off (The bend in the curve)
# The silhouette score plot is useful for finding the number of clusters with the highest score
# If the two plots do not agree on the same number of clusters, you need to find a compromise solution by selecting a number of clusters
# that is recommended by the elbow method plot and also has a relatively high silhouette score

optimal_clusters_number(df, cols, 20)

#Second: Call the cluster_and_plot function to cluster your data and plot the results
#cluster_and_plot(df, cols, 6, 'top_5_foreign_nationalities')

# Third: Load the resulting csv file into a new pandas DataFrame and add a new column to the DataFrame
# This column will contain numerical values describing the cluster label for each data point.
#df = pd.read_csv('../../data/Processed/clustering/clustered_transportation.csv')

# Here 0 means low, 1 means medium and 2 means high
#df['label'] = df['cluster'].map({0: 0, 1: 1, 2: 2})

# Or we can still consider adding categorical values to the label column
#df['label_cat'] = df['cluster'].map({0: 'medium_number_library_studyroom', 1: 'high_number_library_studyroom', 2: 'low_number_library_studyroom'})

#df.to_csv('../../data/Processed/clustering/labled/labeled_transportation.csv', index=False)
