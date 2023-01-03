import pandas as pd
import openai
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = [w for w in filtered_sentence if w.isalpha()]
    return filtered_sentence

def GPT_Completion(texts):
## Call the API key under your account (in a secure way)
    openai.api_key = "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"
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt =  texts,
    temperature = 0.6,
    top_p = 1,
    max_tokens = 200,
    frequency_penalty = 0,
    presence_penalty = 0
    )
    return print(response.choices[0].text)



df = pd.read_csv('/data/Processed/joined_data/final_table_labeled_desc.csv')



# Define the mapping function
def get_label_acc(value):
    if value == 0.0:
        return 'This neighbourhood has very few accidents, making it a safe and peaceful place to live.'
    elif value == 1.0:
        return 'Accidents in this neighbourhood are not a common occurrence, so it is generally a safe place to live.'
    elif value == 2.0:
        return 'Accidents are a rare occurrence in this neighbourhood, so you can feel confident about the safety of the area'
    elif value == 3.0:
        return 'This neighbourhood experiences some accidents, but they are not a regular occurrence.'
    elif value == 4.0:
        return 'Accidents happen relatively often in this neighbourhood, so you may want to consider the safety of the area before deciding to live here.'
    elif value == 5.0:
        return 'Accidents are a common occurrence in this neighbourhood, so you may want to consider other neighbourhoods if safety is a top priority.'
    elif value == 6.0:
        return 'This neighbourhood experiences a high number of accidents, so you may want to consider other neighbourhoods if safety is a top concern.'
    else:
        return 'unknown'

def get_label_avg_occ(value):
    if value == 0.0:
        return 'This neighbourhood has a low population density, with relatively few people living in a given area. It may feel less crowded and more open than other areas.'
    elif value == 1.0:
        return 'This neighbourhood has a relatively low population density, with fewer people living in a given area compared to more densely populated areas. It may feel less crowded and more open than other areas.'
    elif value == 2.0:
        return 'This neighbourhood has a moderate population density, with a reasonable number of people living in a given area. It may feel less crowded than more densely populated areas, but not as open as sparsely populated areas.'
    elif value == 3.0:
        return 'This neighbourhood has a relatively high population density, with a significant number of people living in a given area. It may feel more crowded than lightly populated areas, but not as crowded as densely populated areas.'
    elif value == 4.0:
        return 'This neighbourhood has a very high population density, with a large number of people living in a given area. It may feel very crowded and may not have as much open space as less densely populated areas.'
    elif value == 5.0:
        return 'This neighbourhood has an extremely high population density, with a very large number of people living in a given area. It may feel extremely crowded and may not have much open space.'
    elif value == 6.0:
        return 'This neighbourhood has a population density that is significantly beyond capacity, with a very large number of people living in a given area. It may feel severely crowded and may not have any open space.'
    elif value == 7.0:
        return 'This neighbourhood has an extremely high population density, with a massive number of people living in a given area. It may feel severely overcrowded and may not have any open space.'
    else:
        return 'unknown'

def get_label_above_65(value):
    if value == 0.0:
        return 'a relatively young population'
    elif value == 1.0:
        return 'a balance between young and older residents'
    elif value == 2.0:
        return 'more older residents than young ones'
    elif value == 3.0:
        return 'a significant number of older residents'
    elif value == 4.0:
        return 'a predominantly older population'
    elif value == 5.0:
        return 'a neighborhood with a high concentration of elderly residents'
    else:
        return 'unknown'

def get_label_accademic(value):
    if value == 0.0:
        return 'This neighbourhood has a low concentration of people with a university degree or higher. It may be not suitable for students or young professionals.'
    elif value == 1.0:
        return 'This neighbourhood may have a large number of people with a university degree or higher. It may be suitable for students or young professionals.'
    else:
        return 'unknown'

def get_label_between_18_65(value):
    if value == 0.0:
        return 'This neighborhood may have fewer young adults and families with children compared to others.'
    elif value == 1.0:
        return 'This neighborhood may have a mix of different age groups, including some young adults and families with children.'
    elif value == 2.0:
        return 'This neighborhood may have a higher concentration of young adults and families with children compared to others.'
    elif value == 3.0:
        return 'This neighborhood may have a very high number of young adults and families with children, possibly making it a vibrant and lively area.'
    else:
        return 'unknown'

