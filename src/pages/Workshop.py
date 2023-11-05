import streamlit as st
import streamlit_survey as ss
import random

st.set_page_config(

    page_title=f"Workshop",

    page_icon = "🛠️"
)
st.title("Which Workshop you should check out!")

st.sidebar.success("Don't know which one to go? Let us help!")

#make a recommendation test that based on what user choice of buttons gives them an answer of recommendation such Machine Learning', 'Post Grad', 'Surprise me
survey = ss.StreamlitSurvey();
begin_sent = 'You should check out'

st.write("What interest you the most")
recommendation_list =  ['Fire Spinning', 'Basic Machine Learning', 'Git Workshop', 'How to Stick a Computer in a Bowling Ball']

choices = ["Machine Learning", "Post Grad", "Surprise me!"]
option = st.radio("Select your option", choices)
if option == "Machine Learning":
    recommendation = " the Basic Machine Learning workshop is the perfect choice for you"
elif option == "Post Grad":
    recommendation = " the Post Grad workshop is a great choice if you are considering a graduate program or internships"
else:
    recommendation = random.choice(recommendation_list)

st.write(begin_sent + " " + recommendation + "!")

st.markdown("![](https://media.giphy.com/media/4TrKGDZrcugHAt2VBc/giphy.gif)")
