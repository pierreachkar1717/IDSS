import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import json
import geopandas as gpd

# Mapping each answer to numerical value
mapping_dict= {
    "How much do you care about neighbourhood safety?": {
        "Very concerned about safety": 0.0,
        "Extremely concerned about safety": 1.0,
        "Highly concerned about safety": 2.0,
        "Somewhat concerned about safety": 3.0,
        "Mildly concerned about safety": 4.0,
        "Not very concerned about safety": 5.0,
        "Not concerned about safety at all": 6.0
    },
    "Which of the following options best reflects your preference for the level of crowding and liveliness in the neighborhood?": {
        "Prefer a extremely quiet neighborhood": 0.0,
        "Prefer a very quiet neighborhood": 1.0,
        "Prefer a quiet neighborhood": 2.0,
        "Prefer a lightly crowded neighborhood": 3.0,
        "Prefer a mildly crowded neighborhood": 4.0,
        "Prefer a lively neighborhood": 5.0,
        "Prefer a crowded neighborhood": 6.0,
        "Prefer a very crowded neighborhood": 7.0
    },
    "Would you like to stay in a neighbourhood with a lot of students?": {
        "no": 0.0,
        "yes": 1.0
    },
    "How important is the availability of public transportation in the neighborhood to you?": {
        "Not important at all": 0.0,
        "Somewhat important": 1.0,
        "Very important": 2.0,
        "Extremely important": 3.0
    },
    "How important is the presence of childrens play areas in the neighborhood to you?": {
        "Not important at all": 0.0,
        "Somewhat important": 1.0,
        "Important": 2.0,
        "Very important": 3.0,
        "Extremely important": 4.0,
        "Critical": 5.0,
        "Absolutely essential": 6.0,
        "Most important factor": 7.0
    },
    "Are you interested in having cultural events and attractions (such as theaters, cinemas, museums, etc.) near you?": {
        "Not interested at all": 0.0,
        "Mildly interested": 1.0,
        "Interested": 2.0,
        "Very interested": 3.0,
        "Extremely interested": 4.0
    },
    "Is the presence of libraries or study rooms in the neighborhood important to you?": {
        "Not important at all": 0.0,
        "Somewhat important": 1.0,
        "Mildly important": 2.0,
        "Very important": 3.0,
        "Extremely important": 4.0
          },
    "How important to you is having sports facilities available within the neighbourhood?": {
        "Not important at all": 0.0,
        "Somewhat important": 1.0,
        "Mildly important": 2.0,
        "Very important": 3.0
    },
    "How much does the level of tourism in the neighborhood matter to you?": {
        "Very important, do not want tourists in neighborhood": 0.0,
        "Important, do not want tourists in neighborhood": 1.0,
        "Mildly important": 2.0,
        "Somewhat important": 3.0,
        "Not important": 4.0,
        "Not at all important": 5.0
    },
    "Do you appreciate having open-air street markets and fairs in your neighborhood?": {
        "Do not appreciate at all": 0.0,
        "Somewhat appreciate": 1.0,
        "Mildly appreciate": 2.0,
        "Very much appreciate": 3.0
    },
    "How much are you planning to spend on rent?": {
        "(550-690)": 0.0,
        "(690-820)": 1.0,
        "(820-920)": 2.0,
        "(920-1200)": 3.0,
        "(1200-1500)": 4.0,
        "(1500-2000)": 5.0
      },
    "Do you like to exercise outdoors?": {
        "No, Do not like to exercise outdoors": 0.0,
        "Somewhat enjoy exercising outdoors": 1.0,
        "Yes, Very much enjoy exercising outdoors": 2.0
  },
    "How important is it for you to have parks nearby?": {
        "Not important at all": 0.0,
        "Somewhat important": 1.0,
        "Mildly important": 2.0,
        "Very important": 3.0
  },
   "How important is the presence of bars and nightclubs in the neighborhood to you?": {
        "Not important at all": 0.0,
        "Somewhat important": 1.0,
        "Mildly important": 2.0,
        "Very important": 3.0,
        "Extremely important": 4.0
  },
   "Which of the following neighbourhood age groups seems to be the best fit for you?": {
        "mostly young people": 0.0,
        "mixed": 1.0,
        "mostly older people": 2.0
  }
}

