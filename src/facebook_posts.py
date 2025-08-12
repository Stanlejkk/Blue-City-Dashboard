import os
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()


def fetch_facebook_posts(page_id: str) -> pd.DataFrame:
    token = os.getenv("FACEBOOK_ACCESS_TOKEN")
    if not token:
        return pd.DataFrame()

    url = f"https://graph.facebook.com/v17.0/{page_id}/posts"
    params = {
        "access_token": token,
        "fields": "message,created_time",
        "limit": 100,
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json().get("data", [])
    except Exception:
        return pd.DataFrame()

    rows = [
        {"text": item.get("message"), "time": item.get("created_time")}
        for item in data
        if item.get("message")
    ]
    return pd.DataFrame(rows)
