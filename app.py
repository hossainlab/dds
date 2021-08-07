import streamlit as st
from multiapp import MultiApp
from apps import home, diabetes, heart,  liver # import your app modules here

app = MultiApp()

st.markdown("""
# CHIRAL Diseases Detection System (CHIRAL-DDS)
 By [Md. Jubayer Hossain]()
 
This project aims to help doctors or medical professionals make data-driven decisions in health care, and they can easily detect patients with the disease. 
""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Diabetes", diabetes.app)
app.add_app("Heart Diseases", heart.app)
app.add_app("Liver Diseases", liver.app)



# The main app
app.run()