# Mapping for drop down menue
name_mapping = {
    'Accidents': 'accidents',
    'Average occupation per household': 'average_occupation_per_household',
    'Number of people above 65': 'above_65t',
    'Number of people between 18-64': 'between_18_65',
    'Bus stops': 'bus_stops',
    'Transportation': 'transportation',
    'Number of children play areas': 'children_play_areas',
    'Number of cinema, theatre and concerts': 'cinema_theatre_concerts',
    'Number of culture leisure spaces': 'culture_leisure_spaces',
    'Number of library studyroom museum spaces': 'library_studyroom_museum_spaces',
    'Number of sport facilities': 'sport_facilities',
    'Number of tourists points': 'tourists_points',
    'Number of street markets and fairs': 'street_markets_and_fairs',
    'Rent price': 'rent_price',
    'Number of hotels': 'hotels',
    'Number of exercising spaces': 'spaces_for_excercise',
    'Number of parks & gardens': 'parks_gardens',
    'Number of museums & exhibitions': 'number_of_museums_and_exhibitions',
    'Number of bars & nightclubs': 'music_drinks'
}

def process_dataframe(df, mapping_dict):
    # Apply Mapping
    df = df.replace(mapping_dict)

    # Copy the dataframe
    df2 = df.copy()

    # Create columns for doing the matching
    df2['label_accidents'] = df2['How much do you care about neighbourhood safety?']
    df2['label_avg_occupation'] = df2[
        'Which of the following options best reflects your preference for the level of crowding and liveliness in the neighborhood?']
    df2['label_above_65'] = df2['Which of the following neighbourhood age groups seems to be the best fit for you?']
    df2['label_academic_level'] = df2['Would you like to stay in a neighbourhood with a lot of students?']
    df2['label_between_18_65'] = df2[
        'Which of the following neighbourhood age groups seems to be the best fit for you?']
    df2['label_bus_stops'] = df2[
        'How important is the availability of public transportation in the neighborhood to you?']
    df2['label_children_play_areas'] = df2[
        'How important is the presence of childrens play areas in the neighborhood to you?']
    df2['label_cinema_theaters'] = df2[
        'Are you interested in having cultural events and attractions (such as theaters, cinemas, museums, etc.) near you?']
    df2['label_cultural_leisure_spaces'] = df2[
        'Are you interested in having cultural events and attractions (such as theaters, cinemas, museums, etc.) near you?']
    df2['label_library_studyroom'] = df2[
        'Is the presence of libraries or study rooms in the neighborhood important to you?']
    df2['label_sport_facilities'] = df2[
        'How important to you is having sports facilities available within the neighbourhood?']
    df2['label_tourists_points'] = df2['How much does the level of tourism in the neighborhood matter to you?']
    df2['label_transportation'] = df2[
        'How important is the availability of public transportation in the neighborhood to you?']
    df2['label_street_markets_and_fairs'] = df2[
        'Do you appreciate having open-air street markets and fairs in your neighborhood?']
    df2['label_rent_price'] = df2['How much are you planning to spend on rent?']
    df2['label_hotels'] = df2['How much does the level of tourism in the neighborhood matter to you?']
    df2['label_spaces_for_excercise'] = df2['Do you like to exercise outdoors?']
    df2['label_parks_gardens'] = df2['How important is it for you to have parks nearby?']
    df2['label_exhebitons_museums'] = df2[
        'Are you interested in having cultural events and attractions (such as theaters, cinemas, museums, etc.) near you?']
    df2['label_music_drinks'] = df2['How important is the presence of bars and nightclubs in the neighborhood to you?']
    df2['label_temporary_exhibitions'] = df2[
        'Are you interested in having cultural events and attractions (such as theaters, cinemas, museums, etc.) near you?']

    # Remove unecessary columns
    df2 = df2.filter(regex='user_id|label_')

    # Mappping to our values
    df2.loc[df2['label_cultural_leisure_spaces'] > 2.0, 'label_cultural_leisure_spaces'] = 2.0
    df2.loc[df2['label_exhebitons_museums'] > 2.0, 'label_exhebitons_museums'] = 2.0

    df2.loc[df2['label_temporary_exhibitions'] > 3.0, 'label_temporary_exhibitions'] = 3.0

    df2.loc[df2['label_hotels'] > 3.0, 'label_hotels'] = 3.0

    df2.loc[df2['label_above_65'] == 2.0, 'label_above_65'] = 5.0
    df2.loc[df2['label_above_65'] == 1.0, 'label_above_65'] = 2.0
    df2.loc[df2['label_above_65'] == 0.0, 'label_above_65'] = 0.0

    df2.loc[df2['label_between_18_65'] == 2.0, 'label_between_18_65'] = 0.0
    df2.loc[df2['label_between_18_65'] == 1.0, 'label_between_18_65'] = 1.0
    df2.loc[df2['label_between_18_65'] == 0.0, 'label_between_18_65'] = 3.0

    df2.to_csv('/Users/pierreachkar/Downloads/neighborhood_finder/data/user_input/user_input.csv', index=False)

    return df2

