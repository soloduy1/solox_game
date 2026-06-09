import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

GAME_URL = os.getenv(
    "GAME_URL",
    "https://soloduy1.github.io/solex-site/",
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                text="🎮 Играть",
                web_app=WebAppInfo(url=GAME_URL),
            )
        ]
    ])

    await update.message.reply_text(
        "Нажми кнопку ниже, чтобы открыть игру:",
        reply_markup=keyboard,
    )


def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN не задан")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()


if __name__ == "__main__":
    main()
