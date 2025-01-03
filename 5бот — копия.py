import asyncio
import openai
from aiogram import Bot,types
from aiogram.dispatcher import dispatcher
from aiogram.utils import executor

token=('7422695402:AAHYSWV1hdfN5ZNsHrdnxLu_D-cGIM2nxHs')
openai.api_key = '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'
bot=Bot(token)
dp=Dispatcher(bot)
@dp.message_handler()
async def send(message:types.Message):
    responce=openai.Completions.create(
    model='code-davinci-002',
    promt=message.text,
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.6,
    stop=['You:']
    )
    await message.answer(responce['choices'][0]['text'])
    
    executor.start_polling(dp,skip_updates=True)