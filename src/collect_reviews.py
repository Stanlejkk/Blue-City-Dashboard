from serpapi import GoogleSearch
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


def collect_reviews(data_id: str) -> pd.DataFrame:
    api_key = os.getenv("SERPAPI_KEY")
    if not api_key:
        return pd.DataFrame()

    params = {
        "engine": "google_maps_reviews",
        "api_key": api_key,
        "hl": "pl",
        "data_id": data_id,
        "sort_by": "qualityScore",
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    reviews = results.get("reviews", [])
    rows = [
        {
            "text": r.get("snippet"),
            "rating": r.get("rating"),
            "time": r.get("relative_time_description"),
        }
        for r in reviews
    ]
    return pd.DataFrame(rows)
