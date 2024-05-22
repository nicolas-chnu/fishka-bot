import os
from dotenv import load_dotenv
from telegram import Update,InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler, CallbackContext

load_dotenv()
bot_token = os.getenv('BOT_TOKEN')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = ('Привіт, мене звати Fishka!\n\n'
            'Хочеш першим дізнаватися про найцікавіша пропозиції?\n'
            'Тоді переходь за посиланням 👇 і нумо накопичувати бали!')

    keyboard = [
        [InlineKeyboardButton("Клацни на мене", url="https://nicolas-chnu.github.io/google-auth/")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_sticker('fish-sticker.tgs')
    await update.message.reply_text(text, reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    await query.answer()
    await query.delete_message()


if __name__ == '__main__':
    application = ApplicationBuilder().token(bot_token).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()
