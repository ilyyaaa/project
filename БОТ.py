from mistralai import Mistral
import telebot
import os
import logging
from telebot.types import Message

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Извлечение токенов и API-ключей из переменных окружения
api_key = os.environ.get('MISTRAL_API_KEY')  # Убедитесь, что ключ MISTRAL_API_KEY установлен
telegram_token = os.environ.get('TELEGRAM_BOT_TOKEN')  # Убедитесь, что ключ TELEGRAM_BOT_TOKEN установлен

client = Mistral(api_key=api_key)

bot = telebot.TeleBot(telegram_token)

@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.send_message(
        message.chat.id,
        f'Привет, {message.from_user.first_name}!\nЧем могу помочь?'
    )

# Обработчик команды /about
@bot.message_handler(commands=['about'])
def about(message: Message):
    about_text = (
        'Привет! Я могу помогать вам в решении задач и искать нужную информацию. '
        'Буду рад помочь!'
    )
    bot.send_message(message.chat.id, about_text)

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda msg: True)
def message_handler(msg: Message):
    try:
        # Запрос к Mistral
        response = client.chat.complete(
            model="pixtral-12b-2409",
            messages=[
                {"role": "user", "content": msg.text},
            ]
        )
  
        chat_response = response.choices[0].message.content
        bot.send_message(msg.chat.id, chat_response, parse_mode='Markdown')
    except AttributeError as e:
        
        bot.send_message(msg.chat.id, "Извините, произошла ошибка при обработке ответа.")
   


@bot.message_handler(content_types=['photo'])
def get_photo(message: Message):
    bot.send_message(
        message.chat.id,
        'Классная фотка! Но меня еще не научили их распознавать... Может подсказать?'
    )


bot.polling(non_stop=True)
