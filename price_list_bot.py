from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import Message

price_list = [198, 318, 428, 658, 49]
bot = Bot("6243201914:AAErA4WVDMPovzkdNV080pDiLG6Lgeq65sw")
dsp = Dispatcher(bot)


async def on_start(_):
    print("Бот запущен")


@dsp.message_handler(commands=["start"])
async def com_start(message: Message):
    await message.reply(f"Привет, {message.from_user.first_name}! "
                        f"Рад, что ты являешься нашим абонентом. "
                        f"Чтобы узнать стоимость тарифа, введи команду /price")


@dsp.message_handler(commands=["price"])
async def com_price(message: Message):
    await message.reply("""Выбери предпочтительный тариф:
    200 мин и 2 ГБ: /first
    400 мин и 4 ГБ: /second
    600 мин и 8 ГБ: /third
    1200 мин и 16 ГБ: /fourth""")


@dsp.message_handler(commands=["first"])
async def com_first(message: Message):
    price = price_list[0]
    await message.reply(f"""Стоимость выбранного тарифа: {price} руб.
    Хочешь подключить безлимитные СМС за {price_list[4]} руб?
    'Да': /yes 
    'Нет': /no""")
    price_list.append(price)


@dsp.message_handler(commands=["second"])
async def com_second(message: Message):
    price = price_list[1]
    await message.reply(f"""Стоимость выбранного тарифа: {price} руб.
    Хочешь подключить безлимитные СМС за {price_list[4]} руб?
    'Да': /yes 
    'Нет': /no""")
    price_list.append(price)


@dsp.message_handler(commands=["third"])
async def com_third(message: Message):
    price = price_list[2]
    await message.reply(f"""Стоимость выбранного тарифа: {price} руб.
    Хочешь подключить безлимитные СМС за {price_list[4]} руб?
    'Да': /yes 
    'Нет': /no""")
    price_list.append(price)


@dsp.message_handler(commands=["fourth"])
async def com_fourth(message: Message):
    price = price_list[3]
    await message.reply(f"""Стоимость выбранного тарифа: {price} руб. 
    Хочешь подключить безлимитные СМС за {price_list[4]} руб?
    'Да': /yes 
    'Нет': /no""")
    price_list.append(price)


@dsp.message_handler(commands=["yes"])
async def com_yes(message: Message):
    await message.reply(f"Стоимость выбранного тарифа c безлимитными СМС: {price_list[5] + price_list[4]} руб. "
                        f"\nДо встречи! По всем вопросам: @egiazarov_vazgen")
    price_list.pop(5)


@dsp.message_handler(commands=["no"])
async def com_no(message: Message):
    await message.reply("До встречи! По всем вопросам: @egiazarov_vazgen")
    price_list.pop(5)


executor.start_polling(dsp, skip_updates=True, on_startup=on_start)
