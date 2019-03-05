#google text to speech api
from gtts import *
import gtts
import os
tts = gtts.gTTS(text='Hello World', lang='en')
tts.save("hello.mp3")
os.system("mpg321 hello.mp3")
