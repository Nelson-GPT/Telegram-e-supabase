from telegram import Update
from telegram.ext import CallbackContext

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        "/help - Display this help message\n"
        "/calculate <drug_name> <weight> - Calculate drug dosage\n"
        "/search <topic> - Search for a topic in Nelson's knowledge\n"
    )
