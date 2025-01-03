from telegram import Update
from telegram.ext import CallbackContext
from supabase.supabase_queries import query_supabase

def calculate_dosage(update: Update, context: CallbackContext):
    """
    Calculate dosage based on drug name and patient's weight in kilograms.
    Usage: /calculate <drug_name> <weight_in_kg>
    """
    # Check if sufficient arguments are provided
    if len(context.args) < 2:
        update.message.reply_text("Usage: /calculate <drug_name> <weight_in_kg>")
        return

    # Extract the drug name and weight
    drug_name = context.args[0].lower()
    try:
        weight = float(context.args[1])
    except ValueError:
        update.message.reply_text("Please provide a valid weight in kilograms.")
        return

    # Query the drug information from the Supabase database
    drug_info = query_supabase("drugs", f"drug_name=eq.{drug_name}")
    if not drug_info:
        update.message.reply_text("Drug not found in database.")
        return

    # Extract drug details
    drug = drug_info[0]
    try:
        dosage_range = drug["dosage"].split("-")
        min_dose = round(float(dosage_range[0]) * weight)
        max_dose = round(float(dosage_range[1]) * weight)

        # Format and send the response
        update.message.reply_text(
            f"**Drug:** {drug_name.capitalize()}\n"
            f"**Dosage:** {min_dose}-{max_dose} mg/dose\n"
            f"**Frequency:** {drug['frequency']}\n"
            f"**Route:** {drug['route']}"
        )
    except (KeyError, ValueError, IndexError):
        update.message.reply_text("Error processing drug dosage information.")