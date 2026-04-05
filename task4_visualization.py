"""
TrendPulse - Task 4: Data Visualization

Goal:
1. Load cleaned CSV data
2. Create visual charts
3. Save plots as image files

Author: <your name>
"""

import pandas as pd
import matplotlib.pyplot as plt


# -------------------------------
# STEP 1: Load dataset
# -------------------------------

def load_data(filename):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        print("CSV file not found. Run Task 2 first.")
        return None


# -------------------------------
# STEP 2: Plot functions
# -------------------------------

def plot_category_counts(df):
    """
    Bar chart: Number of stories per category
    """
    counts = df["category"].value_counts()

    plt.figure(figsize=(8, 5))
    counts.plot(kind="bar", color="skyblue")

    plt.title("Stories per Category")
    plt.xlabel("Category")
    plt.ylabel("Number of Stories")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig("chart_category_counts.png")
    plt.show()


def plot_category_distribution(df):
    """
    Pie chart: Distribution of categories
    """
    counts = df["category"].value_counts()

    plt.figure(figsize=(6, 6))
    counts.plot(kind="pie", autopct="%1.1f%%", startangle=140)

    plt.title("Category Distribution")
    plt.ylabel("")

    plt.savefig("chart_category_pie.png")
    plt.show()


def plot_avg_scores(df):
    """
    Bar chart: Average score per category
    """
    avg_scores = df.groupby("category")["score"].mean()

    plt.figure(figsize=(8, 5))
    avg_scores.plot(kind="bar", color="orange")

    plt.title("Average Score per Category")
    plt.xlabel("Category")
    plt.ylabel("Average Score")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig("chart_avg_scores.png")
    plt.show()


def plot_top_stories(df):
    """
    Bonus: Top 5 highest scoring stories
    """
    top = df.sort_values(by="score", ascending=False).head(5)

    plt.figure(figsize=(10, 5))
    plt.barh(top["title"], top["score"], color="green")

    plt.title("Top 5 Stories by Score")
    plt.xlabel("Score")
    plt.ylabel("Title")

    plt.gca().invert_yaxis()  # Highest score on top

    plt.tight_layout()
    plt.savefig("chart_top_stories.png")
    plt.show()


# -------------------------------
# MAIN FUNCTION
# -------------------------------

def main():
    print("Loading dataset...")

    df = load_data("task2_output.csv")

    if df is None:
        return

    print("Generating visualizations...")

    plot_category_counts(df)
    plot_category_distribution(df)
    plot_avg_scores(df)
    plot_top_stories(df)

    print("All charts saved successfully!")


# -------------------------------
# ENTRY POINT
# -------------------------------

if __name__ == "__main__":
    main()