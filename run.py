

#Importing modules

import time
time.clock = time.time
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)


# CREATING CHATBOT

chatbot = ChatBot("My Bot" ,storage_adapter="chatterbot.storage.SQLStorageAdapter")

# TRAINING THE BOT
bot_trainer = ChatterBotCorpusTrainer(chatbot)
bot_trainer.train("chatterbot.corpus.english")

while True:
    user = input("you : ")
    if user =="Exit" :
        break
    bot_response = chatbot.get_response(user)
    print("bot : ", bot_response)


