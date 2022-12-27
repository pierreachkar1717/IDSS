"""
This code defines two functions: optimal_clusters_number and cluster_and_plot.

The optimal_clusters_number function determines the optimal number of clusters for a given data frame and set of columns. It uses two methods:

The elbow method plots the sum of squared errors (SSE) for different numbers of clusters.
The silhouette method plots the silhouette score for different numbers of clusters.
The user specifies the maximum number of clusters to test. The function then plots the results of both methods using the Seaborn library and displays the plots. This can help the user choose the best number of clusters for their data.

The cluster_and_plot function clusters the data in a given data frame and set of columns into a specified number of clusters using the K-means algorithm. It then adds a 'cluster' column to the data frame with the cluster label for each data point, sorts the data frame by the cluster labels, and saves the data frame to a CSV file. The function then creates a bar plot showing the data points in the specified columns, grouped by neighborhood and colored by cluster, and saves the plot as a PNG file. The Seaborn library is used to create the plot. This can help the user visualize the clustering results.
"""

import pandas as pd
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

def optimal_clusters_number(data_frame, columns, n):
    """
    optimal_clusters_number(data_frame, column)

    This function determines the optimal number of clusters for a given data frame and column using the elbow method and
     silhouette method. It plots the results of both methods and displays the plots.

    Parameters:
    data_frame (pandas DataFrame): The data frame to be used for clustering.
    columns (list): List of columns in the data frame to be used for clustering.
    n (int): The maximum number of clusters to be tested.

    Returns:
    None
    """

    df = data_frame

    # elbow method
    sse = {}
    for k in range(1, n):
        kmeans = KMeans(n_clusters=k, max_iter=1000).fit(df[columns])
        df["clusters"] = kmeans.labels_
        sse[k] = kmeans.inertia_ # Inertia: Sum of distances of samples to their closest cluster center
    sns.pointplot(x=list(sse.keys()), y=list(sse.values()))
    plt.xlabel("Number of cluster")
    plt.ylabel("SSE")
    plt.show()

    # silhouette method
    silhouette_avg = {}
    for k in range(2, n):
        kmeans = KMeans(n_clusters=k, max_iter=1000).fit(df[columns])
        df["clusters"] = kmeans.labels_
        silhouette_avg[k] = silhouette_score(df[columns], df["clusters"])
    sns.pointplot(x=list(silhouette_avg.keys()), y=list(silhouette_avg.values()))
    plt.xlabel("Number of cluster")
    plt.ylabel("Silhouette score")
    plt.show()

def cluster_and_plot(data, columns, n_clusters, output_file_name):
    """
    cluster_and_plot(data, column, n_clusters)

    This function clusters the data in the specified column of the given data frame into the specified number of clusters
    and adds a 'cluster' column to the data frame with the cluster label for each data point. It then saves the data frame
    to a csv file and creates a bar plot showing the data points in the specified column per neighbourhood, colored by cluster,
    and saves the plot as a png file.

    Parameters:
    data (pandas DataFrame): The data frame containing the data to be clustered.
    columns (list): List of columns in the data frame to be used for clustering.
    n_clusters (int): The number of clusters to create.
    output_file_name (str): The name of the output file.

    Returns:
    None
    """

    # run kmeans on the data
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(data[columns])
    data['cluster'] = kmeans.labels_
    data = data.sort_values(by='cluster')

    #check if the data frame contains a clusters column and drop it if it does
    if 'clusters' in data.columns:
        data = data.drop(columns='clusters')
    data.to_csv('../../data/Processed/clustering/clustered_{}.csv'.format(output_file_name), index=False)

    # plot the data with the clusters and y axis as the number of data points in each cluster, don't show the names of the each neighbourhood on the x axis
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    sns.countplot(x='neighbourhood_name', hue='cluster', data=data)
    plt.xticks(rotation=90)
    plt.xlabel('Neighbourhood')
    plt.ylabel('Number of data points')
    plt.title('Number of data points per neighbourhood per cluster')
    plt.savefig('../../data/Processed/clustering/Plots/clusters_{}.png'.format(output_file_name))


