import os
import logging
from datetime import datetime, timedelta
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters
import openai

# Завантаження змінних оточення
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_KEY

# Логи
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# /start команда
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("AI Відповідь", callback_data="ai_response")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привіт! Я твій Telegram бот 🤖
Використовуй кнопки або команди.", reply_markup=reply_markup)

# /help команда
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/start - Запустити бота
/help - Допомога
/time - Показати час
/remind <хвилини> <текст> - Нагадування")

# /time команда
async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now().strftime("%H:%M:%S")
    await update.message.reply_text(f"Зараз {now} ⏰")

# /remind команда
async def remind_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        minutes = int(context.args[0])
        text = " ".join(context.args[1:])
        remind_time = datetime.now() + timedelta(minutes=minutes)
        context.job_queue.run_once(lambda ctx: ctx.bot.send_message(chat_id=update.effective_chat.id, text=f"Нагадування: {text}"), when=minutes*60)
        await update.message.reply_text(f"Нагадування через {minutes} хвилин ✅")
    except:
        await update.message.reply_text("Формат: /remind <хвилини> <текст>")

# Обробка кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "ai_response":
        await query.message.reply_text("Напиши своє питання, і я відповім ✨")

# AI відповідь
async def ai_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if OPENAI_KEY is None:
        await update.message.reply_text("⚠️ OpenAI API ключ не налаштований.")
        return
    user_text = update.message.text
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": user_text}])
    await update.message.reply_text(response["choices"][0]["message"]["content"])

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("time", time_command))
    app.add_handler(CommandHandler("remind", remind_command))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ai_handler))

    app.run_polling()

if __name__ == "__main__":
    main()
