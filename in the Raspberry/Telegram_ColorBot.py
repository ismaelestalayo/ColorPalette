import telebot
from telebot import types
import time

from PIL import Image, ImageFont, ImageDraw
import random


knownUsers = []  # todo: save these in a file,
userStep = {}  # so they won't reset every time the bot restarts

commands = {  
              'start': 'First things first',

              'help': 'Shows info about the available commands',

              'palette': 'Generates a pseudo-random palette of colors.',

              'gradient': 'Generates a pseudo-random gradient of two colors.'
}




def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]

    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print "New user detected, who hasn't used \"/start\" yet"
        return 0

#Outputs the incoming messages in the console
def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print str("   >" + m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text



############################################################################
def main():
    bot = telebot.TeleBot("346619541:AAEJXdhfgt-LedjpDr_GOYvO4de9RSkGHmw")
    bot.set_update_listener(listener)  # register listener

 
    @bot.message_handler(commands=['start'])
    def command_start(m):
        cid = m.chat.id

        if cid not in knownUsers: 
            knownUsers.append(cid)  
            bot.send_message(cid, "Hello, stranger, let me scan you...")
            bot.send_message(cid, "Scanning complete, I know you now!")
            command_help(m)  # show the new user the help page

        else:
            bot.send_message(cid, "I already know you ^^")





    @bot.message_handler(commands=['help'])
    def command_help(m):
        cid = m.chat.id
        help_text = "This are the available commands: \n"
        for key in commands:
            help_text += "/" + key + ": "
            help_text += commands[key] + "\n"

        bot.send_message(cid, help_text)



    @bot.message_handler(func=lambda message: message.text == "Ping")
    def command_text_hi(m):
        bot.send_message(m.chat.id, "Pong")



    @bot.message_handler(commands=['palette'])
    def command_palette(m):
        cid = m.chat.id
	bot.send_message(m.chat.id, "Creating random palette...")

	execfile("randomPalette.py")	

        bot.send_photo(cid, open('randomPalette.jpg', 'rb')) 


    @bot.message_handler(commands=['gradient'])
    def command_gradient(m):
	cid = m.chat.id
	bot.send_message(m.chat.id, "Creating random gradient...")

	execfile("randomGradient.py")

	bot.send_photo(cid, open('randomGradient.jpg', 'rb'))


    bot.polling()

############################################################################
try:
    main()

except KeyboardInterrupt:
    print("Exiting by Ctrl-C request...")
    sys.exit(0)

    
