import os
import logging
from telegram.ext import Application, CommandHandler
from commands.calculate import calculate_dosage
from commands.search import search_topic
from commands.help import help_command
from config import TELEGRAM_BOT_TOKEN

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

async def main():
    """Start the bot using a webhook."""
    # Initialize the Application with the bot token
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Command Handlers
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("calculate", calculate_dosage))
    application.add_handler(CommandHandler("search", search_topic))

    # Webhook settings
    PORT = int(os.environ.get("PORT", 8443))  # Use Render's dynamic port
    RENDER_EXTERNAL_URL = os.environ.get("RENDER_EXTERNAL_URL")  # Your Render URL

    if not RENDER_EXTERNAL_URL:
        logger.error("RENDER_EXTERNAL_URL is not set. Exiting...")
        return

    await application.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TELEGRAM_BOT_TOKEN,
        webhook_url=f"{RENDER_EXTERNAL_URL}/{TELEGRAM_BOT_TOKEN}",
    )

    logger.info(f"Webhook started at {RENDER_EXTERNAL_URL}/{TELEGRAM_BOT_TOKEN}")

    # Idle to keep the bot running
    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
