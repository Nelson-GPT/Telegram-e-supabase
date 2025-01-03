from telegram import Update
from telegram.ext import Updater, CommandHandler
from commands.calculate import calculate_dosage
from commands.search import search_topic
from commands.help import help_command
from config import TELEGRAM_BOT_TOKEN

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN)

    # Command Handlers
    updater.dispatcher.add_handler(CommandHandler("help", help_command))
    updater.dispatcher.add_handler(CommandHandler("calculate", calculate_dosage))
    updater.dispatcher.add_handler(CommandHandler("search", search_topic))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
