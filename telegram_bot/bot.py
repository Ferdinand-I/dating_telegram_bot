import asyncio
import os

from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv()

# https://docs.aiogram.dev/en/dev-3.x/dispatcher/router.html
router = Router()

# тестовые пресеты с кнопками
BUTTONS = {
    'welcome': InlineKeyboardButton(text='Привет!', url='https://ya.ru')
}


@router.message()
async def echo_message(message: Message) -> None:
    """Простой пример использования бота. Echo message."""
    await message.answer(message.text)


@router.startup()  # Хендлер, который отрабатывает при запуске
async def welcome(bot: Bot) -> None:
    """Велкам функция."""
    # собираем клавиатуру
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [BUTTONS.get('welcome')]
        ]
    )
    await bot.send_message(chat_id=147332835, text='wqe', reply_markup=markup)


async def main() -> None:
    """Основная логика."""
    # https://docs.aiogram.dev/en/dev-3.x/dispatcher/dispatcher.html
    dispatcher = Dispatcher()
    dispatcher.include_router(router)
    __token = os.getenv('TOKEN')

    # https://docs.aiogram.dev/en/dev-3.x/api/bot.html
    bot = Bot(token=__token)
    await dispatcher.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
