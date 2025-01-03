import openai
import openai
from aiogram import Bot, types

import logging
openai.api_key = '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'
token = telebot.TeleBot('7422695402:AAHYSWV1hdfN5ZNsHrdnxLu_D-cGIM2nxHs')


bot=Bot(token)
dp=Dispatcher
print(openai.Model.list())