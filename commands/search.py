from telegram import Update
from telegram.ext import CallbackContext
from supabase.supabase_queries import query_supabase

def search_topic(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        update.message.reply_text("Usage: /search <topic>")
        return

    topic = " ".join(context.args).lower()
    results = query_supabase("nelson_knowledge", f"search_term=ilike.%{topic}%")

    if results:
        update.message.reply_text(results[0].get("content", "No content found."))
    else:
        update.message.reply_text("No results found.")
