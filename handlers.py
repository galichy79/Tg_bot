from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text, Command

from keyboards import keyboard, keyboard1, phone_key, mak_key, cb

from main import bot, dp
from config import chat_id


async def send_hello(dp):
    await bot.send_message(chat_id=chat_id, text='Hello')


@dp.message_handler(Command('shop'))
async def show_shop(message: Message):
    await message.answer('Shop', reply_markup=keyboard)


@dp.message_handler(Text(equals=['btn1', 'btn2', 'btn3']))
async def get_goods(message: Message):
    await message.answer(message.text, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Command('tshop'))
async def show(message: Message):
    await message.answer(text='Buy or cancel', reply_markup=keyboard1)


@dp.callback_query_handler(text_contains='phone')
async def phone(call: CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer('Купить', reply_markup=phone_key)


@dp.callback_query_handler(cb.filter(name='mac'))
async def mac(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    p = callback_data.get('price')

    await call.message.answer(f'Купить. Он стоит: {p}', reply_markup=mak_key)


@dp.callback_query_handler(text_contains='cancel')
async def cancel(call: CallbackQuery):
    await call.answer('Отмена', show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)
