import pandas as pd
import seaborn as sns

def aggregate_per_district(data_path, output_path, value_column, output_column, agg):
    """
    aggregate_per_district(data_path, output_path, value_column, output_column, agg)

    This function reads in a csv file from the specified data_path, replaces any occurrences of '...' with 0, converts the specified value_column to a float, groups the data by district, and writes the resulting data to a csv file at the specified output_path. It also creates a bar plot showing the specified output_column per district, and saves the plot as a png file.

    Parameters:
    data_path (str): The path to the input csv file.
    output_path (str): The path to the output csv file.
    value_column (str): The column to be aggregated and converted to a float.
    output_column (str): The name of the column in the output data that will contain the aggregated values.
    agg (str): The aggregation function to apply to the value_column.

    Returns:
    None
    """

    df = pd.read_csv(data_path, sep=';')

    df[value_column] = df[value_column].astype(float)

    # Group the data by district
    df = df.groupby(['district_code', 'district_name']).agg(agg).reset_index()
    df = df.rename(columns={value_column: output_column})
    df = df[['district_code', 'district_name', output_column]]

    df.to_csv(output_path, index=False)

    # Plot the data
    sns.set(style="whitegrid")
    ax = sns.barplot(x='district_name', y=output_column, data=df.sort_values(output_column, ascending=False))
    ax.set_xticklabels(ax.get_xticklabels(), rotation=25, fontsize=7)
    ax.set_title('{} per district'.format(output_column))
    ax.set_xlabel(output_column)
    ax.set_ylabel('District')
    ax.figure.savefig('{}_by_district.png'.format(output_column))

def aggregate_per_neighbourhood(data_path, output_path, value_column, output_column, agg):
    """
    aggregate_per_neighbourhood(data_path, output_path, value_column, output_column, agg)

    This function reads in a csv file from the specified data_path, replaces any occurrences of '...' with 0, converts the specified value_column to a float, groups the data by neighbourhood, and writes the resulting data to a csv file at the specified output_path. It also creates a bar plot showing the specified output_column per neighbourhood for the top 10 neighbourhoods, and saves the plot as a png file.

    Parameters:
    data_path (str): The path to the input csv file.
    output_path (str): The path to the output csv file.
    value_column (str): The column to be aggregated and converted to a float.
    output_column (str): The name of the column in the output data that will contain the aggregated values.
    agg (str): The aggregation function to apply to the value_column.

    Returns:
    None
    """

    df = pd.read_csv(data_path, sep=';')

    df[value_column] = df[value_column].astype(float)

    # Group the data by neighbourhood
    df = df.groupby(['district_code', 'district_name', 'neighbourhood_code', 'neighbourhood_name']).agg(agg).reset_index()
    df = df.rename(columns={value_column: output_column})
    df = df[['district_code', 'district_name', 'neighbourhood_code', 'neighbourhood_name', output_column]]

    df.to_csv(output_path, index=False)

    # Plot the data
    sns.set(style="whitegrid")
    ax = sns.barplot(x='neighbourhood_name', y=output_column, data=df.sort_values(output_column, ascending=False).head(10))
    ax.set_xticklabels(ax.get_xticklabels(), rotation=25, fontsize=7)
    ax.set_title('{} per neighbourhood (top 10)'.format(output_column))
    ax.set_xlabel(output_column)
    ax.set_ylabel('Neighbourhood')
    ax.figure.savefig('{}_by_neighbourhood_top_10.png'.format(output_column))

if __name__ == '__main__':
    aggregate_per_district('/data/Raw Data/Population/2019_life_expt.csv', '../../data/Processed/district/2019_life_expt_district.csv', 'number', 'avg_life_expt', 'mean')
    aggregate_per_neighbourhood('/data/Raw Data/Population/2019_life_expt.csv', '../../data/Processed/neighbourhood/2019_life_expt_neighbourhood.csv', 'number', 'avg_life_expt', 'mean')

