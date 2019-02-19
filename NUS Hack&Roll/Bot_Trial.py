from telegram.ext import Updater, MessageHandler, Filters
import urllib
import wget
from Meme_Text_Writer import meme_writer
import Tag_Getter
import Emo_Getter
import Selector
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


#To Make List of Numbers into an int
def list_to_int(list):
    a=''
    for i in list:
        a+=str(i)
    a=int(a)
    return(a)

updater = Updater(token='645359765:AAEYSKURaaqjeEEoeAgUG7IqLbN4_xZ1lOM')
dispatcher = updater.dispatcher

#For Exception Handling
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello and Welcome to Brownie Memes!")

#Start Bot
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

#Meme is made and sent
def echo(bot, update):
    file = bot.getFile(update.message.photo[-1].file_id)
    print(file)
    file_url = (file.file_path)
    print(file_url)
    file_name = wget.download(file_url)
    print(file_name)
    tags = Tag_Getter.detect_labels(file_name)
    emo = Emo_Getter.detect_faces(file_name)
    meme_message=Selector.simple_function(list_to_int(emo),tags)
    meme_writer(meme_message,0,file_name)

    bot.send_photo(chat_id=update.message.chat_id, photo=open("Completed/temp.png", 'rb'))
    print(tags,'\n',emo)

echo_handler = MessageHandler(Filters.photo, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
