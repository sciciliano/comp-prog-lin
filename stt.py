import streamlit as st
import speech_recognition as sr

r = sr.Recognizer()
file = st.file_uploader("Upload file", type=['wav'])
with sr.AudioFile(file) as source:
    audio= r.record(source)

recognized_text = r.recognize_google(audio)
st.write(recognized_text)
