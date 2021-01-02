from credentials import token
from telegram.ext import Updater, CommandHandler
from textos import saludo, metadatos

def Hola(update, context):
    name = update.effective_user.first_name
    ChatID = update.message.chat_id
    context.bot.sendMessage(chat_id=ChatID,text=saludo.format(name))

def MetaData(update, context):
    #name,channel,date,day,month,year,stage,state = GetDatos()
    name = input("Ingresa nombre: ")
    channel = input("Ingresa canal: ")
    date = input("Ingresa fecha dd/mm/aa: ")
    day = input("Ingresa el día: ")
    month = input("Ingresa el mes: ")
    year = input("Ingresa el año: ")
    stage = input("Ingresa la etapa: (tailandia - japon) ")
    state = input("Ingresa el estado: (copia - original) ")
    ChatID = update.message.chat_id
    context.bot.sendMessage(chat_id=ChatID,text=metadatos.format(name,
                                                                 channel,
                                                                 date,
                                                                 day,
                                                                 month,
                                                                 year,
                                                                 stage,
                                                                 state))

def main():

    updater = Updater(token=token)

    # manejador de la funcion Hola
    updater.dispatcher.add_handler(CommandHandler("hola",Hola))

    # manejador de la funcion MetaData
    updater.dispatcher.add_handler(CommandHandler("metadata",MetaData))

    
    print("MindaBot yeah!!")

    # iniciamos bot
    updater.start_polling()

if __name__ == "__main__":
    main()