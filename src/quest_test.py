import pandas as pd

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
        "Very important": 2.0,
        "Important": 3.0,
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


#create a dataframe with 20 columns: first one is user_id, the other 19 are the answers to the questions
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

#add a row to the dataframe
df.loc[len(df)] = ['Pierre', 'Highly concerned about safety', 'Prefer a lightly crowded neighborhood', 'yes',
                   'Very important',
                   'Not important at all',
                   'Extremely interested', 'Very important', 'Very important', 'Mildly important',
                   'Very much appreciate',
                   '(920-1200)', 'No, Do not like to exercise outdoors', 'Very important',
                   'Mildly important', 'mostly young people']

print(df.head)


#map each answer to a number based on the dictionary
df = df.replace(mapping_dict)

#save the dataframe to a csv file
#df.to_csv('user_data.csv', index=False)











