import json, requests
from googletrans import Translator
import streamlit as st

translator = Translator()
word = st.text_input('ask me a word: ','')
target_language = st.selectbox('Please select a language: ',('it','en','de','es'))
target_word = st.write(translator.translate(word ,dest=target_language))
