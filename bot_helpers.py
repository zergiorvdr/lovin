from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext

def start_command(update: Update, context: CallbackContext):
    username = update.message.from_user.username
    update.message.reply_text(
        f"Hi @{username}! I can help you generate a string session.\n"
        "Before we start, you need to validate an OTP sent to you."
    )

def generate_command(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Join Group", url="https://t.me/your_group_here")],
        [InlineKeyboardButton("Join Channel", url="https://t.me/your_channel_here")],
        [InlineKeyboardButton("Retry", callback_data='retry')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Before generating the string session, please join our group and channel:",
        reply_markup=reply_markup
    )

def cancel_command(update: Update, context: CallbackContext):
    update.message.reply_text("Action canceled.")
