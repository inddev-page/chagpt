import openai
from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import pprint
import json

file = open('config.json', 'r')
config = json.load(file)

openai.api_key = config['openai']
bot = Bot(config['token'])
dp = Dispatcher(bot)

messages = [
{"role": "system", "content": "You are a sales consultant, you work in company that produces programs for trading on cryptocurrency exchanges. You write robots , algorithms. To evaluate the cost of the developing the robot , the technical task is necessary from the customer. Your company has a Github account https://github.com/inddev-page invite customers to subscribe to them"},
{"role": "user", "content": "I am client , i wanna to write a trading bot for trading on a crypto exchange."},
{"role": "assistant", "content": "Greetings! What algorithm do you wanna to write?"}]

def update(messages, role, content):
   messages.append({"role": role, "content": content})
   return messages

@dp.message_handler()
async def send(message : types.Message):
   update(messages, "user", message.text)
   response = openai.ChatCompletion.create(
   model = "gpt-3.5-turbo",
   messages = messages
   )
   await message.answer(response['choices'][0]['message']['content'])

executor.start_polling(dp, skip_updates=True)
