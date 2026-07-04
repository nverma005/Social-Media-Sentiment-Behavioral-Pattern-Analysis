# Social Media Sentiment & Behavioural Pattern Analysis

Analyzes 7,683 Mastodon social media posts to detect echo chambers, doom-scrolling behavior, and sentiment patterns using Python and Power BI.

## What This Project Does

- Collects posts from Mastodon home timeline via API every 2 minutes using a tkinter GUI
- Cleans raw HTML posts through 11 preprocessing steps including tokenization, lemmatization, and negation handling
- Classifies sentiment using VADER into positive, negative, and neutral
- Clusters posts into 5 echo chambers using keyword-based topic rules
- Flags doom-scrolling posts based on sentiment and harmful keywords
- Visualizes findings in an interactive 2-page Power BI dashboard

## Key Findings

- 38% positive, 35.8% negative, 26.2% neutral across 7,683 posts
- Russia-Ukraine War echo chamber had the highest doom-scroll rate at 94%
- Health & Safety echo chamber second at 76%
- 49.5% of all posts flagged as doom-scrolling content
- 5 distinct echo chambers identified across politics, climate, health, war, and business

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

├── Mastodon dataset/            # Raw collected data
├── Pre Processed Dataset/       # Cleaned data
├── Output/
│   ├── powerbi_ready.csv        # Enriched dataset
│   └── Social_Media_Sentiment_Analysis.pbix
├── Screenshots/                 # UI and dashboard screenshots
├── Scripts/
│   ├── user_interface.py        # Main GUI entry point
│   ├── data_access_layer.py     # Connects UI to logic
│   ├── data_collection.py       # Mastodon API collection
│   ├── data_pre_processing.py   # 11-step NLP pipeline
│   └── methodology.py           # Echo chamber and doom scroll detection
└── README.md

## How to Run

1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your Mastodon credentials:

MASTODON_CLIENT_ID=your_client_key
MASTODON_CLIENT_SECRET=your_client_secret
MASTODON_ACCESS_TOKEN=your_access_token
MASTODON_URL=https://mastodon.social

4. Run: `python Scripts/user_interface.py`
5. Follow the 3 steps in the GUI

## Dashboard Screenshots

![Overview](Screenshots/overview_page.png)
![Behaviour Analysis](Screenshots/behaviour_analysis_page.png)

## Related

Based on MSc dissertation: Social Media Sentiment & Behavioural Pattern Analysis
University of Strathclyde, 2023-2024