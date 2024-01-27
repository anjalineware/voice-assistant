# -*- coding: utf-8 -*-
"""voice assistant.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15FAcRLiPBRT-GQHAoy1-K5l9FHZ1dKVg
"""

!pip install -q -U google-generativeai

pip install gTTS

import pathlib
import textwrap

import google.generativeai as genai
from gtts import gTTS

from IPython.display import display
from IPython.display import Markdown
from IPython.display import Audio, display


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key=GOOGLE_API_KEY)

from google.colab import userdata
GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')
model = genai.GenerativeModel('gemini-pro')

def ask_que(name):
  ques = 'Hey ' + name + ' How can I help you? '
  ques = input(ques)
  return ques

ask_que("jay")

from re import T
def classify_que(ques):
  device_list = ['alarm', 'reminder', 'message', 'call']
  personal_list = ['who are you', 'who created you']

  device = False
  for i in device_list:
    if i in ques:
      device = True

  if device:
    print("this question is related to device things, not supported")

  personal_que = False
  for i in personal_list:
    if i in ques.lower():
      personal_que = True

    if personal_que:
      print("Hey am an personal assistant created by tony stark")

    if device:
      doweb_search = False
    elif personal_que:
      doweb_search = False
    else:
      doweb_search = True

    return doweb_search

classify_que("Who are you?")

def ask_gemini(ques):
  modifed_prompt = 'Hey give me answer to this question ' + ques + ' in maximum of 40 words'
  response = model.generate_content(modifed_prompt)

  return response.text

def speak(ans):
    tts = gTTS(ans)
    tts.save('audio.mp3')
    display(Audio('audio.mp3', autoplay=True))

more_ques = 'yes'
name = ''

while more_ques == 'yes':

  if name == '':
    name = input("Hey, whats your name? - ")

  q = ask_que(name)

  go_ahead = classify_que(q)
  ans = ''

  if go_ahead == True:
    ans = ask_gemini(q)
    speak(ans)
    print(ans)

  more_ques = input("Do you have any other questions? yes or no ")

