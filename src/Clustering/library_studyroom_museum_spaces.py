from clustering import optimal_clusters_number, cluster_and_plot
import pandas as pd

# Load your data into a pandas DataFrame
df = pd.read_csv('../../data/Processed/neighbourhood/library_studyroom_museum_spaces_neighbourhood.csv')

# Choose the column/columns in your data that you want to use for clustering
cols = ['library_studyroom_museum_spaces']

# First: Call the optimal_clusters_number function to determine the optimal number of clusters for your data
# Decide on the best number of clusters for your data by considering both plots
# The elbow method plot is useful for finding the point where the decrease in SSE starts to level off (The bend in the curve)
# The silhouette score plot is useful for finding the number of clusters with the highest score
# If the two plots do not agree on the same number of clusters, you need to find a compromise solution by selecting a number of clusters
# that is recommended by the elbow method plot and also has a relatively high silhouette score

#optimal_clusters_number(df, cols, 20)

# Second: Call the cluster_and_plot function to cluster your data and plot the results
cluster_and_plot(df, cols, 2, 'library_studyroom_museum_spaces')