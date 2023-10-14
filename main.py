from gtts import gTTS
import os

text =  "Goodmorning,It's 8:00am London time.Today I'll be coding with Python."\
        "Python is a vast language,but I'm doing all I can to learn everyday."\
        "I'll be having coffee later so I don't burn out."\
        "My program is great!It says what I've written."

language = 'en'
tts = gTTS(text=text, lang=language, slow=False)
tts.save("output.mp3")
os.system("afplay output.mp3")
