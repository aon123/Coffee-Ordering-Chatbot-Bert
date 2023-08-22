
# Coffee Ordering Chatbot using Bert

### Summary

Artificial Intelligence is rapidly getting into the workflow of many businesses across various industries. Due to the advancements in Natural Language Processing (NLP), Natural Language Understanding (NLU), and Deep Learning (DL), we are now able to develop technologies capable of imitating human-like interactions which include recognizing speech, as well as text. This project is designed to solve Coffee ordering process by implementing chatbots.

---

### Background Study

A chatbot is a name given to a software application or service that replicates human-to-human interactions. This is usually achieved through artificial intelligence and machine learning, which allows the chatbot to interpret communication from a human user and respond in a seemingly intelligent way. With this in mind, a coffee chatbot is a service that allows customers to ask questions or make requests without the need for a human staff member to respond. Coffee chatbots are specifically designed with coffee customers in mind and so respond appropriately to the most common queries.

---

### Project Goal

The main goal of chatbot is to reduce the waiting time for customers. It allows the users to skip lengthy lines for morning coffee. And it will also help coffee shops to efficiently make customers order while not being distructed to get orders directly. 

---

### Related Research

#### Transformers

Transformers are a type of artificial neural network architecture that is used to solve the problem of transduction or transformation of input sequences into output sequences in deep learning applications. Google introduced the transformer architecture in the paper “Attention is All you need”. The transformer uses a self-attention mechanism, which is suitable for language understanding. The transformer has an encoder-decoder architecture. They are composed of modules that contain feed-forward and attention layers.

![alt text](https://miro.medium.com/max/1400/1*BHzGVskWGS_3jEcYYi6miQ.png)

#### BERT (Bidirectional Encoder Representations from Transformers)

 BERT uses bidirectional training i.e it reads the sentence from both directions to understand the context of the sentence. Note that BERT is just an encoder. It does not have a decoder.

#### Text To Speech & Speech To Text

gTTS (Google Text-to-Speech)\
The Text-to-Speech API enables developers to generate human-like speech. The API converts text into audio formats such as WAV, MP3, or Ogg Opus. It also supports Speech Synthesis Markup Language (SSML) inputs to specify pauses, numbers, date and time formatting, and other pronunciation instructions.

Whisper Openai\
Whisper is an automatic speech recognition (ASR) system trained on 680,000 hours of multilingual and multitask supervised data collected from the web.

#### Application

#### Server - Flask
Flask is a web framework, it’s a Python module that lets you develop web applications easily. It’s has a small and easy-to-extend core: it’s a microframework that doesn’t include an ORM (Object Relational Manager) or such features.

#### Database - Mongodb
MongoDB is an open source NoSQL database management program. NoSQL is used as an alternative to traditional relational databases. 

#### Frontend - Flutter application

Flutter is an open source framework by Google for building beautiful, natively compiled, multi-platform applications from a single codebase.


---

### Architecture 


#### Coffee ordering Chatbot

##### Dataset

Dataset contains of 4 classes and each class contains 1000 sentences.



##### Training accuracy - accuracy:  86.4 %
##### Test accuracy - accuracy:  83.75 %



### Problem & Solution

After training model i get 83% accuracy to recognize user intent. This was good enough to build script based chatbot. But to build fully independant chatbot we need more data.
To solve this i build script based chatbot and saved user conversation by intent to database after some period of collecting data we can increase accuracy and retrain model to fully operate by its own.

---

#### Conclusion

Coffee ordering chatbot will help many coffee businesses to improve their customer service. And it will reduce waiting time for customers. So it is crucial to implement high quality chatbots. In order to accomplish this quality we need more data.
