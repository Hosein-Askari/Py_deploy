import streamlit as st 
from PIL import Image

st.title("BMI Calculator") 

w=st.number_input("Weight(kg)")
h=st.number_input("Height(m)")

if w != 0 and h != 0:
    
    result = w/h**2
    
    if result<18.5 :
        st.warning(result)
        img=Image.open("streamlit/bmi_img/1.PNG")
        st.image(img)

    elif 18.5<=result<25 :
        st.success(result)
        img=Image.open("bmi_img/2.PNG")
        st.image(img)

    elif 25<=result<30 :
        st.warning(result)
        img=Image.open("bmi_img/3.PNG")
        st.image(img)

    elif 30<=result<35 :
        st.warning(result)
        img=Image.open("bmi_img/4.PNG")
        st.image(img)

    elif 35<result<40 or result > 40:
        st.error(result)
        img=Image.open("bmi_img/5.PNG")
        st.image(img)
