import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import F

TOKEN = "ТВОЙ_ТОКЕН_БОТА"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_numbers_keyboard():
    """Создает клавиатуру с кнопкой"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🎲 Сгенерировать новые числа", callback_data="generate_numbers")]
        ]
    )
    return keyboard

def generate_numbers_text():
    """Генерирует текст с тремя случайными числами"""
    numbers = [random.randint(1, 78) for _ in range(3)]
    return f"🎲 Ваши случайные числа:\n\n" \
           f"🔹 Первое: {numbers[0]}\n" \
           f"🔹 Второе: {numbers[1]}\n" \
           f"🔹 Третье: {numbers[2]}"

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я помогу тебе получить 3 случайных числа от 1 до 78 🎲\n"
        "Нажми на кнопку ниже, чтобы начать! 👇",
        reply_markup=get_numbers_keyboard()
    )

@dp.callback_query(F.data == "generate_numbers")
async def process_numbers(callback: types.CallbackQuery):
    # Редактируем существующее сообщение
    await callback.message.edit_text(
        generate_numbers_text(),
        reply_markup=get_numbers_keyboard()
    )
    await callback.answer()  # Убираем "часики" на кнопке

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if name == "__main__":
    asyncio.run(main())