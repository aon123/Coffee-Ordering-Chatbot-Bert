from pymongo import MongoClient


client = MongoClient("mongodb://plant:plant2022@43.201.136.217:27017/chatbot",authSource="admin")
db = client.chatbot
chatbotDB = db.chatbot
menuDB = db.menu
orderDB = db.order

