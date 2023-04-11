import json, requests
from googletrans import Translator
import streamlit as st

translator = Translator()
word = st.text_input('ask me a word: ','')
target_language = st.selectbox('Please select a language: ',('it','en','de','es'))

if (language and keyword):
  target_word = translator.translate(word ,dest=target_language)
  st.write(target_word)
