from gtts import gTTS
import json, requests
import streamlit as st
from googletrans import Translator
import IPython.display as ipd  

translator = Translator()
input_str = st.text_input('type here some text!\t')
input_lang = st.selectbox('type the language',('en','de','it','es'))
trans_str= translator.translate(input_str, dest= input_lang)
tts1=gTTS(text= trans_str.text, lang= input_lang)
tts1.save('helloworld.mp3')
if (trans_str and input_lang):
    audio_file = open('helloworld.mp3','rb')
    st.audio(data=audio_file, format="audio/mp3", start_time=0)