def get_label_bus_stops(value):
    if value == 0.0:
        return 'poorly served by buses. It may be difficult to get around by public transport.'
    elif value == 1.0:
        return 'moderately served by buses. It may be possible to get around by public transport.'
    elif value == 2.0:
        return 'well served by buses. It may be easy to get around by public transport.'
    elif value == 3.0:
        return 'exceptionally well served by buses. It may be very easy to get around by public transport.'
    else:
        return 'unknown'

def get_label_children_play_area(value):
    if value == 0.0:
        return 'not suitable for families with children'
    elif value == 1.0:
        return 'slightly suitable for families with children'
    elif value == 2.0:
        return 'moderately suitable for families with children'
    elif value == 3.0:
        return 'suitable for families with children'
    elif value == 4.0:
        return 'very suitable for families with children'
    elif value == 5.0:
        return 'ideal for families with children'
    elif value == 6.0:
        return 'exceptionally suitable for families with children'
    elif value == 7.0:
        return 'a heaven for families with children'
    else:
        return 'unknown'

def get_label_cinema_theatre_concerts(value):
    if value == 0.0:
        return 'not a good choice for movie/theater lovers'
    elif value == 1.0:
        return 'limited options for movie/theater entertainment'
    elif value == 2.0:
        return 'a moderate selection of cinemasn & theaters'
    elif value == 3.0:
        return 'plenty of options for movie/theater entertainment'
    elif value == 4.0:
        return 'a great choice for movie/theater lovers'
    else:
        return 'unknown'

def get_label_cultural_leisure_spaces(value):
    if value == 0.0:
        return 'There are no cultural activities in the area. It may not be a good choice for people who like to participate in cultural activities.'
    elif value == 1.0:
        return 'There are only a few cultural activities in the area. It may not be a good choice for people who like to participate in cultural activities.'
    elif value == 2.0:
        return 'There are several cultural activities in the area, providing a wide range of events. It may be a good choice for people who like to participate in cultural activities.'
    else:
        return 'unknown'

def get_label_library_studyroom(value):
    if value == 0.0:
        return 'This indicates that the neighbourhood does not have any library or study room. It may not be suitable for students or people who need a quiet place to study.'
    elif value == 1.0:
        return 'This indicates that the neighbourhood has a few libraries or study rooms. It may not be very suitable for students or people who need a quiet place to study.'
    elif value == 2.0:
        return 'This indicates that the neighbourhood has some libraries or study rooms. It may be suitable for students or people who need a quiet place to study, but they may need to search for a place to study.'
    elif value == 3.0:
        return 'This indicates that the neighbourhood has a lot of libraries or study rooms. It may be very suitable for students or people who need a quiet place to study.'
    elif value == 4.0:
        return 'This indicates that the neighbourhood has a very large number of libraries or study rooms. It is likely to be very suitable for students or people who need a quiet place to study.'
    else:
        return 'unknown'

def get_label_sport_facilities(value):
    if value == 0.0:
        return 'This neighbourhood has very few or no sport facilities. It may not be suitable for people who like to participate in sports.'
    elif value == 1.0:
        return 'This neighbourhood has some sport facilities. It may be suitable for people who like to participate in sports.'
    elif value == 2.0:
        return 'This neighbourhood has a good number of sport facilities that are easily accessible and well-equipped. It may be very suitable for people who like to participate in sports.'
    elif value == 3.0:
        return 'This neighbourhood has a very high number of sport facilities, making it an ideal location for those who enjoy sports and physical activity.'
    else:
        return 'unknown'

def get_label_tourists_points(value):
    if value == 0.0:
        return 'This neighborhood is not a popular tourist destination and does not have many attractions or landmarks that attract tourists.'
    elif value == 1.0:
        return 'This neighborhood has a small number of tourist attractions or landmarks, and may not be a major destination for tourists.'
    elif value == 2.0:
        return 'This neighborhood has a moderate number of tourist attractions or landmarks, and may attract a moderate number of tourists.'
    elif value == 3.0:
        return 'This neighborhood has a large number of tourist attractions or landmarks, and may be a popular destination for tourists.'
    elif value == 4.0:
        return 'This neighborhood has a very high number of tourist attractions or landmarks, and is likely to be a major destination for tourists.'
    elif value == 5.0:
        return 'This neighborhood has an exceptionally high number of tourist attractions or landmarks, and is likely to be a major destination for tourists.'
    else:
        return 'unknown'

