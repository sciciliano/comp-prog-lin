import streamlit as st
import json, requests
from googletrans import Translator

translator = Translator()
input_txt = st.file_uploader("Upload file", type=['txt'])
input_str = input_txt.getvalue().decode("utf-8")
input_lang = st.selectbox('type the language',('en','de','it','es'))
trans_str= translator.translate(input_str, dest= input_lang)
output = trans_str.text

if (trans_str and input_lang):
  st.write(output)
st.download_button(label="Download your translated file", data=output, file_name='transfile.txt',mime='text/txt')
