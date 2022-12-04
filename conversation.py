from test_model import *
import speech_recognition as sr
from gtts import gTTS
import os
from io import BytesIO
from stt import recordVoice
import pygame
import time
import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from db import *
import requests
from datetime import datetime

recognizer = sr.Recognizer()


def speak(text, language='en'):
    mp3_fo = BytesIO()
    tts = gTTS(text, lang=language, slow=False)
    tts.write_to_fp(mp3_fo)
    return mp3_fo
    


def userSpeak():
    text = recordVoice()
    result = get_prediction(text)
    return result, text


text = ""

def botSpeak(text):
    pygame.init()
    pygame.mixer.init()

    sound = speak(text)
    pygame.mixer.music.load(sound, 'mp3')
    pygame.mixer.music.play()



x = menuDB.find({})
product = [i['name'] for i in x]
sizes = ['medium', 'large', 'small']

conversation = {}
order = {}
while text != 'q':
    conversation = {}
    order = {}
    bot = "Hello welcome to Starbucks"
    botSpeak(bot)
    time.sleep(3)
    result, text = userSpeak()
    name = ""
    for i in text.replace('?', '').split():
        for j in product:
            if  fuzz.ratio(i.lower(), j.lower())>90:
                name = j.lower()
    print(name)
    if labels[result] == 'greeting':
        conversation['greeting'] = text
        bot = "What you want to order?"
        botSpeak(bot)
        time.sleep(3)
        result, text = userSpeak()
        name = ""
        for i in text.replace('?', '').split():
            for j in product:
                if  fuzz.ratio(i.lower(), j.lower())>90:
                    name = j.lower()
        if name != '':
            if labels[result] == 'order':
                conversation['order'] = text
                bot = "What size do you want? We have large, medium and small."
                botSpeak(bot)
                time.sleep(5)
                result, text = userSpeak()
                
                #Check if size exist in sized list
                size = ''
                for i in text.replace(',', '').split():
                    for j in sizes:
                        if  fuzz.ratio(i.lower(), j.lower())>90:
                            size = j.lower()
                if size != '':
                    if labels[result] == 'size':
                        conversation['size'] = text
                        bot = f"You ordered {size} {name}. Please wait until we prepare your order"
                        botSpeak(bot)
                        order['name'] = name
                        order['size'] = size
                        order['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        order['status'] = 'Processing'
                        time.sleep(5)
                        result, text = userSpeak()
                        if labels[result] == 'thank':
                            conversation['thank'] = text
                            bot = "Thank you for choosing us! Have a wonderful day!"
                            botSpeak(bot)
                            time.sleep(5)

                            text = 'q'
                        else:
                            bot = "Thank you for choosing us! Have a wonderful day!"
                            botSpeak(bot)
                            time.sleep(5)
                            text = 'q'
                    else:
                        bot = "Sorry I didn't understand what you mean!"
                        botSpeak(bot)
                        time.sleep(5)
                else:
                    bot = "Sorry I didn't understand what you mean!"
                    botSpeak(bot)
                    time.sleep(5)    
            else:
                bot = "Sorry I didn't understand what you mean!"
                botSpeak(bot)
                time.sleep(5)    
        else:
            bot = "Sorry we don't have that product in our menu!"
            botSpeak(bot)
            time.sleep(5)

    elif labels[result] == 'order':
        if name != '':
            if labels[result] == 'order':

                bot = "What size do you want? We have large, medium and small."
                botSpeak(bot)
                time.sleep(5)
                result, text = userSpeak()
                
                #Check if size exist in sized list
                size = ''
                for i in text.replace(',', '').split():
                    for j in sizes:
                        if  fuzz.ratio(i.lower(), j.lower())>90:
                            size = j.lower()
                if size != '':
                    if labels[result] == 'size':
                        bot = f"You ordered {size} {name}. Please wait until we prepare your order"
                        botSpeak(bot)

                        time.sleep(5)
                        result, text = userSpeak()
                        if labels[result] == 'thank':
                            bot = "Thank you for choosing us! Have a wonderful day!"
                            botSpeak(bot)
                            time.sleep(5)
                            text = 'q'
                        else:
                            bot = "Thank you for choosing us! Have a wonderful day!"
                            botSpeak(bot)
                            time.sleep(5)
                            text = 'q'
                    else:
                        bot = "Sorry I didn't understand what you mean!"
                        botSpeak(bot)
                        time.sleep(5)
                else:
                    bot = "Sorry I didn't understand what you mean!"
                    botSpeak(bot)
                    time.sleep(5)    
            else:
                bot = "Sorry I didn't understand what you mean!"
                botSpeak(bot)
                time.sleep(5)    
        else:
            bot = "Sorry we don't have that product in our menu!"
            botSpeak(bot)
            time.sleep(5)
    else:
        bot = "Please start conversation with greeting or ordering"
        botSpeak(bot)
        time.sleep(5)

requests.post('http://172.30.1.35:3000/make/order', json=order)
requests.post('http://172.30.1.35:3000/save/chatbot', json=conversation)
