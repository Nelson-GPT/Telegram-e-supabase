from telegram import Update
from telegram.ext import CallbackContext
from supabase.supabase_queries import query_supabase

def calculate_dosage(update: Update, context: CallbackContext):
    if len(context.args) < 2:
        update.message.reply_text("Usage: /calculate <drug_name> <weight_in_kg>")
        return

    drug_name = context.args[0].lower()
    try:
        weight = float(context.args[1])
    except ValueError:
        update.message.reply_text("Please provide a valid weight in kilograms.")
        return

    drug_info = query_supabase("drugs", f"drug_name=eq.{drug_name}")
    if not drug_info:
        update.message.reply_text("Drug not found in database.")
        return

    drug = drug_info[0]
    dosage_range = drug["dosage"].split("-")
    min_dose = round(float(dosage_range[0]) * weight)
    max_dose = round(float(dosage_range[1]) * weight)

    update.message.reply_text(
        f"**Drug:** {drug_name.capitalize()}
"
        f"**Dosage:** {min_dose}-{max_dose} mg/dose
"
        f"**Frequency:** {drug['frequency']}
"
        f"**Route:** {drug['route']}"
    )
