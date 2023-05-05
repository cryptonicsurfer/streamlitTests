import streamlit as st
import cv2
import requests
import numpy as np
from PIL import Image
from io import BytesIO
import tempfile

def load_image(input_path):
    if input_path.startswith("http"):
        response = requests.get(input_path)
        img = Image.open(BytesIO(response.content))
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    else:
        img = cv2.imread(input_path)

    return img

def lineApp(img, lower, upper, line_color, bg_color):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    edges = cv2.Canny(blur, lower, upper)

    colored_edges = np.zeros_like(img)
    colored_edges[np.where(edges != 0)] = line_color
    colored_edges[np.where(edges == 0)] = bg_color

    return colored_edges

st.set_option("deprecation.showfileUploaderEncoding", False)
st.title("Line Drawing App")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "bmp"])
image_url = st.text_input("Or paste an image URL")

if uploaded_file or image_url:
    if uploaded_file:
        img = Image.open(uploaded_file)
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    else:
        img = load_image(image_url)
    st.image(img, caption="Original Image", use_column_width=True)

    lower_threshold = st.slider("Lower Threshold", 0, 255, 100)
    upper_threshold = st.slider("Upper Threshold", 0, 255, 150)
    line_color = st.color_picker("Line Color", "#000000")
    bg_color = st.color_picker("Background Color", "#FFFFFF")

    result = lineApp(img, lower_threshold, upper_threshold, tuple(int(line_color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4)), tuple(int(bg_color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4)))
    st.image(result, caption="Line Drawing", use_column_width=True)

    if st.button("Download Image"):
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
        cv2.imwrite(temp_file.name, result)
        st.markdown(f"[Download Image]({temp_file.name})", unsafe_allow_html=True)
else:
    st.write("Please upload an image or provide an image URL.")
