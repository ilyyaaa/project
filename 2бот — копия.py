import telebot
import openai

# Установите свой ключ API OpenAI
openai.api_key = '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'

# Инициализация бота
bot = telebot.TeleBot('7422695402:AAHYSWV1hdfN5ZNsHrdnxLu_D-cGIM2nxHs')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} \nЧем смогу помочь?')

@bot.message_handler(commands=['about'])
def about(message):
    about_text = 'Привет! Я могу помогать вам в решении задач и искать нужную информацию! Буду рад помочь!'
    bot.send_message(message.chat.id, about_text)

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.send_message(message.chat.id, 'Классная фотка! Но меня еще не научили их распознавать... Может подсказать?')

@bot.message_handler(func=lambda message: True)
def respond_with_gpt(message):
    try:
        # Используем новый интерфейс OpenAI API с ChatCompletion
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Выбор модели, аналогичной text-davinci-003
            messages=[  # Формируем историю сообщений
                {"role": "system", "content": "Ты помощник."},  # Сообщение для задания контекста
                {"role": "user", "content": message.text}  # Сообщение от пользователя
            ],
            temperature=0.5,  # Настройка для вариативности ответов
            max_tokens=1000,  # Ограничиваем количество токенов
            top_p=1.0,  # Настройка для выборки по вероятности
            frequency_penalty=0.5,  # Штраф за частоту
            presence_penalty=0.0  # Штраф за присутствие
        )

        # Отправляем ответ от GPT пользователю
        bot.send_message(message.chat.id, response['choices'][0]['message']['content'])

    except Exception as e:
        bot.send_message(message.chat.id, "Произошла ошибка при обработке вашего запроса.")
        print(e)

bot.polling(non_stop=True)

