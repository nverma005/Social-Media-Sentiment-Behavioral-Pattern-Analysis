# Social Media Sentiment & Behavioural Pattern Analysis

Analyzes 7,683 Mastodon social media posts to detect echo chambers,
doom-scrolling behavior, and sentiment patterns using Python and Power BI.

## What This Project Does

- Collects posts from Mastodon home timeline via API every 2 minutes using a tkinter GUI
- Cleans raw HTML posts through 11 preprocessing steps including tokenization, lemmatization, and negation handling
- Classifies sentiment using VADER into positive, negative, and neutral
- Clusters posts into 5 echo chambers using keyword-based topic rules
- Flags doom-scrolling posts based on sentiment and harmful keywords
- Visualizes all findings in an interactive 2-page Power BI dashboard

## Key Findings

- 38% positive, 35.8% negative, 26.2% neutral across 7,683 posts
- Russia-Ukraine War echo chamber had the highest doom-scroll rate at 94%
- Health & Safety echo chamber second at 76%
- 49.5% of all posts flagged as doom-scrolling content
- 5 distinct echo chambers found across politics, climate, health, war, and business

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10 | Core language |
| Mastodon API | Data collection |
| tkinter | GUI for data collection and preprocessing |
| BeautifulSoup | HTML tag removal |
| NLTK + VADER | Text preprocessing and sentiment classification |
| langdetect | Non-English post filtering |
| Pandas | Data manipulation |
| Keyword Rules | Echo chamber clustering |
| Power BI | Dashboard and visualization |

## Project Structure

├── Dataset/
│   ├── Mastodon dataset/
│   └── Pre Processed Dataset/
├── Output/
│   ├── powerbi_ready.csv
│   └── Social_Media_Sentiment_Analysis.pbix
├── Screenshots/
│   ├── overview_page.png
│   └── behaviour_analysis_page.png
├── Scripts/
│   ├── data_collection.py
│   ├── data_pre_processing.py
│   └── methodology.py
└── README.md

## Pipeline

**Step 1: Data Collection**
Connects to Mastodon API, fetches 100 posts every 2 minutes via GUI, saves to CSV.

**Step 2: Preprocessing**
11 steps: HTML removal, special character cleaning, lowercasing, tokenization,
stopword removal, space normalization, lemmatization, negation handling,
specific word removal, non-English filtering, deduplication.
VADER assigns sentiment label to each post.

**Step 3: Analysis**
Keyword rules assign each post to one of 5 echo chambers.
Doom scroll flag added based on negative sentiment and harmful keywords.

**Step 4: Dashboard**
Power BI reads enriched CSV and visualizes sentiment, echo chambers,
doom scroll rates, trends over time, and top active users.

## Dashboard Screenshots

![Overview](Screenshots/overview_page.png)
![Behaviour Analysis](Screenshots/behaviour_analysis_page.png)

## Related

Based on MSc dissertation: Social Media Sentiment & Behavioural Pattern Analysis
University of Strathclyde, 2023-2024