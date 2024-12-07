import os
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from threading import Thread

# Flask app for webhook
app = Flask(__name__)

# Telegram bot token from environment variable
TOKEN = "7751018653:AAHL2DZ_dRIPqBNQzroFoct_8Hz2KPz_0sk"

# Initialize the bot application
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your bot.")

bot_app = ApplicationBuilder().token(TOKEN).build()
bot_app.add_handler(CommandHandler("start", start))

# Webhook route
@app.route("/api/webhook", methods=["POST"])
def webhook():
    if request.method == "POST":
        # Process the incoming update (this is where we pass the data to the bot)
        update = Update.de_json(request.get_json(), bot_app.bot)
        bot_app.dispatcher.process_update(update)
        return "OK", 200

# Function to run the Flask app in a separate thread
def run_flask():
    app.run(debug=True, use_reloader=False)

# Function to run the bot in the main thread
def run_bot():
    bot_app.run_polling()

if __name__ == "__main__":
    # Run Flask in a separate thread
    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    # Run bot
    run_bot()