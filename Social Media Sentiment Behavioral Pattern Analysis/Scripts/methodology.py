import pandas as pd

df = pd.read_csv("Dataset/Pre Processed Dataset/pre_processed_data.csv")
df['Date Time'] = pd.to_datetime(df['Date Time'], format='mixed').dt.tz_localize(None)
df['User Name'] = df['User Name'].fillna('Unknown')

def assign_cluster(text):
    text = str(text).lower()
    
    # Politics - broadened
    if any(w in text for w in [
        'trump', 'election', 'president', 'minister', 'politics', 'modi', 
        'india', 'government', 'party', 'vote', 'democrat', 'republican',
        'congress', 'senate', 'policy', 'law', 'court', 'judge', 'legal',
        'case', 'investigation', 'scandal', 'campaign', 'political'
    ]):
        return 'EC0 - Politics & World Affairs'
    
    # Russia-Ukraine - broadened
    elif any(w in text for w in [
        'ukraine', 'russia', 'war', 'military', 'sanction', 'nato',
        'grain', 'invasion', 'zelensky', 'putin', 'weapon', 'bomb',
        'missile', 'frontline', 'refugee', 'conflict', 'troops', 'army'
    ]):
        return 'EC3 - Russia-Ukraine War'
    
    # Health & Safety - broadened
    elif any(w in text for w in [
        'health', 'hospital', 'police', 'death', 'water', 'covid',
        'died', 'killed', 'fire', 'flood', 'disaster', 'emergency',
        'crime', 'arrest', 'shooting', 'victim', 'accident', 'drug',
        'disease', 'mental', 'vaccine', 'medical', 'doctor', 'nurse'
    ]):
        return 'EC2 - Health & Safety'
    
    # Business & Economy - broadened
    elif any(w in text for w in [
        'business', 'inflation', 'economy', 'bank', 'energy', 'billion',
        'market', 'stock', 'trade', 'company', 'corporate', 'startup',
        'investment', 'gdp', 'recession', 'tax', 'finance', 'revenue',
        'profit', 'loss', 'budget', 'price', 'cost', 'money', 'fund'
    ]):
        return 'EC4 - Business & Economy'
    
    # Climate & Tech - broadened (catches most remaining)
    elif any(w in text for w in [
        'climate', 'heat', 'wildfire', 'temperature', 'global', 'carbon',
        'twitter', 'biden', 'microsoft', 'tech', 'ai', 'social', 'media',
        'internet', 'digital', 'data', 'science', 'research', 'study',
        'news', 'report', 'world', 'people', 'new', 'day', 'time', 'year'
    ]):
        return 'EC1 - Climate & Tech'
    
    else:
        return 'EC1 - Climate & Tech'  # true fallback, should be minimal now

df['cluster'] = df['text'].apply(assign_cluster)
df['echo_chamber'] = df['cluster']

def flag_doom(row):
    doom_keywords = [
        'war', 'death', 'kill', 'crisis', 'attack', 'disaster',
        'flood', 'fire', 'murder', 'violence', 'ukraine', 'russia',
        'terror', 'threat', 'fear', 'panic', 'dead', 'hospital',
        'died', 'shooting', 'explosion', 'protest', 'arrested',
        'victim', 'abuse', 'corrupt', 'collapse', 'fail', 'danger'
    ]
    text = str(row['text']).lower()
    is_negative = row['Sentiment'] == 'negative'
    has_doom_word = any(w in text for w in doom_keywords)
    return 1 if (is_negative or has_doom_word) else 0

df['doom_scroll'] = df.apply(flag_doom, axis=1)

# --- Save enriched file ---
df.to_csv("Output/PowerBi Alalysis data.csv", index=False)

print("Done!")
print("\nCluster distribution:")
print(df['cluster'].value_counts())
print("\nDoom scroll %:", round(df['doom_scroll'].mean() * 100, 2))
print("\nGeneral count:", len(df[df['cluster'] == 'General']))