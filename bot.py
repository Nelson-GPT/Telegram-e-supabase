from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from flask import Flask, request

# Flask app for webhook
app = Flask(__name__)

# Telegram bot token from environment variable
TOKEN="7751018653:AAHL2DZ_dRIPqBNQzroFoct_8Hz2KPz_0sk"
# Define the start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your bot.")

# Initialize the bot
bot_app = ApplicationBuilder().token(TOKEN).build()
bot_app.add_handler(CommandHandler("start", start))

# Webhook route
@app.route("/", methods=["POST"])
def webhook():
    if request.method == "POST":
        bot_app.update_queue.put(request.get_json(force=True))
        return "OK", 200

if __name__ == "__main__":
    app.run()