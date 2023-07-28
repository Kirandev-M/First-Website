import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image


st.set_page_config(page_title="My Test Website", page_icon=":tada:",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use Local CSS

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style\style.css")


#---------LOAD ASSETS-----

lottie_anime = load_lottieurl("https://lottie.host/09f94b11-c355-4e99-9d4c-c760659a7520/TpPEpwR8kH.json")
DB_cooper = Image.open("db cooper.jpg")
#-----------Header Section-------
with st.container():
    st.subheader("Hi, I am Kiran :wave:")
    st.title("A Electrical Engineering Student")
    st.write("I am trying to see ways I can create a website with python")
    st.write("[Python](https://www.python.org/)")

#--------WHAT I DO-------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write("""
                   I am trying to see ways I can create a website with python
                   - trying different projects to understand python more 
                   -made a reddit tiktok video from python
                   -trying to make it a reddit video bot
                   """)
        st.write("[Click Here for Youtube Channel!](https://www.youtube.com/channel/UC5k9oTE_BPpqeqgCst9BaBg)")
    with right_column:
        st_lottie(lottie_anime, height = 300, key= "anime")
with st.container():
    st.write("---")
    st.header("My Videos")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(DB_cooper)
    with text_column:
        st.subheader("True Crime: DB Cooper")
        st.write(""" 
                Watch as we delve into the bizare case of DB Cooper!      
                True Crime investigation of the man who disappeared.    

                    """)
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=b5NN5BTsX-k)") 

#----CONTACT-------
with st.container():
    st.write("---")
    st.header("Get In Touch With Me")
    st.write("##")


    contact_form = """
    <form action="https://formsubmit.co/kirandevmanoharan@ehotmail.com" method="POST">
        <input type ="hidden" name="_captcha" value = "false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()       