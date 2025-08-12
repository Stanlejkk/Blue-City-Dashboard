import os
import pandas as pd
from newsapi import NewsApiClient
from dotenv import load_dotenv

load_dotenv()


def fetch_news_articles(query: str) -> pd.DataFrame:
    api_key = os.getenv("NEWSAPI_KEY")
    if not api_key:
        return pd.DataFrame()

    try:
        newsapi = NewsApiClient(api_key=api_key)
        articles = newsapi.get_everything(q=query, language="pl")
        articles_list = articles.get("articles", [])
    except Exception:
        return pd.DataFrame()

    rows = [
        {
            "text": f"{a.get('title')} - {a.get('description')}",
            "time": a.get("publishedAt"),
        }
        for a in articles_list
    ]
    return pd.DataFrame(rows)
