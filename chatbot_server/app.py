from flask import Flask, jsonify, redirect, render_template, request
from db import *
import string
import random
from gtts import gTTS
import os
from io import BytesIO
import pygame



app = Flask(__name__)


def speak(text, language='en'):
    mp3_fo = BytesIO()
    tts = gTTS(text, lang=language, slow=False)
    tts.write_to_fp(mp3_fo)
    return mp3_fo
    

def botSpeak(text):
    pygame.init()
    pygame.mixer.init()

    sound = speak(text)
    pygame.mixer.music.load(sound, 'mp3')
    pygame.mixer.music.play()


def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@app.get('/')
def home():
    return jsonify({"message": "Hello Welcom to chatbot API"})


@app.post('/create/menu')
def create_menu():
    data = request.get_json()
    data['_id'] = id_generator(10)
    menuDB.insert_one(data)
    return jsonify(data)

@app.post('/delete/menu')
def delete_menu():
    data = request.get_json()
    menuDB.delete_one({"_id": data['_id']})
    x = menuDB.find({})
    data = [i for i in x]
    return jsonify({"message": "successfully deleted", "data": data})

@app.get('/menu')
def get_menu():
    x = menuDB.find({})
    data = [ i for i in x]
    return jsonify(data)

@app.get('/menu/<string:id>')
def menu_by_id(id):
    data = menuDB.find_one({"_id": id})
    return jsonify(data)


@app.post('/make/order')
def make_order():
    data= request.get_json()
    data['_id'] = id_generator(4)
    orderDB.insert_one(data)
    return jsonify(data)

@app.get('/order')
def get_order():
    x = orderDB.find({})
    data = [i for i in x]
    return jsonify(data)


@app.post("/save/chatbot")
def chatbot_save():
    data = request.get_json()
    data['_id'] = id_generator()
    chatbotDB.insert_one(data)
    return jsonify(data)

@app.get('/chatbot')
def get_chatbot():
    x = chatbotDB.find({})
    data = [i for i in x]
    return jsonify(data)


@app.post('/ready')
def check_ready():
    print('ready')
    data = request.get_json()
    print(data)
    orderDB.update_one({"_id": data['_id']},{"$set": {'status': 'Ready'}})
    order = orderDB.find_one({"_id": data['_id']})
    x = orderDB.find({})
    data = [i for i in x]
    bot = f"Order with {order['_id']} is ready! Please take your order! Thank you!"
    botSpeak(bot)
    return jsonify(data)


if __name__ =='__main__':
    app.run(host="0.0.0.0", port=3000)