def find_similar_neighborhoods(questions_file, data_file):
  df_q = questions_file
  df_data = data_file

  # use neighborhood_code as index
  df_data = df_data.set_index('neighbourhood_code')

  # drop the columns that are not needed
  df_data = df_data.drop(['district_code', 'district_name', 'neighbourhood_name'], axis=1)

  # use user_name as index
  df_q = df_q.set_index('user_id')

  # calculate the cosine similarity and store it in a new column in df_data
  df_data['similarity'] = cosine_similarity(df_data, df_q)

  # sort the dataframe by similarity
  df_data = df_data.sort_values(by=['similarity'], ascending=False)

  # save the top 10 results
  #df_data.head(10).to_csv(output_file, index=True)

  return df_data.head(10)

import geopandas as gpd
import plotly.express as px

def create_choropleth_map(geojson_file, df, column_name):
  # read the geojson file with geopandas
  gdf = geojson_file

  # if DISTRICTE or BARRI values start with 0, remove the 0
  gdf['BARRI'] = gdf['BARRI'].str.lstrip('0')
  gdf['DISTRICTE'] = gdf['DISTRICTE'].str.lstrip('0')

  # read the csv file
  df = df

  # convert the district_code and neighbourhood_code to string
  df['district_code'] = df['district_code'].astype(str)
  df['neighbourhood_code'] = df['neighbourhood_code'].astype(str)

  # merge the two dataframes on district_code and neighbourhood_code from df and DISTRICTE and BARRI from gdf
  merged = gdf.merge(df, left_on=['DISTRICTE', 'BARRI'], right_on=['district_code', 'neighbourhood_code'], how='outer')

  # define min max for the legend
  min_value = merged[column_name].min()
  max_value = merged[column_name].max()

  # create map with plotly
  fig = px.choropleth_mapbox(merged, geojson=merged.geometry, locations=merged.index, color=column_name,
                              color_continuous_scale="Viridis",
                              range_color=(min_value, max_value),
                              mapbox_style="carto-positron",
                              zoom=9, center={"lat": 41.3851, "lon": 2.1734},
                              opacity=0.5,
                              # add neighborhood name to hover data
                              hover_data={column_name: True, 'Neighbourhood': True}
                              )
  fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
  st.plotly_chart(fig)