def get_label_transportation(value):
    if value == 0.0:
        return 'This neighborhood may not have many transportation options available, making it inconvenient for those who rely on public transportation to get around.'
    elif value == 1.0:
        return 'This neighborhood may have a limited number of transportation options available, which may not be sufficient for those who rely heavily on public transportation.'
    elif value == 2.0:
        return 'This neighborhood may have a moderate number of transportation options available, which may be sufficient for those who occasionally use public transportation.'
    elif value == 3.0:
        return 'This neighborhood may have a large number of transportation options available, making it convenient for those who rely on public transportation to get around.'
    else:
        return 'unknown'

def get_label_street_markets_and_fairs(value):
    if value == 0.0:
        return 'There are no street markets or fairs in the area, offering a more quiet atmosphere.'
    elif value == 1.0:
        return 'There are only a few street markets or fairs in the area.'
    elif value == 2.0:
        return 'There are several street markets and fairs in the area, making it a lively and vibrant area.'
    elif value == 3.0:
        return 'The area has numerous street markets and fairs, creating a lively atmosphere. It may be a popular destination for tourists and it may be loud and busy.'
    else:
        return 'unknown'

def get_label_rent_price(value):
    if value == 0.0:
        return 'This could indicate that the neighborhood is more affordable and may be a good option for those looking to save on rent.'
    elif value == 1.0:
        return 'This could indicate that the neighborhood has moderate rent prices, making it a good option for those who want a balance of price and location.'
    elif value == 2.0:
        return 'This could indicate that the neighborhood has average rent prices and may be a good option for those looking for a convenient location.'
    elif value == 3.0:
        return 'This could indicate that the neighborhood has higher rent prices and may not be a good option for those on a tight budget.'
    elif value == 4.0:
        return 'This could indicate that the neighborhood has very high rent prices and may not be a suitable option for most people.'
    elif value == 5.0:
        return 'This could indicate that the neighborhood has extremely high rent prices and is likely only suitable for those who can afford a luxurious lifestyle.'
    else:
        return 'unknown'

def get_label_hotels(value):
    if value == 0.0:
        return 'This neighborhood does not have any hotels, indicating that it may not be a popular tourist destination.'
    elif value == 1.0:
        return 'This neighborhood has a small number of hotels, suggesting that it may not be a major tourist hub.'
    elif value == 2.0:
        return 'This neighborhood has a moderate number of hotels, indicating that it may attract some tourists but is not necessarily a major tourist destination.'
    elif value == 3.0:
        return 'This neighborhood has a large number of hotels, suggesting that it is a popular tourist destination.'
    else:
        return 'unknown'

def get_label_spaces_for_excercise(value):
    if value == 0.0:
        return 'There are no outdoor spaces suitable for exercise in this neighbourhood.'
    elif value == 1.0:
        return 'There are a few outdoor spaces suitable for exercise in this neighbourhood.'
    elif value == 2.0:
        return 'There are some outdoor spaces suitable for exercise in this neighbourhood.'
    else:
        return 'unknown'

def get_label_parks_gardens(value):
    if value == 0.0:
        return 'This neighbourhood does not have any parks or gardens, so it may not be suitable for people who want outdoor spaces for their pets or for leisure activities.'
    elif value == 1.0:
        return 'This neighbourhood has a few parks or gardens, but they may not be easily accessible or convenient for everyone in the neighbourhood.'
    elif value == 2.0:
        return 'This neighbourhood has a moderate number of parks or gardens, which may be suitable for people who want some outdoor spaces for their pets or leisure activities.'
    elif value == 3.0:
        return 'This neighbourhood has a large number of parks or gardens, which may be suitable for people who want plenty of outdoor spaces for their pets or leisure activities.'
    else:
        return 'unknown'

def get_label_exhebitons_museums(value):
    if value == 0.0:
        return 'There are no exhibitions or museums in the area, making it unsuitable for culture lovers.'
    elif value == 1.0:
        return 'There are few exhibitions and museums in the area, but they offer a good opportunity to visit some artistic and cultural activities and events.'
    elif value == 2.0:
        return 'There are several exhibitions and museums in the area, which offer a wide range of cultural activities and events.'
    else:
        return 'unknown'

