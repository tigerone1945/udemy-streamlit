import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Image')

img = Image.open('/Users/maedayouzou/Desktop/UdemyLesson/Python/今西/Webアプリ開発/IMG_0062.jpg')
st.image(img, caption='Brompton 2L-X', use_column_width=True)

st.write('Data Frame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

#st.write(df)
#st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)
st.table(df)

#"""
# 章
## 節
### 項
#```python
#import streamlit as st
#import numpy as np
#import pandas as pd
#```
#"""

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a', 'b', 'c']
)

st.write('折れ線グラフ')
st.line_chart(df)

st.write('面グラフ')
st.area_chart(df)

st.write('棒グラフ')
st.bar_chart(df)

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df)