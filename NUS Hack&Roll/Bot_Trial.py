from telegram.ext import Updater
import urllib
import wget
from memeTextWriter import meme_writer
import Tag_Getter
import Emo_Getter
import meme_gen

def sss(List):
    a=''
    for i in List:
        a+=str(i)
    a=int(a)
    return(a)

updater = Updater(token='732081876:AAGvjOxwN-pFQ2z97_KHtro6O3-wzylMo-c')

dispatcher = updater.dispatcher
#For Exception Handling
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello and Welcome to Brownie Memes!")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def echo(bot, update):
    file = bot.getFile(update.message.photo[-1].file_id)

    file_url = (file.file_path)

    file_name = wget.download(file_url)
    tags = Tag_Getter.detect_labels(file_name)
    emo = Emo_Getter.detect_faces(file_name)
    meme_message=meme_gen.simpleFunction(sss(emo),tags)
    meme_writer(meme_message,0,file_name)

    bot.send_photo(chat_id=update.message.chat_id, photo=open("Completed/temp.png", 'rb'))
    print(tags,'\n',emo)

from telegram.ext import MessageHandler, Filters

echo_handler = MessageHandler(Filters.photo, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