def questionary():
    st.title(" Forms to find the best neighborhood for you")
   
    # Create an account
    original_title = '<p style="font-family:sans-serif; color:White; font-size: 30px;">Create an account</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    firstname = st.text_input("Firstname")
    lastname = st.text_input("Lastname")
        
    original_title = '<p style="font-family:sans-serif; color:White; font-size: 30px;">Main Form</p>'
    st.markdown(original_title, unsafe_allow_html=True)

    #checkbox
    st.subheader("How much do you care about neighbourhood safety?")
    q1 = st.radio(
        "", #title above because i could find how to change the font
        ('Very concerned about safety', 'Extremely concerned about safety', 'Highly concerned about safety', 'Somewhat concerned about safety', 'Mildly concerned about safety', 'Not very concerned about safety', 'Not concerned about safety at all'), key=1, 
        )
    st.write("")
    st.subheader("Which of the following options best reflects your preference for the level of crowding and liveliness in the neighborhood?")
    q2 = st.radio(
        "",
        ('Prefer a extremely quiet neighborhood', 'Prefer a very quiet neighborhood', 'Prefer a quiet neighborhood', 'Prefer a lightly crowded neighborhood', 'Prefer a mildly crowded neighborhood', 'Prefer a lively neighborhood', 'Prefer a crowded neighborhood', 'Prefer a very crowded neighborhood'), key=2)
    
    st.write("") 
    st.subheader("Would you like to stay in a neighbourhood with a lot of students? ")
    q3 = st.radio(
        "",
        ('no', 'yes'), key=3)
    
    st.write("") 
    st.subheader("How important is the availability of public transportation in the neighborhood to you? ")
    q45= st.radio(
        "",
        ('Not important at all', 'Somewhat important', 'Very important', 'Extremely important'), key=4)

    st.write("") 
    st.subheader("How important is the presence of children's play areas in the neighborhood to you?")
    q6 = st.radio(
        "",
        ('Not important at all', 'Somewhat important', 'Important', 'Very important', 'Extremely important', 'Critical', 'Absolutely essential', 'Most important factor'), key=6)

    
    st.write("") 
    st.subheader("Are you interested in having cultural events and attractions (such as theaters, cinemas, museums, etc.) near you?")
    q789 = st.radio(
        "",
        ('Not interested at all', 'Mildly interested', 'Interested', 'Very interested', 'Extremely interested'), key=7)

    st.write("") 
    st.subheader("Is the presence of libraries or study rooms in the neighborhood important to you?")
    q10 = st.radio(
        "",
        ('Not important at all', 'Somewhat important', 'Mildly important', 'Very important', 'Extremely important'), key=10)

    st.write("") 
    st.subheader("How important to you is having sports facilities available within the neighbourhood?")
    q11 = st.radio(
        "",
        ('Not important at all', 'Somewhat important', 'Mildly important', 'Very important'), key=11)

    st.write("") 
    st.subheader("How much does the level of tourism in the neighborhood matter to you?")
    q1213 = st.radio(
        "",
        ('Very important, do not want tourists in neighborhood', 'Important, do not want tourists in neighborhood', 'Mildly important', 'Somewhat important', 'Not important', 'Not at all important'), key=12)

    st.write("") 
    st.subheader("Do you appreciate having open-air street markets and fairs in your neighborhood?")
    q14 = st.radio(
        "",
        ('Do not appreciate at all', 'Somewhat appreciate', 'Mildly appreciate', 'Very much appreciate'), key=14)
    
    st.write("") 
    st.subheader("How much are you planning to spend on rent?")
    q15 = st.radio(
        "",
        ('(550-690)', '(690-820)', '(820-920)', '(920-1200)', '(1200-1500)', '(1500-2000)'), key=15)

    st.write("") 
    st.subheader("Do you like to exercise outdoors?")
    q16 = st.radio(
        "",
        ('No, Do not like to exercise outdoors', 'Somewhat enjoy exercising outdoors', 'Yes, Very much enjoy exercising outdoors'), key=16)
    
    st.write("") 
    st.subheader("How important is it for you to have parks nearby?")
    q17 = st.radio(
        "",
        ('Not important at all', 'Somewhat important', 'Mildly important', 'Very important'), key=17)
    
    st.write("") 
    st.subheader("How important is the presence of bars and nightclubs in the neighborhood to you?")
    q18 = st.radio(
        "",
        ('Not important at all', 'Somewhat important', 'Mildly important', 'Very important', 'Extremely important'), key=18)

    st.write("") 
    st.subheader("Which of the following neighbourhood age groups seems to be the best fit for you?")
    q1920 = st.radio(
        "",
        ('mostly young people', 'mixed', 'mostly older people'), key=19)
    
    st.write("") 
    button = st.button(label='SEND')

    # store is a dataframe
    df = pd.DataFrame(columns=['user_id', 'How much do you care about neighbourhood safety?',
                            'Which of the following options best reflects your preference for the level of crowding and liveliness in the neighborhood?',
                            'Would you like to stay in a neighbourhood with a lot of students?',
                            'How important is the availability of public transportation in the neighborhood to you?',
                            'How important is the presence of childrens play areas in the neighborhood to you?',
                            'Are you interested in having cultural events and attractions (such as theaters, cinemas, museums, etc.) near you?',
                            'Is the presence of libraries or study rooms in the neighborhood important to you?',
                            'How important to you is having sports facilities available within the neighbourhood?',
                            'How much does the level of tourism in the neighborhood matter to you?',
                            'Do you appreciate having open-air street markets and fairs in your neighborhood?',
                            'How much are you planning to spend on rent?',
                            'Do you like to exercise outdoors?',
                            'How important is it for you to have parks nearby?',
                            'How important is the presence of bars and nightclubs in the neighborhood to you?',
                            'Which of the following neighbourhood age groups seems to be the best fit for you?'])

    # Answers
    df.loc[len(df)] = [f"{firstname}.{lastname}", q1, q2, q3, q45, q6, q789, q10, q11, q1213, q14, q15, q16, q17, q18, q1920]

    if button:
      st.write('You have successfully submitted !')
      #st.write(df)

    return df

      # # map the user input & save to csv
      # df_u = process_dataframe(df, mapping_dict)
      # df_data = pd.read_csv('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/labeled_num.csv')
      #
      # # recommend the neighbourhood
      # df_rec = find_similar_neighborhoods(df_u, df_data)
      #
      # # merge the recommendation with the original data
      # df_all_data = pd.read_csv('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table_all_info.csv')
      # df_res = pd.merge(df_rec, df_all_data, on=['neighbourhood_code'], how='left')
      #
      # #rename the column neighbourhood_name to Neighbourhood
      # df_res.rename(columns={'neighbourhood_name': 'Neighbourhood'}, inplace=True)
      #
      # #  display the results
      # st.write('Your recommended neighbourhoods are:')
      #
      # # write the Neighbourhood column as a table
      # st.table(df_res['Neighbourhood'])
      #
      # # write a text and then drop menue to choose the column
      # st.write('You can also see the results with more details in a map:')
      #
      #   #drop menue to choose the column (map the names in the drop down to the names in the dataframe)
      #   # option = st.selectbox(
      #   #     'Select the column you want to see in the map',
      #   #     ('accidents', 'average_occupation_per_household', 'above_65t', 'between_18_64', 'bus_stops'
      #   #      'transportation', 'children_play_areas', 'cinema_theatre_concerts', 'culture_leisure_spaces',
      #   #      'library_studyroom_museum_spaces', 'sport_facilities', 'tourists_points',
      #   #      'street_markets_and_fairs', 'rent_price', 'hotels', 'spaces_for_exercising', 'parks_gardens',
      #   #      'number_of_museums_and_exhibitions', 'music_drinks'))
      #
      # option = st.selectbox(
      #       'Select the column you want to see in the map',
      #       list(name_mapping.keys())
      # )
      #
      # # column name is the result of the drop menue
      # column_name = option
      #
      # # map
      # geojson = gpd.read_file('/Users/pierreachkar/Downloads/neighborhood_finder/data/barris.geojson')
      # create_choropleth_map(geojson, df_res, name_mapping[option])

