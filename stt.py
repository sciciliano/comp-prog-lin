import speech_recognitions as sr

r = sr.Recognizer()
file = st.file_uploader("Upload file", type=['wav'])
with sr.AudioFile(file) as source:
    audio= r.record(source)

recognized_text = r.recognize_google(audio)
print(recognized_text)
