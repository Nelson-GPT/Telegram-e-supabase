from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from commands.calculate import calculate_dosage
from commands.search import search_topic
from commands.help import help_command
from config import TELEGRAM_BOT_TOKEN

import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def error_handler(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning(f"Update {update} caused error {context.error}")

def main():
    """Main function to start the bot."""
    try:
        updater = Updater(TELEGRAM_BOT_TOKEN)

        # Command Handlers
        updater.dispatcher.add_handler(CommandHandler("help", help_command))
        updater.dispatcher.add_handler(CommandHandler("calculate", calculate_dosage))
        updater.dispatcher.add_handler(CommandHandler("search", search_topic))

        # Add error handler
        updater.dispatcher.add_error_handler(error_handler)

        # Start the bot
        logger.info("Starting the bot...")
        updater.start_polling()
        updater.idle()

    except Exception as e:
        logger.error(f"Bot encountered an issue: {e}")
        if "Conflict" in str(e):
            logger.error(
                "Conflict detected: Make sure no other instances of the bot are running."
            )

if __name__ == "__main__":
    main()