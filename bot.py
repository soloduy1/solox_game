import os
import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")
GAME_URL = os.getenv(
    "GAME_URL",
    "https://modeselector1.github.io/game_solmax_bot/gemini-code-1780062785165.html"
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎮 Играть", web_app=WebAppInfo(url=GAME_URL))]
    ])

    await update.message.reply_text(
        "Нажми кнопку, чтобы запустить игру:",
        reply_markup=keyboard
    )


async def web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    raw_data = update.message.web_app_data.data

    try:
        data = json.loads(raw_data)
    except json.JSONDecodeError:
        data = {"raw": raw_data}

    await update.message.reply_text(f"Результат игры: {data}")


def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN не задан")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data))

    app.run_polling()


if __name__ == "__main__":
    main()
