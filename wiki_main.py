import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1931222660:AAGqBQVSOnOQudVYa21rDBT39R3yXxCko3k'
wikipedia.set_lang('uz')
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu alaykum jiyanlar!\nMana ko'chir-ko'chir bilan qilingan wikibot !\nPowered by KrAcaV4iK.")



@dp.message_handler()
async def wikicha(message: types.Message):
    try:
        javob = wikipedia.summary(message.text)
        await message.answer(javob)
    except:
        await  message.answer('Kechirasiz chota adashdiz')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
