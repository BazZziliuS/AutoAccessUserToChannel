from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ChatJoinRequest
bot = Bot("TOKEN")
dp = Dispatcher(bot)
print('AutoAccessChannel On')

@dp.chat_join_request_handler()
async def join(update: types.ChatJoinRequest):
    await update.approve()
    print('У нас новый подписчик!')

if __name__ == '__main__':
    executor.start_polling(dp)