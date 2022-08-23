from cgitb import text
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')


#st.write('DataFrame')

#df = pd.DataFrame({
#    '1retume':[1,2,3,4],
#    '2retume':[50,20,30,40]
#})

#st.write(df)
#st.dataframe(df.style.highlight_max(axis=0))#, width=100, height=100)
#st.table(df.style.highlight_max(axis=0))#, width=100, height=100)

#
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

#df = pd.DataFrame(
#    np.random.rand(20, 3),
#    columns=['a', 'b', 'c']
#)

#st.area_chart(df)

#df = pd.DataFrame(
#    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#    columns=['lat', 'lon']
#)

#st.map(df)

#st.write('Display Image')

#if st.checkbox('Show Image'):

#    img = Image.open('1.jpg')
#    st.image(img, caption='pressure gage', use_column_width=True)

#option = st.selectbox(
#   'あなたが好きな数字を入力してください',
#    list(range(1,11))
#)

#'あなたの好きな数字は、', option , 'です'


st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)



# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラムです')

# expander1 = st.expander('問い合わせ')
# expander1.write('問い合わせ内容を書く')
# expander2 = st.expander('問い合わせ')
# expander2.write('問い合わせ内容を書く')
# expander3 = st.expander('問い合わせ')
# expander3.write('問い合わせ内容を書く')


# text = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'あなたの趣味は', text, 'です'
# 'コンディション：', condition