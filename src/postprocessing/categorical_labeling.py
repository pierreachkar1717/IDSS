''' transforming numerical labels to categorical labels '''
import pandas as pd

df = pd.read_csv('/data/Processed/joined_data/final_table_labeled_cat.csv')

# Define the mapping function
def get_label_acc(value):
    if value == 0.0:
        return 'minimal'
    elif value == 1.0:
        return 'infrequent'
    elif value == 2.0:
        return 'rare'
    elif value == 3.0:
        return 'occasional'
    elif value == 4.0:
        return 'frequent'
    elif value == 5.0:
        return 'common'
    elif value == 6.0:
        return 'very_common'
    else:
        return 'unknown'

def get_label_avg_occ(value):
    if value == 0.0:
        return 'sparse'
    elif value == 1.0:
        return 'sparsely_populated'
    elif value == 2.0:
        return 'lightly_populated'
    elif value == 3.0:
        return 'moderately_populated'
    elif value == 4.0:
        return 'densely_populated'
    elif value == 5.0:
        return 'crowded'
    elif value == 6.0:
        return 'overcrowded'
    elif value == 7.0:
        return 'extremely_crowded'
    else:
        return 'unknown'

def get_label_above_65(value):
    if value == 0.0:
        return 'low'
    elif value == 1.0:
        return 'medium_low'
    elif value == 2.0:
        return 'medium'
    elif value == 3.0:
        return 'medium_high'
    elif value == 4.0:
        return 'high'
    elif value == 5.0:
        return 'very_high'
    else:
        return 'unknown'

def get_label_accademic(value):
    if value == 0.0:
        return 'low'
    elif value == 1.0:
        return 'high'
    else:
        return 'unknown'

def get_label_between_18_65(value):
    if value == 0.0:
        return 'low'
    elif value == 1.0:
        return 'medium'
    elif value == 2.0:
        return 'high'
    elif value == 3.0:
        return 'very_high'
    else:
        return 'unknown'

def get_label_bus_stops(value):
    if value == 0.0:
        return 'low'
    elif value == 1.0:
        return 'medium'
    elif value == 2.0:
        return 'high'
    elif value == 3.0:
        return 'very_high'
    else:
        return 'unknown'

def get_label_children_play_area(value):
    if value == 0.0:
        return 'low'
    elif value == 1.0:
        return 'few'
    elif value == 2.0:
        return 'medium'
    elif value == 3.0:
        return 'many'
    elif value == 4.0:
        return 'several'
    elif value == 5.0:
        return 'high'
    elif value == 6.0:
        return 'very_high'
    elif value == 7.0:
        return 'a lot'
    else:
        return 'unknown'

def get_label_cinema_theatre_concerts(value):
    if value == 0.0:
        return 'none'
    elif value == 1.0:
        return 'few'
    elif value == 2.0:
        return 'some'
    elif value == 3.0:
        return 'many'
    elif value == 4.0:
        return 'a_lot'
    else:
        return 'unknown'

def get_label_cultural_leisure_spaces(value):
    if value == 0.0:
        return 'low'
    elif value == 1.0:
        return 'medium'
    elif value == 2.0:
        return 'high'
    else:
        return 'unknown'

def get_label_library_studyroom(value):
    if value == 0.0:
        return 'none'
    elif value == 1.0:
        return 'few'
    elif value == 2.0:
        return 'some'
    elif value == 3.0:
        return 'many'
    elif value == 4.0:
        return 'a_lot'
    else:
        return 'unknown'

def get_label_sport_facilities(value):
    if value == 0.0:
        return 'low'
    elif value == 1.0:
        return 'medium'
    elif value == 2.0:
        return 'high'
    elif value == 3.0:
        return 'very_high'
    else:
        return 'unknown'

def get_label_tourists_points(value):
    if value == 0.0:
        return 'none'
    elif value == 1.0:
        return 'few'
    elif value == 2.0:
        return 'some'
    elif value == 3.0:
        return 'many'
    elif value == 4.0:
        return 'several'
    elif value == 5.0:
        return 'a_lot'
    else:
        return 'unknown'

def get_label_transportation(value):
    if value == 0.0:
        return 'none'
    elif value == 1.0:
        return 'few'
    elif value == 2.0:
        return 'some'
    elif value == 3.0:
        return 'many'
    else:
        return 'unknown'

def get_label_street_markets_and_fairs(value):
    if value == 0.0:
        return 'none'
    elif value == 1.0:
        return 'few'
    elif value == 2.0:
        return 'some'
    elif value == 3.0:
        return 'many'
    else:
        return 'unknown'

def get_label_rent_price(value):
    if value == 0.0:
        return 'low'
    elif value == 1.0:
        return 'affordable'
    elif value == 2.0:
        return 'medium'
    elif value == 3.0:
        return 'expensive'
    elif value == 4.0:
        return 'very_expensive'
    elif value == 5.0:
        return 'luxurious'
    else:
        return 'unknown'

def get_label_hotels(value):
    if value == 0.0:
        return 'none'
    elif value == 1.0:
        return 'few'
    elif value == 2.0:
        return 'some'
    elif value == 3.0:
        return 'many'
    else:
        return 'unknown'

def get_label_spaces_for_excercise(value):
    if value == 0.0:
        return 'none'
    elif value == 1.0:
        return 'few'
    elif value == 2.0:
        return 'some'
    else:
        return 'unknown'

def get_label_parks_gardens(value):
    if value == 0.0:
        return 'none'
    elif value == 1.0:
        return 'few'
    elif value == 2.0:
        return 'some'
    elif value == 3.0:
        return 'many'
    else:
        return 'unknown'

def get_label_exhebitons_museums(value):
    if value == 0.0:
        return 'none'
    elif value == 1.0:
        return 'few'
    elif value == 2.0:
        return 'some'
    else:
        return 'unknown'

def get_label_music_drinks(value):
    if value == 0.0:
        return 'none'
    elif value == 1.0:
        return 'few'
    elif value == 2.0:
        return 'some'
    elif value == 3.0:
        return 'many'
    elif value == 4.0:
        return 'a_lot'
    else:
        return 'unknown'

def get_label_temporary_exhibitions(value):
    if value == 0.0:
        return 'none'
    elif value == 1.0:
        return 'few'
    elif value == 2.0:
        return 'some'
    elif value == 3.0:
        return 'many'
    else:
        return 'unknown'


# Apply the mapping functions
# df['label_accidents'] = df['label_accidents'].apply(get_label_acc)
# df['label_avg_occ'] = df['label_avg_occ'].apply(get_label_avg_occ)
# df['label_above_65'] = df['label_above_65'].apply(get_label_above_65)
# df['label_academic_level'] = df['label_academic_level'].apply(get_label_accademic)
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
# df['label_rent_price'] = df['label_rent_price'].apply(get_label_rent_price)
# df['label_hotels'] = df['label_hotels'].apply(get_label_hotels)
#df['label_spaces_for_excercise'] = df['label_spaces_for_excercise'].apply(get_label_spaces_for_excercise)
#df['label_parks_gardens'] = df['label_parks_gardens'].apply(get_label_parks_gardens)
#df['label_exhebitons_museums'] = df['label_exhebitons_museums'].apply(get_label_exhebitons_museums)
#df['label_music_drinks'] = df['label_music_drinks'].apply(get_label_music_drinks)
#df['label_temporary_exhibitions'] = df['label_temporary_exhibitions'].apply(get_label_temporary_exhibitions)

# save the data
#df.to_csv('/Users/pierreachkar/Downloads/neighborhood_finder/data/Processed/joined_data/final_table_labeled_cat.csv', index=False)
