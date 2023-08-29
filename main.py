import os Utils
import logging
from telegram.ext import Updater, Filters,  CommandHandler, MessageHandler,  CallbackContext, CallbackQueryHandler
from bot_helpers import start_command, generate_command, cancel_command
from otp_helpers import generate_otp, validate_otp_format, validate_otp
from telethon_helpers import generate_telethon_session


# Load environment variables from .env file
load_dotenv()

# Initialize logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

updater  = Updater("6319248602:AAG0QgESUUtlC5oBJ562icQNO2jy8uRNQy0" , use_context=True)
dispatcher = updater.dispatcher

# Command handlers
dispatcher.add_handler(CommandHandler("start", start_command))
dispatcher.add_handler(CommandHandler("generate", generate_command))
dispatcher.add_handler(CommandHandler("cancel", cancel_command))

# Message handler for OTP input
def receive_otp(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    user_input = update.message.text.strip()

    if validate_otp_format(user_input):
        client_data = get_client(chat_id)
        if client_data and not client_data['otp_validated']:
            stored_otp = client_data.get('otp')
            if stored_otp and validate_otp(stored_otp, user_input):
                update_otp_validation(chat_id)
                keyboard = [
                    [InlineKeyboardButton("Telethon", callback_data='telethon')],
                    [InlineKeyboardButton("Pyrogram", callback_data='pyrogram')]
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)
                update.message.reply_text("OTP has been validated! Now choose a framework.", reply_markup=reply_markup)
            else:
                update.message.reply_text("Invalid OTP. Please try again.")
        else:
            update.message.reply_text("You have already validated the OTP before.")
    else:
        update.message.reply_text("Invalid OTP format. Please enter a 6-digit number.")

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, receive_otp))
