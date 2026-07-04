# Social Media Sentiment & Behavioural Pattern Analysis

Built a Python tool that collects live social media posts, analyses sentiment, 
detects echo chambers, and flags doom-scrolling content. Results visualised 
in a Power BI dashboard.

**Dataset:** 7,683 Mastodon posts collected via API  
**Tools:** Python, NLTK, VADER, Pandas, Power BI  
**Type:** End-to-end NLP pipeline with GUI

---

## What I Built

A 3-step application with a tkinter GUI:

**Step 1: Data Collection**  
Connects to Mastodon API and pulls 100 posts every 2 minutes. Saves to CSV automatically.

**Step 2: Preprocessing**  
Cleans raw HTML posts through 11 steps: HTML removal, tokenization, lemmatization, 
stopword removal, negation handling, language filtering, and deduplication. 
VADER assigns sentiment to each post.

**Step 3: Analysis**  
Assigns posts to 5 echo chambers using keyword rules. Flags doom-scrolling content 
based on negative sentiment and harmful keywords. Outputs enriched CSV for Power BI.

---

## Key Results

| Finding | Value |
|---|---|
| Total posts analysed | 7,683 |
| Positive sentiment | 38% |
| Negative sentiment | 35.8% |
| Doom-scroll rate (Russia-Ukraine chamber) | 94% |
| Doom-scroll rate (Health & Safety chamber) | 76% |
| Overall doom-scroll rate | 49.5% |
| Echo chambers detected | 5 |

---

## Echo Chambers Found

- EC0: Politics & World Affairs
- EC1: Climate & Tech
- EC2: Health & Safety
- EC3: Russia-Ukraine War (highest doom-scroll rate at 94%)
- EC4: Business & Economy

---

## Dashboard

Built in Power BI with 2 pages covering sentiment distribution, post volume 
by echo chamber, doom-scroll rates, sentiment trends over time, and top active users.

![Overview](Screenshots/overview_page.png)
![Behaviour Analysis](Screenshots/behaviour_analysis_page.png)

---

## How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Add your Mastodon credentials to a .env file
MASTODON_CLIENT_ID=your_key
MASTODON_CLIENT_SECRET=your_secret
MASTODON_ACCESS_TOKEN=your_token
MASTODON_URL=https://mastodon.social

# Launch the app
python Scripts/user_interface.py
```

---

## Project Structure

```
├── Mastodon dataset/
├── Pre Processed Dataset/
├── Output/
│   ├── powerbi_ready.csv
│   └── Social_Media_Sentiment_Analysis.pbix
├── Screenshots/
├── Scripts/
│   ├── user_interface.py
│   ├── data_access_layer.py
│   ├── data_collection.py
│   ├── data_pre_processing.py
│   └── methodology.py
├── requirements.txt
└── README.md
```

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