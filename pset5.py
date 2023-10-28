import streamlit as st
from PIL import Image

st.title('How Are You Feeling Today?')

choice = st.radio("Are You a Dog or a Cat Person?", ["Cat :cat:", "Dog :dog:"])
if choice == "Cat :cat:":
    preference = 'cat'
elif choice == "Dog :dog:": 
    preference = 'dog'

selection = st.selectbox('Select your current emotion:',("Happy", "Sad", "Angry", "Silly"))

if selection == "Happy":
    text = "Keep up the good mood!"
    img = Image.open(f'images/happy{preference}.jpg')
elif selection == "Sad":
    text = "Hang in there!"
    img = Image.open(f'images/sad{preference}.jpg')
elif selection == "Angry":
    text = "You should calm down."
    img = Image.open(f'images/angry{preference}.jpg')
elif selection == "Silly":
    text = "What are you thinking about?"
    img = Image.open(f'images/silly{preference}.jpg')

col1, col2, col3 = st.columns(3)

if st.button('Give me an Image!'):
    with col2:
        st.write(text)
        st.image(img)