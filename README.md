# Blue City Warszawa Perception Dashboard

This Streamlit application aggregates public opinion about the **Blue City Warszawa** shopping center from multiple sources:

- Google Maps reviews (via [SerpAPI](https://serpapi.com/))
- Facebook posts (via Facebook Graph API)
- Online news articles (via [NewsAPI](https://newsapi.org/))

The data is analysed with [VADER sentiment analysis](https://github.com/cjhutto/vaderSentiment) and visualised as interactive charts.

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Provide API credentials in environment variables or a `.env` file:

   - `SERPAPI_KEY` – Google Maps reviews
   - `FACEBOOK_ACCESS_TOKEN` – Facebook Graph API
   - `NEWSAPI_KEY` – News API

## Usage

Run the dashboard with Streamlit:

```bash
streamlit run main.py
```

If any of the API keys are missing, the corresponding section of the dashboard will display a message instead of data.
