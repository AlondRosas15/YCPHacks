#creating a web app for MLH, would have a recruiter/sponsor, sponsored hack links, and workshop navigation 
import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np


hackathon = 'YCP hackathon '

st.set_page_config(

    page_title=f"{hackathon} - Machine Learning Hackathons",

    page_icon = "🖥️"
)


st.title('MLH Navigate')
st.header('Welcome Hackers!')
st.subheader('Your journey starts here!')

st.write("Here is your one way stop to " +hackathon+ "'s resources")

#schedule here
st.sidebar.success("Select the pages above")

st.write("[Devpost](https://devpost.com)")
st.write('Communication:')

#add mlh-logo-color.png
#image = Image.open('src\mlh-logo-color.jpg')
#st.image(image)

st.write("🔮🤖☀️👨‍💻🤍🦾🚀")

def anonymous_feedback():
    st.subheader('How was your experience?')
    options = ['Very good', 'Good', 'Average', 'Poor', 'Very poor']
    selected_option = st.selectbox('Please select an option:', options)

    if selected_option != '':
        with st.form(key='anonymous_feedback'):
            st.text_input('Any additional feedback?', key='feedback')
            st.form_submit_button('Submit')

if __name__ == '__main__':
    anonymous_feedback()