def generate_and_display_recommendations(df):
    # map the user input & save to csv
    df_u = process_dataframe(df, mapping_dict)
    df_data = pd.read_csv('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/labeled_num.csv')

    # recommend the neighbourhood
    df_rec = find_similar_neighborhoods(df_u, df_data)

    # merge the recommendation with the original data
    df_all_data = pd.read_csv('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table_all_info.csv')
    df_res = pd.merge(df_rec, df_all_data, on=['neighbourhood_code'], how='left')

    #rename the column neighbourhood_name to Neighbourhood
    df_res.rename(columns={'neighbourhood_name': 'Neighbourhood'}, inplace=True)

    #  display the results
    st.write('Your recommended neighbourhoods are:')

    # write the Neighbourhood column as a table
    st.table(df_res['Neighbourhood'])

    # write a text and then drop menue to choose the column
    st.write('You can also see the results with more details in a map:')

    #drop menue to choose the column (map the names in the drop down to the names in the dataframe)
    # option = st.selectbox(
    #     'Select the column you want to see in the map',
    #     ('accidents', 'average_occupation_per_household', 'above_65t', 'between_18_64', 'bus_stops'
    #      'transportation', 'children_play_areas', 'cinema_theatre_concerts', 'culture_leisure_spaces',
    #      'library_studyroom_museum_spaces', 'sport_facilities', 'tourists_points',
    #      'street_markets_and_fairs', 'rent_price', 'hotels', 'spaces_for_exercising', 'parks_gardens',
    #      'number_of_museums_and_exhibitions', 'music_drinks'))

    option = st.selectbox(
        'Select the column you want to see in the map',
        list(name_mapping.keys())
    )

    # column name is the result of the drop menue
    column_name = option

    # map
    geojson = gpd.read_file('/Users/pierreachkar/Downloads/neighborhood_finder/data/barris.geojson')
    create_choropleth_map(geojson, df_res, name_mapping[option])

def main():
    st.title('Neighbourhood Finder')
    st.write('Please fill in the following information to get your recommended neighbourhoods:')
    df = questionary()
    generate_and_display_recommendations(df)

if __name__ == '__main__':
    main()
