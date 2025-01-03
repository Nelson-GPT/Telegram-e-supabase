import requests
from config import SUPABASE_URL, SUPABASE_API_KEY

def query_supabase(table_name, query_params):
    headers = {
        "apikey": SUPABASE_API_KEY,
        "Authorization": f"Bearer {SUPABASE_API_KEY}",
        "Content-Type": "application/json",
    }
    url = f"{SUPABASE_URL}/rest/v1/{table_name}?{query_params}"
    response = requests.get(url, headers=headers)
    return response.json()
