import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Iteractive Widgets')

if st.checkbox('Show Image'):
    img = Image.open('/Users/maedayouzou/Desktop/UdemyLesson/Python/今西/Webアプリ開発/IMG_0062.jpg')
    st.image(img, caption='Brompton 2L-X', use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)

'あなたの好きな数字は、',option,'です'

text = st.text_input('あなたの趣味はなんですか？')
'あなたの趣味：', text

condition = st.slider('あなたの今の調子は？',0, 100, 50)
'コンディション:',condition