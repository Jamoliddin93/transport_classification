import streamlit as st
from fastai.vision.all import *
from fastai.learner import CastToTensor
import plotly.express as px
import pathlib
import platform

plt = platform.system()
if plt=='Linux':pathlib.WindowsPath = pathlib.PosixPath

st.title('Transportni klassifikatsiya qiluvchi model')

file = st.file_uploader('Upload', type=['png','jpeg','gif','svg'])

if file:

    st.image(file)

    img = PILImage.create(file)

    model = load_learner('transport_model.pkl')

    pred, pred_id, probs = model.predict(img)
    st.success(f'Bashorat: {pred}')
    st.info(f'Ehtimollik: {probs[pred_id]*100:.1f}%')

    fig = px.bar(x=probs*100, y=model.dls.vocab)
    st.plotly_chart(fig)
