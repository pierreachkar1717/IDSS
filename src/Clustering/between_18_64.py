from clustering import optimal_clusters_number, cluster_and_plot
import pandas as pd


## Each step should be done separately, so comment the other functions out when running one of them.

# Load your data into a pandas DataFrame
#df = pd.read_csv('../../data/Processed/neighbourhood/2022_between_18_64_neighbourhood.csv')

# Choose the column/columns in your data that you want to use for clustering
#cols = ['between_18_64']

# First: Call the optimal_clusters_number function to determine the optimal number of clusters for your data
# Decide on the best number of clusters for your data by considering both plots
# The elbow method plot is useful for finding the point where the decrease in SSE starts to level off (The bend in the curve)
# The silhouette score plot is useful for finding the number of clusters with the highest score
# If the two plots do not agree on the same number of clusters, you need to find a compromise solution by selecting a number of clusters
# that is recommended by the elbow method plot and also has a relatively high silhouette score

#optimal_clusters_number(df, cols, 20)

# Second: Call the cluster_and_plot function to cluster your data and plot the results
#cluster_and_plot(df, cols, 4, 'between_18_64')

# Third: Load the resulting csv file into a new pandas DataFrame and add a new column to the DataFrame
# This column will contain numerical values describing the cluster label for each data point.
df = pd.read_csv('../../data/Processed/clustering/clustered_between_18_64.csv')

# Here 0 means low, 1 means medium and 2 means high
df['label'] = df['cluster'].map({0: 1, 1: 2, 2: 0})

# Or we can still consider adding categorical values to the label column
#df['label_cat'] = df['cluster'].map({0: 'medium_number_library_studyroom', 1: 'high_number_library_studyroom', 2: 'low_number_library_studyroom'})

df.to_csv('../../data/Processed/clustering/labled/labled_between_18_64.csv', index=False)
