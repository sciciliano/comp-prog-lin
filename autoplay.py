from gtts import gTTS
import json, requests
import base64
import streamlit as st
from googletrans import Translator

translator = Translator()
input_str = st.text_input('type here some text!\t')
input_lang = st.selectbox('type the language',('en','de','it','es'))
trans_str= translator.translate(input_str, dest= input_lang)
tts1=gTTS(text= trans_str.text, lang= input_lang)
tts1.save('helloworld.mp3')

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

if (trans_str and input_lang):
    autoplay_audio(audio_file)
