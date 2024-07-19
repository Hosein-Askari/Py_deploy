import pandas as pd
import streamlit as st
import numpy as np



upload_file = st.file_uploader("upload your dataset file",type=["csv"])


if upload_file is not None :
    df = pd.read_csv(upload_file)
    st.success("file upload successfully")
    st.write(df)
    df= pd.DataFrame(df)
    if len(df.keys())>1:
        

        st.bar_chart(df,height=400,width=800,use_container_width=True,x=df.keys()[0])
    else:
        st.bar_chart(df,height=400,width=800,use_container_width=True)
    


else:
    st.error("nothing has uploaded yet")


with    st.sidebar :
    st.info("simple app for showing chart of csv files!")