from serpapi import GoogleSearch
import os
import json
from dotenv import load_dotenv
load_dotenv()

# Collect reviews from Google Maps using SerpAPI
def collect_reviews(data_id):
    params = {
        "engine": "google_maps_reviews",
        "api_key": os.getenv("SERPAPI_KEY"),  # don’t hardcode API keys
        "hl": "pl",
        "data_id": data_id,
        "sort_by": "qualityScore"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    print(json.dumps(results, indent=2, ensure_ascii=False))
    return results.get("reviews", [])

if __name__ == "__main__":
    reviews = collect_reviews("0x471ecb57a156bd51:0x64ee744a4f4b14fe")

    os.makedirs("data", exist_ok=True)

    with open("data/reviews.json", "w", encoding="utf-8") as f:
        json.dump(reviews, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(reviews)} reviews.")
