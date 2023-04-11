import pyttsx3
import json, requests
import base64
import streamlit as st
from googletrans import Translator

engine = pyttsx3.init()
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )

translator = Translator()
input_str = st.text_input('type here some text!\t')
input_lang = st.selectbox('type the language',('en','de','it','es'))
trans_str= translator.translate(input_str, dest= input_lang)
engine.say(trans_str)


if (trans_str and input_lang):
    autoplay_audio(engine.say(trans_str))
