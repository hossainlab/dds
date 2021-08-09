import streamlit as st
from multiapp import MultiApp
from apps import home, diabetes, heart,  liver # import your app modules here


app = MultiApp()

st.set_page_config(layout="wide", page_title="CHIRAL-DDS")
# Add all your application here
app.add_app("Home", home.app)
app.add_app("Diabetes", diabetes.app)
app.add_app("Heart Diseases", heart.app)
app.add_app("Liver Diseases", liver.app)


# The main app
app.run()
