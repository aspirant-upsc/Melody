
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config import OWNER_NAME
from handlers.profile import get_fancy_for_user


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    text = (
        f"✨ Welcome to MelodyX!\n\n"
        f"👑 Owner: {OWNER_NAME}\n"
        f"Use the buttons below to explore the bot."
    )

    # Buttons
    kb = [
        [
            InlineKeyboardButton('▶️ Play', callback_data='play_menu'),
            InlineKeyboardButton('📚 Learn', callback_data='learn_menu')
        ],
        [
            InlineKeyboardButton('❓ Help', callback_data='help_menu'),
            InlineKeyboardButton('👤 Owner', callback_data='owner_info')
        ],
        [
            InlineKeyboardButton('✨ Fancy Name', callback_data='fancy_menu'),
            InlineKeyboardButton('💖 Add me baby', callback_data='add_me_baby')
        ],
    ]

    # Fancy name fetch
    fancy = get_fancy_for_user(user.id)
    if fancy:
        text += f"\n\n🌟 Your fancy name: {fancy}"

    # Send message
    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(kb)
    )