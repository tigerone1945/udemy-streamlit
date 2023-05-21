import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!!'

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!'


if st.checkbox('Show Image'):
    img = Image.open('/Users/maedayouzou/Desktop/UdemyLesson/Python/今西/Webアプリ開発/IMG_0062.jpg')
    st.image(img, caption='Brompton 2L-X', use_column_width=True)

left_column, right_column = st.columns(2)
button =left_column.button('右からむに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせの回答')

#text = st.text_input('あなたの趣味はなんですか？')
#'あなたの趣味：', text

#condition = st.slider('あなたの今の調子は？',0, 100, 50)
#'コンディション:',condition