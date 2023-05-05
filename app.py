import streamlit as st
import json
from PIL import Image
import requests
from streamlit_lottie import st_lottie
import pandas as pd
import numpy as np


#---- define arbetsloshet URL and parse json to dataframe ---
URL_arbetsloshet="https://nav.utvecklingfalkenberg.se/items/arbetsloshet?limit=-1"

    
response = requests.get(URL_arbetsloshet)
if response.status_code == 200:
    json_response = response.text
else:
    st.error(f"Failed to fetch data from {url}. Status code: {response.status_code}")
    json_response = "{}"

# ---- parse the json response ---- 

response_data = json.loads(json_response).get("data", [])

# ---- extract data to DataFrame and column names ----

if response_data:
    data =  [(item["datum"], item["arbetsloshet"]) for item in response_data]
    columns = ("datum", "arbetsloshet")
else:
    data = []
    columns = ()

#---- create a pandas Dataframe ---- 

df = pd.DataFrame(data, columns = columns )


#--- define function for json Lottie file
def url_lottie(url:str):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

#---config the width of the page---

st.set_page_config(page_title="Palles python website using Streamlit", page_icon=":tada:", layout="wide")


#---- HEADER SECTION ----
with st.container():
    st.subheader("Hello Streamlit, :wave:")
    st.title("a beginner programmer, just curious enough to learn to code (a little...)")
    st.write("I am curious about many things, so I rarely get myself deep enough into anything before I like to jump into the next exciting thing to learn:-)")


#---- 2 columns with TEXT and IMAGE SECTION ----
with st.container():
    st.write("---")
    left_column, right_column=st.columns(2)

    with left_column:
        st.header("I have just discovered Midjourney")
        st.markdown("##")
        st.markdown(
            """
            **Table of contents**  
                * Prerequisites  
                * Install Streamlit on Windows  
                * Install Streamlit on macOS/Linux  
            """
            )

    with right_column:
        image_path = 'images/image1.png'
        image = Image.open(image_path)
        st.image(image, caption="supernova of tropical fruits, kirigami (midjourney v5")

#---- DIVIDER -----
st.divider()
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        lottie_json = url_lottie("https://assets3.lottiefiles.com/packages/lf20_w51pcehl.json")
        st_lottie(
            lottie_json,
            speed=2
        )   
                 
    with col2: 
        st.markdown(
            """
                - random text 1          
                - random text 2
                - random text 3
            """
        )

st.divider()

#---- preprocess the data for the line chart
df = pd.DataFrame(data, columns = ['datum', 'arbetsloshet'])
df['datum'] = pd.to_datetime(df['datum'])
df.set_index('datum', inplace=True)



#---- insert dataframe and line chart ---- 
colA, colB, colC = st.columns(3)
with colA:
        st.write('   ')
with colB:
        st.subheader( 'This is a table and a line chart showing arbetsloshet')
with colC:
        st.write('   ')

        


with st.container():
    left_column2, right_column2 = st.columns([1, 3])

with left_column2:
        st.write(df)

with right_column2:
        st.line_chart(df, height = 500)


#st.write("#") = line with some extra space

#st.write("---") = st.divider()
