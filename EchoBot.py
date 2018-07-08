import telebot #telegram library for python
import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot('Ron Obvious',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    logic_adapters = ['chatterbot.logic.MathematicalEvaluation',
                     {
                    'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                    'input_text': 'Access Database',
                    'output_text': 'Ok, here is a link: http:127.0.0.1:5000/'
                    },
                    {
                    'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                    'input_text': 'How can I help',
                    'output_text': 'You can do donations like time, money, human resource, kind donations.'
                    },
                    {
                    'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                    'input_text': 'How can I donate',
                    'output_text': 'Contact http://www.cwfglobal.org'
                    },
                    {
                    'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                    'input_text': 'How long will it take to acheive the desired progress',
                    'output_text': 'It may take around 4 months to 1 year to achieve the desrired progress'
                    },
                    {
                    'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                    'input_text': 'How many schools have you adopted',
                    'output_text': 'Currently we have adopted around 15 schools'
                    },
                    {
                    'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                    'input_text': 'How much time needs to be spent',
                    'output_text': 'Time depends upon the school that you choose to help'
                    },
                    {
                    'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                    'input_text': 'How many people work for you',
                    'output_text': 'There are many people who are voluntiarly working for us'
                    },
                    {
                    'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                    'input_text': 'What is your budget',
                    'output_text': 'The information cannot be revealed'
                    },
                    {
                    'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                    'input_text': 'When was the organisation formed',
                    'output_text': 'The organisation was formed on Jan 2014'
                    },
                    {
                    'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                    'input_text': 'Do you have technical assistance and support',
                    'output_text': 'Yes we have, technical support'
                    },
                    {
                    'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                    'input_text': 'How many action plans have you implemented till now',
                    'output_text': 'We have undertaken more than 100 action plans'
                    },
                    {
                    'import_path': 'chatterbot.logic.BestMatch'
                    },
                    {
                    'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                    'threshold': 0.5,
                    'default_response': 'I am sorry, but I do not understand.'
                    }],
       database='./database.sqlite3')

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

API_TOKEN = '302199532:AAE8dNIRfl-35RXpMd5YVa0Oaq_Jsg4ja-w'

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Okay Let's start chatting")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot_input = message.text+""
    bot_output = chatbot.get_response(bot_input)
    bot.reply_to(message, bot_output)

bot.polling()

