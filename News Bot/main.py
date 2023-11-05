from telegram import Update
from telegram.ext import *
from telegram import *
from telegram.ext import *
from aiogram import types
import NewsService

TOKEN = "5743423359:AAGbfTcbyvWsIBuOTt6iE-13WtGbqUbtK4Q"
BOT_USENAME= "@news123apibot"
bot = Bot(token=TOKEN)

categoriesList = ["главное", "технологии", "спорт", "бизнес", "наука"]

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Здравствуйте!')
    keyboard = []
    for item in categoriesList:
        keyboard.append([InlineKeyboardButton(item, callback_data=item)])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Выберите категорию новостей:', reply_markup=reply_markup)

# Responses
async def button_handler(update, context):
    query = update.callback_query
    print(query.data)
    await query.answer()
    await query.edit_message_text(text=f'Вы выбрали категорию новостей: {query.data}')
    await handle_categories(update, query.data)

async def handle_categories(message, query: str):

    category = NewsService.currentCategory(category=query)
    news = NewsService.fetchNews(category=category)

    print(news)

    for news_item in news:
        image = "https://cdn.vectorstock.com/i/preview-1x/82/99/no-image-available-like-missing-picture-vector-43938299.jpg"
        title = news_item["title"]
        caption = f"{title}"
        await bot.send_photo(chat_id=message.effective_chat.id, photo=image, caption=caption)

if __name__ == '__main__':
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CallbackQueryHandler(button_handler))

    # Polls the bot
    print("Polling...")
    app.run_polling(poll_interval=5)
