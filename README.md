# NelsonBot Telegram Integration

This is a simple Telegram bot integrated with a Flask app, deployed using Vercel. It handles webhook requests from Telegram and processes updates using the `python-telegram-bot` library.

## Requirements

- Python 3.8.10 (or compatible version)
- Flask
- python-telegram-bot library

## Setup

1. Clone the repository.
2. Install dependencies from `requirements.txt`.
3. Set up a Telegram bot via BotFather and obtain your bot token.
4. Set the webhook URL for your bot.

## Deploying to Vercel

1. Push the code to your Git repository.
2. Deploy the app using Vercel.

The app will listen for updates at `/api/webhook`.

## Running Locally

Run the Flask app locally:

```bash
python bot.py