import streamlit as st
from PIL import Image


st.title("Moon Camp | Mission Control")

moon = Image.open("moon_base.png")
zoomed = moon.crop((250, 150, 1450, 900))
st.image(zoomed, width="stretch")

