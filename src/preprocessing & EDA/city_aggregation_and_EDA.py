import pandas as pd
import seaborn as sns

def aggregate_by_district(data_path, output_path, column):
    """
    aggregate_by_district(data_path, output_path, column)

    This function reads in a csv file from the specified data_path, groups the data by district, and writes the resulting data to a csv file at the specified output_path. It also creates a bar plot showing the number of entries in the specified column per district, and saves the plot as a png file.

    Parameters:
    data_path (str): The path to the input csv file.
    output_path (str): The path to the output csv file.
    column (str): The column to group and count by district.

    Returns:
    None
    """

    df = pd.read_csv(data_path, sep=';')

    # Group by district
    df = df.groupby(['district_code', 'district_name']).size().reset_index(name=column)
    df.to_csv(output_path, index=False)

    # Plot the data
    sns.set(style="whitegrid")
    ax = sns.barplot(x="district_name", y=column, data=df.sort_values(by=column, ascending=False))
    ax.set_xticklabels(ax.get_xticklabels(), rotation=25, fontsize=7)
    ax.set_title('Number of {} per district'.format(column))
    ax.set_xlabel('District')
    ax.set_ylabel('Number of {}'.format(column))
    ax.figure.savefig('{}_by_district.png'.format(column))

def aggregate_by_neighbourhood(data_path, output_path, column):
    """
    aggregate_by_neighbourhood(data_path, output_path, column)

    This function reads in a csv file from the specified data_path, groups the data by neighbourhood, and writes the resulting data to a csv file at the specified output_path. It also creates a bar plot showing the number of entries in the specified column per neighbourhood for the top 10 neighbourhoods, and saves the plot as a png file.

    Parameters:
    data_path (str): The path to the input csv file.
    output_path (str): The path to the output csv file.
    column (str): The column to group and count by neighbourhood.

    Returns:
    None
    """

    df = pd.read_csv(data_path, sep=';')

    # Group by neighbourhood
    df = df.groupby(['district_code', 'district_name', 'neighbourhood_code', 'neighbourhood_name']).size().reset_index(name=column)
    df.to_csv(output_path, index=False)

    # Plot the data
    sns.set(style="whitegrid")
    ax = sns.barplot(x="neighbourhood_name", y=column, data=df.sort_values(by=column, ascending=False).head(10))
    ax.set_xticklabels(ax.get_xticklabels(), rotation=25, fontsize=7)
    ax.set_title('Number of {} per neighbourhood (top 10)'.format(column))
    ax.set_xlabel('Neighbourhood')
    ax.set_ylabel('Number of {}'.format(column))
    ax.figure.savefig('{}_by_neighbourhood_top_10.png'.format(column))


if __name__ == '__main__':
    aggregate_by_district('/data/Raw Data/City/music_drinks.csv',
                          '../../data/Processed/district/music_drinks.csv', 'music_drinks')
    aggregate_by_neighbourhood('/data/Raw Data/City/music_drinks.csv',
                               '../../data/Processed/neighbourhood/music_drinks.csv', 'music_drinks')

