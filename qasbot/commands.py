from telegram import ReplyKeyboardMarkup, ParseMode
from telegram.ext import  ConversationHandler
from .templating import LoadTemplate

from .qasengine import Engine

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

plihan_keyboard =  [['Tanya']]

tanya_keyboard = [ ['Batal'] ]

engine = Engine()

markup = ReplyKeyboardMarkup(plihan_keyboard, one_time_keyboard=True, resize_keyboard=True)
tanya_markup = ReplyKeyboardMarkup(tanya_keyboard, one_time_keyboard=True, resize_keyboard=True)

def TampilTemplate(update, nama ): 
    if nama.lower() == "alamat":
        update.message.reply
    teks, mode = LoadTemplate(nama)
    update.message.reply_text(teks.format(username = update.message.from_user.first_name.replace('-', ' ')),
     parse_mode=mode, reply_markup=markup) 
    
def mulai(update, context):
    TampilTemplate(update,'#pembuka' )  
    return CHOOSING


def tanya_jawab(update, context):
    text = update.message.text
    text = text.lower()
    if text in ['gajadi', 'batal', 'malu', 'nanti aja']:
        update.message.reply_text('Yaudah gapapa...', reply_markup=markup) 
        return CHOOSING
    
    update.message.reply_text('Mohon Tunggu Sebentar yaa...') 
    state, text = engine.Parse(text)
    if state:
        TampilTemplate(update, text)
    else:
        update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=tanya_markup)
    return TYPING_CHOICE

def info_umum(update, context): 
    update.message.reply_text('Okey silahkan tanyakan apapun...', reply_markup=tanya_markup)
    return TYPING_CHOICE

def selesai(update, context):
    user_data = context.user_data
    
    if 'choice' in user_data:
        del user_data['choice']

    update.message.reply_text("Terimakasih telah menggunakan Candi Prambanan Bot") 
    user_data.clear()
    
    return ConversationHandler.END
