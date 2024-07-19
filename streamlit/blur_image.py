import cv2
import numpy as np
from PIL import Image
import streamlit as st


st.title("Blur Image")

upload_file = st.file_uploader("upload image",type=["jpg","png","jpeg"])


if upload_file is not None :
    img = Image.open(upload_file)
    st.success("file upload successfully")
    st.image(upload_file)

    img = np.array(img)
    img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    blur_amount=st.slider("How much blue, do you want?",1,199,10,step=2)
    img = cv2.blur(img,(blur_amount,blur_amount))
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    st.image(img)


else:
    st.error("nothing has uploaded yet")