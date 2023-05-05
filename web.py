import streamlit as st
import requests
from PIL import Image




#---- set up page configuration ----- 

st.set_page_config('Page built with Streamlit', layout="wide")
st.title('This is a title')

st.divider()

col1, col2 = st.columns(2)

with col1:
    image_path = 'images/image1.png'
    image = Image.open(image_path)
    st.image(image, caption="supernova of tropical fruits, Midjourney v5")

with col2:
    st.subheader('Midjourney can create awesome art')
    st.markdown("""
                    **This is what you need to think of:  
                        * be specific, object, angle, lighting, shadows, level of detail etc  
                        * be creative, mix and match
                        * techniques, you can make it pixelated, kirigami, pointilism
                        * aspect ratio
                """
    )


    

