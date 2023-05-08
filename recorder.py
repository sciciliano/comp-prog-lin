import streamlit as st
from audio_recorder_streamlit import audio_recorder

audio_bytes = audio_recorder()
my_audio=st.audio(audio_bytes, format="audio/wav")
if audio_bytes:
    my_audio
    my_audio.save('my_audio.mp3')
