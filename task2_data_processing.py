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
import pandas as pd


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
    # print("Loading data from Task 1...")

    # data = load_data("task1_output.json")

    # print(f"Original records: {len(data)}")

    # cleaned_data = clean_data(data)

    # print(f"Cleaned records: {len(cleaned_data)}")

    # save_to_csv(cleaned_data, "task2_output.csv")

    # print("Cleaned data saved to task2_output.csv")
    # Step 1 — Load JSON file into DataFrame
     # Step 1 — Load JSON file into DataFrame
    input_path = "task1_output.json"
    print(f"Loading data from {input_path} ...")

    df = pd.read_json(input_path)
    print("Columns in DataFrame:", df.columns)

    # Rename 'id' to 'post_id' for consistency if needed
    if 'id' in df.columns:
        df = df.rename(columns={"id": "post_id"})

    print(f"Loaded {len(df)} stories from {input_path}")

    # Step 2a — Remove duplicates by post_id
    before = len(df)
    df = df.drop_duplicates(subset="post_id")
    after = len(df)
    print(f"After removing duplicates: {after}")

    # Step 2b — Drop rows with missing post_id, title, or score
    before = len(df)
    df = df.dropna(subset=["post_id", "title", "score"])
    after = len(df)
    print(f"After removing nulls: {after}")

    # Step 2c — Fix data types for score and num_comments
    df["score"] = df["score"].astype(int)
    if "num_comments" in df.columns:
        df["num_comments"] = df["num_comments"].fillna(0).astype(int)
    else:
        df["num_comments"] = 0

    # Step 2d — Remove stories with score < 5
    before = len(df)
    df = df[df["score"] >= 5]
    after = len(df)
    print(f"After removing low scores: {after}")

    # Step 2e — Strip whitespace from title
    df["title"] = df["title"].str.strip()

    # Step 3 — Save cleaned data as CSV
    output_path = "data/trends_clean.csv"
    df.to_csv(output_path, index=False)
    print(f"\nSaved {len(df)} rows to {output_path}")

    # Step 4 — Print summary: stories per category
    print("\nStories per category:")
    category_counts = df["category"].value_counts()
    for category, count in category_counts.items():
        print(f"  {category:<15} {count}")

if __name__ == "__main__":
    main()