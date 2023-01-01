import plotly.express as px
import pandas as pd
import json
import geopandas as gpd

#read the geojson file with geopandas
gdf = gpd.read_file('/Users/pierreachkar/Downloads/neighborhood_finder/data/barris.geojson')

# if DISTRICTE or BARRI values start with 0, remove the 0
gdf['BARRI'] = gdf['BARRI'].str.lstrip('0')
gdf['DISTRICTE'] = gdf['DISTRICTE'].str.lstrip('0')


# read the csv file
df = pd.read_csv('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/neighbourhood/2022_2_rent_price.csv', sep= ';')

#convert the district_code and neighbourhood_code to string
df['district_code'] = df['district_code'].astype(str)
df['neighbourhood_code'] = df['neighbourhood_code'].astype(str)

# merge the two dataframes on district_code and neighbourhood_code from df and DISTRICTE and BARRI from gdf
merged = gdf.merge(df, left_on=['DISTRICTE', 'BARRI'], right_on=['district_code', 'neighbourhood_code'], how='outer')

# create map with plotly
fig = px.choropleth_mapbox(merged, geojson=merged.geometry, locations=merged.index, color='preis',
                            color_continuous_scale="Viridis",
                            range_color=(0, 1700),
                            mapbox_style="carto-positron",
                            zoom=9, center = {"lat": 41.3851, "lon": 2.1734},
                            opacity=0.5,
                           # add neighborhood name to hover data
                            hover_data={'preis':True, 'neighbourhood_name':True}
                            )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()




