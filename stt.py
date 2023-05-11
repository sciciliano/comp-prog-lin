import streamlit as st
import speech_recognition as sr
from audio_recorder_streamlit import audio_recorder

audio_bytes = audio_recorder()
my_audio=st.audio(audio_bytes, format="audio/wav")
if audio_bytes:
    my_audio
    my_audio.save('my_audio.mp3')
    
r = sr.Recognizer()
with 'my_audio.mp3' as source:
    audio= r.record(source)

recognized_text = r.recognize_google(audio)
st.write(recognized_text)
