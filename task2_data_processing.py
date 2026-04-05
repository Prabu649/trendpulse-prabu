"""
TrendPulse - Task 2: Clean Data & Convert to CSV

Goal:
1. Load JSON data from Task 1
2. Clean the dataset
3. Remove duplicates & invalid entries
4. Save as CSV for analysis

Author: <your name>
"""

import json
import csv


# -------------------------------
# STEP 1: Load JSON data
# -------------------------------

def load_data(filename):
    """
    Loads JSON data from file
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("File not found. Make sure Task 1 output exists.")
        return []


# -------------------------------
# STEP 2: Clean data
# -------------------------------

def clean_data(data):
    """
    Cleans dataset by:
    - Removing missing titles
    - Removing 'other' category
    - Removing duplicates
    - Standardizing text
    """
    cleaned = []
    seen_titles = set()

    for item in data:
        title = item.get("title", "").strip()
        category = item.get("category", "").strip().lower()
        url = item.get("url", "").strip()
        score = item.get("score", 0)

        # Skip invalid entries
        if not title:
            continue

        if category == "other":
            continue

        if title in seen_titles:
            continue

        if not isinstance(score, int) or score < 0:
            continue

        seen_titles.add(title)

        cleaned.append({
            "title": title,
            "category": category,
            "score": score,
            "url": url
        })

    return cleaned


# -------------------------------
# STEP 3: Save to CSV
# -------------------------------

def save_to_csv(data, filename):
    """
    Saves cleaned data to CSV file
    """
    fieldnames = ["title", "category", "score", "url"]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()

        for row in data:
            writer.writerow(row)


# -------------------------------
# STEP 4: Main function
# -------------------------------

def main():
    print("Loading data from Task 1...")

    data = load_data("task1_output.json")

    print(f"Original records: {len(data)}")

    cleaned_data = clean_data(data)

    print(f"Cleaned records: {len(cleaned_data)}")

    save_to_csv(cleaned_data, "task2_output.csv")

    print("Cleaned data saved to task2_output.csv")


# -------------------------------
# ENTRY POINT
# -------------------------------

if __name__ == "__main__":
    main()