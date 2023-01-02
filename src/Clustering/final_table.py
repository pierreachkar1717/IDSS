from clustering import optimal_clusters_number, cluster_and_plot
import pandas as pd


## Each step should be done separately, so comment the other functions out when running one of them.

# Load your data into a pandas DataFrame
df = pd.read_csv('../../data/Processed/joined_data/final_table.csv')


# Choose the column/columns in your data that you want to use for clustering
cols = ['accidents', 'label_accidents',
       'average_occupation_per_household', 'label_avg_occ', 'above_65t',
       'label_above_65', 'elementary_highschool_bachelorsdegree', 'no_studies',
       'primarystudies_schoolcertificate', 'university_studies',
       'secondary_school', 'label_academic_level', 'between_18_64',
       'label_between_18_65', 'bus_stops', 'label_bus_stops',
       'children_play_areas', 'label_children_play_areas',
       'cinema_theater_concerts', 'label_cinema_theatre_concerts',
       'culture_leisure_spaces', 'label_cultural_leisure_spaces',
       'library_studyroom_museum_spaces', 'label_library_studyroom',
       'sport_facilities', 'label_sport_facilities', 'tourists_points',
       'label_tourists_points', 'transportation', 'label_transportation',
       'street_markets_and_fairs', 'label_street_markets_and_fairs',
       'temporaray_exhibitions',
       'rent_price', 'label_rent_price', 'hotels', 'label_hotels',
       'spaces_for_exercising', 'label_spaces_for_excercise', 'parks_gardens',
       'label_parks_gardens', 'number_of_museums_and_exhibitions',
       'label_exhebitons_museums']

# First: Call the optimal_clusters_number function to determine the optimal number of clusters for your data
# Decide on the best number of clusters for your data by considering both plots
# The elbow method plot is useful for finding the point where the decrease in SSE starts to level off (The bend in the curve)
# The silhouette score plot is useful for finding the number of clusters with the highest score
# If the two plots do not agree on the same number of clusters, you need to find a compromise solution by selecting a number of clusters
# that is recommended by the elbow method plot and also has a relatively high silhouette score

#optimal_clusters_number(df, cols, 40) # 8 clusters

#Second: Call the cluster_and_plot function to cluster your data and plot the results
cluster_and_plot(df, cols, 8, 'final_table')

# Third: Load the resulting csv file into a new pandas DataFrame and add a new column to the DataFrame
# This column will contain numerical values describing the cluster label for each data point.
#df = pd.read_csv('../../data/Processed/clustering/clustered_final_table.csv')

# Here 0 means low, 1 means medium and 2 means high
#df['label'] = df['cluster'].map({3:0, 0:1, 1:2, 2:3})

# Or we can still consider adding categorical values to the label column
#df['label_cat'] = df['cluster'].map({0: 'medium_number_library_studyroom', 1: 'high_number_library_studyroom', 2: 'low_number_library_studyroom'})

#df.to_csv('../../data/Processed/clustering/labled/labeled_sport_facilities.csv', index=False)
