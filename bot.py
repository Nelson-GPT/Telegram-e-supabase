import os
from telegram.ext import Application, CommandHandler

from commands.help import help_command
from commands.search import search_topic
from commands.calculate import calculate_dosage

# Load environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "")  # Add this to your .env file

async def main():
    """Start the bot using a webhook."""
    # Initialize the application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("calculate", calculate_dosage))
    application.add_handler(CommandHandler("search", search_topic))

    # Start webhook
    await application.run_webhook(
        listen="0.0.0.0",               # Listen on all network interfaces
        port=8443,                     # Port number
        url_path=TELEGRAM_BOT_TOKEN,   # Token in the URL path
        webhook_url=f"{WEBHOOK_URL}/{TELEGRAM_BOT_TOKEN}"  # External webhook URL
    )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
