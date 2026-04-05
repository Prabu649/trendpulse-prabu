"""
TrendPulse - Task 1: Fetch Data from HackerNews API

Goal:
1. Fetch top 500 story IDs
2. Fetch each story's details
3. Categorize stories based on keywords
4. Save structured data for next task

Author: <your name>
"""

import requests
import time

# -------------------------------
# STEP 0: Define category keywords
# -------------------------------

CATEGORIES = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}


# -------------------------------
# STEP 1: Function to categorize
# -------------------------------

def categorize_title(title):
    """
    Checks which category a title belongs to based on keywords.
    Returns category name or 'other' if no match.
    """
    if not title:
        return "other"

    title_lower = title.lower()

    for category, keywords in CATEGORIES.items():
        for word in keywords:
            if word in title_lower:
                return category

    return "other"


# -------------------------------
# STEP 2: Fetch top story IDs
# -------------------------------

def fetch_top_story_ids(limit=500):
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"

    try:
        response = requests.get(url)
        response.raise_for_status()
        story_ids = response.json()

        return story_ids[:limit]

    except requests.RequestException as e:
        print(f"Error fetching story IDs: {e}")
        return []


# -------------------------------
# STEP 3: Fetch story details
# -------------------------------

def fetch_story_details(story_id):
    url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    except requests.RequestException:
        return None


# -------------------------------
# STEP 4: Main logic
# -------------------------------

def main():
    print("Fetching top stories...")

    story_ids = fetch_top_story_ids()

    collected_data = []

    for idx, story_id in enumerate(story_ids):
        story = fetch_story_details(story_id)

        if story is None:
            continue

        title = story.get("title", "")
        url = story.get("url", "")
        score = story.get("score", 0)

        category = categorize_title(title)

        collected_data.append({
            "id": story_id,
            "title": title,
            "url": url,
            "score": score,
            "category": category
        })

        # Small delay to avoid overwhelming API
        time.sleep(0.01)

        # Progress indicator
        if idx % 50 == 0:
            print(f"Processed {idx} stories...")

    print(f"\nTotal stories collected: {len(collected_data)}")

    # -------------------------------
    # STEP 5: Save raw data to file
    # -------------------------------

    import json

    with open("task1_output.json", "w", encoding="utf-8") as f:
        json.dump(collected_data, f, indent=4)

    print("Data saved to task1_output.json")


# -------------------------------
# ENTRY POINT
# -------------------------------

if __name__ == "__main__":
    main()