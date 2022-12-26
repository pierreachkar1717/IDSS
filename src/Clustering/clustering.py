import pandas as pd
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

def optimal_clusters_number(data_frame, column):
    """
    optimal_clusters_number(data_frame, column)

    This function determines the optimal number of clusters for a given data frame and column using the elbow method and
     silhouette method. It plots the results of both methods and displays the plots.

    Parameters:
    data_frame (pandas DataFrame): The data frame to be used for clustering.
    column (str): The column in the data frame to be used for clustering.

    Returns:
    None
    """

    df = data_frame
    # number of unique neighbourhoods to consider for clustering
    n_neighbourhoods = len(df['neighbourhood_code'].unique())

    # elbow method
    sse = {}
    for k in range(1, n_neighbourhoods):
        kmeans = KMeans(n_clusters=k, max_iter=1000).fit(df[[column]])
        df["clusters"] = kmeans.labels_
        sse[k] = kmeans.inertia_ # Inertia: Sum of distances of samples to their closest cluster center
    sns.pointplot(x=list(sse.keys()), y=list(sse.values()))
    plt.xlabel("Number of cluster")
    plt.ylabel("SSE")
    plt.show()

    # silhouette method
    silhouette_avg = {}
    for k in range(2, n_neighbourhoods):
        kmeans = KMeans(n_clusters=k, max_iter=1000).fit(df[[column]])
        df["clusters"] = kmeans.labels_
        silhouette_avg[k] = silhouette_score(df[[column]], df["clusters"])
    sns.pointplot(x=list(silhouette_avg.keys()), y=list(silhouette_avg.values()))
    plt.xlabel("Number of cluster")
    plt.ylabel("Silhouette score")
    plt.show()

def cluster_and_plot(data, column, n_clusters):
    """
    cluster_and_plot(data, column, n_clusters)

    This function clusters the data in the specified column of the given data frame into the specified number of clusters
    and adds a 'cluster' column to the data frame with the cluster label for each data point. It then saves the data frame
    to a csv file and creates a bar plot showing the data points in the specified column per neighbourhood, colored by cluster,
    and saves the plot as a png file.

    Parameters:
    data (pandas DataFrame): The data frame containing the data to be clustered.
    column (str): The column in the data frame to be used for clustering.
    n_clusters (int): The number of clusters to create.

    Returns:
    None
    """

    # run kmeans on the data
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(data[[column]])
    data['cluster'] = kmeans.labels_
    print(data)
    data = data.sort_values(by='cluster')

    #check if the data frame contains a clusters column and drop it if it does
    if 'clusters' in data.columns:
        data = data.drop(columns='clusters')
    data.to_csv('clustered_{}.csv'.format(column), index=False)

    # plot the data with the clusters
    sns.set(style="whitegrid")
    ax = sns.barplot(x="neighbourhood_name", y=column, hue="cluster", data=data)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=25, fontsize=7)
    ax.set_title('Clustered {} per neighbourhood'.format(column))
    ax.set_xlabel('Neighbourhood')
    ax.set_ylabel(column)
    ax.figure.savefig('cluster_of_{}.png'.format(column))


df = pd.read_csv('../../data/Processed/neighbourhood/2019_life_expt_neighbourhood.csv')
#optimal_clusters_number(df, 'avg_life_expt')
cluster_and_plot(df, 'avg_life_expt', 2)

