from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor

# Токен вашего бота
BOT_TOKEN = "6718974044:AAFixCnEzU6lZ9p7JQSkUR25QJ1sQ83bkSQ"

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Кнопки, которые вы хотите добавить
postbot = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Каналы📊", url="https://t.me/addlist/_NOQVWepeCVhZGU8"),
     InlineKeyboardButton(text="Чат 💬", url="https://t.me/CHAT_SSxHACK")],
    [InlineKeyboardButton(text="Поддержать автора", url="https://www.donationalerts.com/r/ssxzico"), 
     InlineKeyboardButton(text="Купить чит💰", url="https://t.me/gde_zico")],
    [InlineKeyboardButton(text="Ссылка на канал🔐", url="https://t.me/+U_cP468a88U3OTI0")]
])


# Хэндлер для текстовых сообщений в канале
@dp.channel_post_handler(content_types=types.ContentType.TEXT)
async def handle_text_posts(message: types.Message):
    await bot.edit_message_reply_markup(
        chat_id=message.chat.id,
        message_id=message.message_id,
        reply_markup=postbot
    )


# Хэндлер для фото
@dp.channel_post_handler(content_types=types.ContentType.PHOTO)
async def handle_photo_posts(message: types.Message):
    await bot.edit_message_reply_markup(
        chat_id=message.chat.id,
        message_id=message.message_id,
        reply_markup=postbot
    )


# Хэндлер для видео
@dp.channel_post_handler(content_types=types.ContentType.VIDEO)
async def handle_video_posts(message: types.Message):
    await bot.edit_message_reply_markup(
        chat_id=message.chat.id,
        message_id=message.message_id,
        reply_markup=postbot
    )


# Хэндлер для документов/файлов
@dp.channel_post_handler(content_types=types.ContentType.DOCUMENT)
async def handle_document_posts(message: types.Message):
    await bot.edit_message_reply_markup(
        chat_id=message.chat.id,
        message_id=message.message_id,
        reply_markup=postbot
    )


# Хэндлер для аудио
@dp.channel_post_handler(content_types=types.ContentType.AUDIO)
async def handle_audio_posts(message: types.Message):
    await bot.edit_message_reply_markup(
        chat_id=message.chat.id,
        message_id=message.message_id,
        reply_markup=postbot
    )


# Хэндлер для других типов (например, голосовые сообщения, анимации)
@dp.channel_post_handler(content_types=[
    types.ContentType.ANIMATION,
    types.ContentType.VOICE,
    types.ContentType.CONTACT,
    types.ContentType.LOCATION,
    types.ContentType.VENUE,
    types.ContentType.STICKER
])
async def handle_other_posts(message: types.Message):
    await bot.edit_message_reply_markup(
        chat_id=message.chat.id,
        message_id=message.message_id,
        reply_markup=postbot
    )

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Добавь меня в канал!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