def get_label_music_drinks(value):
    if value == 0.0:
        return 'may indicate that the neighbourhood is relatively quiet, with little to no music or drink options available.'
    elif value == 1.0:
        return 'may indicate that there are a limited number of music or drink options in the neighbourhood, possibly making it somewhat quieter than areas with more options.'
    elif value == 2.0:
        return 'may indicate that there are a moderate number of music or drink options in the neighbourhood, potentially making it more lively and less quiet.'
    elif value == 3.0:
        return 'may indicate that there are a large number of music or drink options in the neighbourhood, potentially making it quite lively and not very quiet.'
    elif value == 4.0:
        return 'may indicate that there are a very large number of music or drink options in the neighbourhood, potentially making it very lively and not quiet at all.'
    else:
        return 'unknown'

def get_label_temporary_exhibitions(value):
    if value == 0.0:
        return 'There are no temporary exhibitions in the area. It may be a quiet and peaceful area.'
    elif value == 1.0:
        return 'There are only a few temporary exhibitions in the area, but they offer a variety of cultural activities and events.'
    elif value == 2.0:
        return 'There are several temporary exhibitions in the area, providing a range of cultural activities and events.'
    elif value == 3.0:
        return 'The area has numerous temporary exhibitions, creating a vibrant cultural scene with plenty of activities and events to explore.'
    else:
        return 'unknown'


# Apply the mapping functions
#df['label_accidents'] = df['label_accidents'].apply(get_label_acc)
#df['label_avg_occ'] = df['label_avg_occ'].apply(get_label_avg_occ)
#df['label_above_65'] = df['label_above_65'].apply(get_label_above_65)
#df['label_academic_level'] = df['label_academic_level'].apply(get_label_accademic)
# df['label_between_18_65'] = df['label_between_18_65'].apply(get_label_between_18_65)
# df['label_bus_stops'] = df['label_bus_stops'].apply(get_label_bus_stops)
# df['label_children_play_areas'] = df['label_children_play_areas'].apply(get_label_children_play_area)
# df['label_cinema_theatre_concerts'] = df['label_cinema_theatre_concerts'].apply(get_label_cinema_theatre_concerts)
# df['label_cultural_leisure_spaces'] = df['label_cultural_leisure_spaces'].apply(get_label_cultural_leisure_spaces)
# df['label_library_studyroom'] = df['label_library_studyroom'].apply(get_label_library_studyroom)
# df['label_sport_facilities'] = df['label_sport_facilities'].apply(get_label_sport_facilities)
# df['label_tourists_points'] = df['label_tourists_points'].apply(get_label_tourists_points)
# df['label_transportation'] = df['label_transportation'].apply(get_label_transportation)
# df['label_street_markets_and_fairs'] = df['label_street_markets_and_fairs'].apply(get_label_street_markets_and_fairs)
#df['label_rent_price'] = df['label_rent_price'].apply(get_label_rent_price)
#df['label_hotels'] = df['label_hotels'].apply(get_label_hotels)
#df['label_spaces_for_excercise'] = df['label_spaces_for_excercise'].apply(get_label_spaces_for_excercise)
#df['label_parks_gardens'] = df['label_parks_gardens'].apply(get_label_parks_gardens)
#df['label_exhebitons_museums'] = df['label_exhebitons_museums'].apply(get_label_exhebitons_museums)
#df['label_music_drinks'] = df['label_music_drinks'].apply(get_label_music_drinks)
#df['label_temporary_exhibitions'] = df['label_temporary_exhibitions'].apply(get_label_temporary_exhibitions)


# add column descriptions which concatenate the text from all columns that starts with label_
#df['description'] = df.apply(lambda row: ' '.join(row[row.index.str.startswith('label_')].values.astype(str)), axis=1)


#apply preprocessing to the description column
#df['description_processed'] = df['description'].apply(preprocess_text)

# save the data
#df.to_csv('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table_labeled_desc.csv', index=False)

# save a version only with district_code, district_name, neighborhood_code, neighborhood_name, description
df[['district_code', 'district_name', 'neighbourhood_code', 'neighbourhood_name', 'description']].to_csv('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table_labeled_desc_only.csv', index=False)