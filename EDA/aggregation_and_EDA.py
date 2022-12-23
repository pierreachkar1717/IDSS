import pandas as pd
import seaborn as sns

def aggregate_by_district(data_path, output_path, column):
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
    aggregate_by_district('/Users/pierreachkar/Downloads/neighborhood_finder/OpenDataBCN/City/2021_incidents_gestionats_gub.csv', '/Users/pierreachkar/Downloads/neighborhood_finder/OpenDataBCN/Processed/2021_incidents_gestionats_gub_district.csv', '2021_incidents_gestionats_gub')
    aggregate_by_neighbourhood('/Users/pierreachkar/Downloads/neighborhood_finder/OpenDataBCN/City/2021_incidents_gestionats_gub.csv', '/Users/pierreachkar/Downloads/neighborhood_finder/OpenDataBCN/Processed/2021_incidents_gestionats_gub_neighbourhood.csv', '2021_incidents_gestionats_gub')

