import numpy as np
import plotly.express as px
import streamlit as st

from PIL import Image
from streamlit_image_coordinates import streamlit_image_coordinates

st.set_page_config(layout="wide")
st.title('Ink classifier')
c1, c2, c3 = st.columns(3, gap='small')

yrange = [0, 40000]
with c1:
    im = Image.open('./Micrographs/1u.png')
    fig = px.histogram(np.array(im.convert('L')).flatten(), nbins=256, range_y=yrange)
    st.image(im)
    st.plotly_chart(fig)

with c2:
    im = Image.open('./Micrographs/1v.png')
    fig = px.histogram(np.array(im.convert('L')).flatten(), nbins=256, range_y=yrange)
    st.image(im)
    st.plotly_chart(fig)

with c3:
    im = Image.open('./Micrographs/1i.png')
    fig = px.histogram(
        np.array(im.convert('L')).flatten(), nbins=256, range_y=yrange)
    st.image(im)
    st.plotly_chart(fig)