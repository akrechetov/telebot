
from flask import Flask, request
import telebot
import os


app = Flask(__name__)
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['courses'])
def message_start(message):
    keybord = telebot.types.InLineKeyboardMarkup(row_width=1)

    with open('courses.txt') as file:
        courses = [item.split(',') for item in file]

        for title, link in courses:
            url_button = telebot.types.InLineKeyboardButton(text=title.strip(), url=link.strip())
            keyboard.add(url_button)

        bot.send_message(message.chat.id, 'List of courses', reply_markup=keybord)

@bot.message_handler(func=lambda x: x.text.lower().startswith('python'))
def message_text(message):
    bot.send_message(message.chat.id, 'python!')

@bot.message_handler(commands=['start'])
def message_start(message):
    bot.send_message(message.chat.id, 'Hello user!')

@app.route('/' + TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Python Telegram Bot 30-01-2022", 200


@app.route('/')
def main():
    bot.remove_webhook()
    bot.set_webhook(url='https://lessontelegrambot.herokuapp.com/' + TOKEN)
    return 'Python Telegram Bot', 200

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = int(os.environ.get('PORT', 5000)))

