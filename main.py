
import telebot

bot = telebot.TeleBot("5878101695:AAEW5OX8ZHqazaOy6xi0y-52X1kbDbFShsg")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling()
