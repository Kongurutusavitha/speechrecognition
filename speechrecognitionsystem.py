import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Load your audio clip
with sr.AudioFile("d:\sample-15s.wav") as source:
    audio = recognizer.record(source)  # read the entire file

# Try recognizing the speech
try:
    text = recognizer.recognize_google(audio)
    print("Transcribed text:\n", text)
except sr.UnknownValueError:
    print("Could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
