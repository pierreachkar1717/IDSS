
import streamlit as st
import pandas as pd


def main():
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

    

if __name__ == '__main__':
    main()
