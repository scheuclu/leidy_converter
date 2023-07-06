import streamlit as st
import pandas as pd
import numpy as np

st.title('Leidys file combiner')

from io import StringIO


col1, col2 = st.columns([1, 1])
with col1:
    sep = st.selectbox(label="Select Column Separator", options=[",",";"], index=0)
with col2:
    index = st.selectbox(label="What the index of the header row?", options=[0, 1, 2], index=1)

st.markdown("---")
st.markdown("Upload your tables and play with the above parameters until the tables look right.  ")
st.markdown("Then scroll down and click **download** ")


uploaded_file_0 = st.file_uploader("Choose first file", key="uploader0")
if uploaded_file_0 is not None:
    # To read file as bytes:
    bytes_data = uploaded_file_0.getvalue()

    s = str(bytes_data, 'utf-8')
    data = StringIO(s)

    df1 = pd.read_csv(data, header=index, sep=sep)
    st.dataframe(df1)

uploaded_file_1 = st.file_uploader("Choose second file", key="uploader1")
if uploaded_file_1 is not None:
    # To read file as bytes:
    bytes_data = uploaded_file_1.getvalue()

    s = str(bytes_data, 'utf-8')
    data = StringIO(s)

    df2 = pd.read_csv(data, header=index, sep=sep)
    st.dataframe(df2)


st.markdown("---")

if uploaded_file_0 and uploaded_file_1:
    result=pd.concat([df1,df2], sort=False)
    download_button  = st.download_button("Download result", data=result.to_csv().encode('utf-8'), file_name=uploaded_file_0.name)
