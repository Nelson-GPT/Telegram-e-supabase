# Nelson Bot

A Telegram bot integrated with Supabase for querying Nelson's Textbook of Pediatrics and calculating drug dosages.

## Features
- Topic search from Nelson's database
- Drug dosage calculator
- Interactive commands: `/help`, `/calculate`, `/search`

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repo-url>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the `.env` file with your credentials.
4. Run the bot:
   ```bash
   python bot.py
   ```

## Deployment
- Use Heroku or Render for deployment.
- Include the `Procfile` and set environment variables.

## Commands
- `/help` - Get help
- `/calculate` - Calculate drug dosages
- `/search` - Search Nelson's database
