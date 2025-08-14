import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from src.collect_reviews import collect_reviews
from src.facebook_posts import fetch_facebook_posts
from src.news_articles import fetch_news_articles

load_dotenv()

st.set_page_config(page_title="Blue City Dashboard")
st.title("Blue City Warszawa Perception Dashboard")

analyzer = SentimentIntensityAnalyzer()


def sentiment_analysis(df: pd.DataFrame, text_col: str) -> pd.DataFrame:
    if df.empty:
        return df
    df = df.copy()
    df["sentiment"] = df[text_col].fillna("").apply(lambda x: analyzer.polarity_scores(x)["compound"])
    df["label"] = pd.cut(
        df["sentiment"],
        bins=[-1, -0.05, 0.05, 1],
        labels=["Negative", "Neutral", "Positive"],
    )
    return df


@st.cache_data(show_spinner=False)
def load_data():
    google = collect_reviews("0x471ecb57a156bd51:0x64ee744a4f4b14fe")
    facebook = fetch_facebook_posts("BlueCityWarszawa")
    news = fetch_news_articles("Centrum Handlowe")
    return google, facebook, news


google_df, facebook_df, news_df = load_data()

st.header("Google Reviews")
google_df = sentiment_analysis(google_df, "text")
if not google_df.empty:
    st.bar_chart(google_df["label"].value_counts())
    st.dataframe(google_df[["text", "rating", "label"]])
else:
    st.info("No Google reviews available. Check SERPAPI_KEY.")

st.header("Facebook Posts")
facebook_df = sentiment_analysis(facebook_df, "text")
if not facebook_df.empty:
    st.bar_chart(facebook_df["label"].value_counts())
    st.dataframe(facebook_df[["text", "label"]])
else:
    st.info("No Facebook posts available. Check FACEBOOK_ACCESS_TOKEN.")

st.header("News Articles")
news_df = sentiment_analysis(news_df, "text")
if not news_df.empty:
    st.bar_chart(news_df["label"].value_counts())
    st.dataframe(news_df[["text", "label"]])
else:
    st.info("No news articles available. Check NEWSAPI_KEY.")
