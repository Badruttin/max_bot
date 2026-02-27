import asyncio
import logging

from maxapi import Bot, Dispatcher, F
from maxapi.types import BotStarted, Command, MessageCreated
from os import getenv
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()
TOKEN = getenv('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher()

#@dp.message_created(F.message.body.text)
#async def echo(event: MessageCreated):
#    await event.message.answer(f"sdljfdsljf {event.message.body.text}")

# Ответ бота на команду /start
@dp.message_created(Command('start'))
async def hello(event: MessageCreated):
    await event.message.answer(f"Пример чат-бота для MAX 💙")

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())