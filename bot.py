from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    CallbackQueryHandler, ContextTypes, filters
)

from handlers.start import start_handler
from handlers.callbacks import callback_router
from handlers.play import play_handler
from handlers.inline_message import generic_message
from handlers.profile import get_fancy_for_user

from system.database import init_db
from system.logger import get_logger

from pyrogram import Client
from pytgcalls import PyTgCalls

from config import TELEGRAM_BOT_TOKEN, SESSION


logger = get_logger(__name__)


# ------------------------------
# 🔥 Pyrogram Client + PyTgCalls
# ------------------------------
pyro_client = Client(
    "melody_session",
    api_id=123456,            # <-- User must fill API ID
    api_hash="your_api_hash", # <-- User must fill API HASH
    session_string=SESSION
)

pytgcalls_client = PyTgCalls(pyro_client)


def main():
    if not TELEGRAM_BOT_TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN not set")

    # Database Init
    init_db()

    # ------------------------------
    # PTB Application
    # ------------------------------
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("play", play_handler))

    # Callbacks
    app.add_handler(CallbackQueryHandler(callback_router))

    # Normal/Text Messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generic_message))

    logger.info("🔥 Melody Bot Starting…")

    # ------------------------------
    # Run both PTB + Pyrogram + VC
    # ------------------------------
    pyro_client.start()
    pytgcalls_client.start()

    app.run_polling()


if __name__ == "__main__":
    main()
