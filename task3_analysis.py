"""
TrendPulse - Task 3: Data Analysis using Pandas & NumPy

Goal:
1. Load cleaned CSV data
2. Perform statistical analysis
3. Generate insights from trending stories

Author: <your name>
"""

import pandas as pd
import numpy as np


# -------------------------------
# STEP 1: Load dataset
# -------------------------------

def load_data(filename):
    """
    Loads CSV into Pandas DataFrame
    """
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print("CSV file not found. Run Task 2 first.")
        return None


# -------------------------------
# STEP 2: Analysis functions
# -------------------------------

def analyze_data(df):
    """
    Perform all required analysis
    """

    print("\n--- BASIC INFO ---")
    print(df.head())

    # --------------------------------
    # 1. Total stories per category
    # --------------------------------
    print("\n--- STORIES PER CATEGORY ---")
    category_counts = df["category"].value_counts()
    print(category_counts)

    # --------------------------------
    # 2. Average score per category
    # --------------------------------
    print("\n--- AVERAGE SCORE PER CATEGORY ---")
    avg_scores = df.groupby("category")["score"].mean()
    print(avg_scores)

    # --------------------------------
    # 3. Top 5 highest-scoring stories
    # --------------------------------
    print("\n--- TOP 5 STORIES ---")
    top_stories = df.sort_values(by="score", ascending=False).head(5)
    print(top_stories[["title", "score", "category"]])

    # --------------------------------
    # 4. Category with highest average score
    # --------------------------------
    best_category = avg_scores.idxmax()
    print(f"\nCategory with highest avg score: {best_category}")

    # --------------------------------
    # 5. Overall statistics using NumPy
    # --------------------------------
    print("\n--- SCORE STATISTICS ---")

    scores = df["score"].values

    print(f"Mean score: {np.mean(scores):.2f}")
    print(f"Median score: {np.median(scores):.2f}")
    print(f"Max score: {np.max(scores)}")
    print(f"Min score: {np.min(scores)}")


# -------------------------------
# STEP 3: Save summary (optional but smart)
# -------------------------------

def save_summary(df):
    """
    Save grouped summary to CSV (bonus marks move)
    """

    summary = df.groupby("category")["score"].agg(["count", "mean", "max"])
    summary.to_csv("task3_summary.csv")

    print("\nSummary saved to task3_summary.csv")


# -------------------------------
# MAIN FUNCTION
# -------------------------------

def main():
    print("Loading cleaned dataset...")

    df = load_data("task2_output.csv")

    if df is None:
        return

    analyze_data(df)
    save_summary(df)


# -------------------------------
# ENTRY POINT
# -------------------------------

if __name__ == "__main__":
    main()