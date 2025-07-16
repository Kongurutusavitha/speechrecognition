# speechrecognition

Company:CODTECH IT SOLUTIONS

NAME:K SAVITHA

INTERN ID:CT06DF1652

Domain Name:Artificial Intelligence

Duration:6 weeks

Mentor name: Neela Santhosh

Project Description:
The Speech-to-Text Transcription Tool is a Python-based project designed to convert spoken audio into written text using speech recognition technology. This application utilizes the Google Speech Recognition API through the speech_recognition library in Python to automatically transcribe the content of a WAV audio file into human-readable text. It is particularly useful for converting voice notes, interviews, lectures, podcasts, or any voice recordings into written form, enhancing accessibility and enabling further text analysis or storage.

The core of the project involves processing an audio file and using Google's cloud-based automatic speech recognition (ASR) engine to interpret the spoken words. Upon successful recognition, the transcribed text is printed to the console. If the audio is unclear or the service is unavailable, the tool gracefully handles errors and informs the user accordingly.
The project follows a simple yet powerful workflow:

Load a WAV format audio file.

Use the speech_recognition library to read and process the audio.

Send the audio data to the Google Speech Recognition service.

Receive the transcribed text or appropriate error messages.

This tool is ideal for developers learning about speech processing, researchers looking to preprocess spoken content, or general users aiming to automate voice-to-text tasks. The design emphasizes ease of use, portability, and fast deployment without needing complex machine learning models or training data.

🛠️ Tools & Technologies Used:
Python 3

Python is the primary programming language used for scripting and logic. Its readability and extensive library ecosystem make it ideal for prototyping speech-related applications.

speech_recognition Library

A high-level Python package that supports multiple speech APIs. In this project, it serves as a wrapper for Google Speech Recognition, handling audio loading, recording, and converting to text.

Supports both online (Google, IBM, etc.) and offline (CMU Sphinx) recognition engines.

Google Web Speech API

A cloud-based service provided by Google that converts audio into text using advanced machine learning and natural language processing (NLP) models. It is free for moderate usage and doesn’t require extensive setup, making it perfect for small projects.

WAV Audio File

The tool uses .wav audio format for input. WAV is widely supported and uncompressed, providing high-quality audio which improves transcription accuracy.

Error Handling with Try-Except

Custom error messages are displayed if the recognition fails due to audio clarity or API issues, ensuring a user-friendly experience.

OUTPUT

<img width="800" height="250" alt="Image" src="https://github.com/user-attachments/assets/e4e13d9e-ee82-41b3-be4e-a31570e11e49" />

