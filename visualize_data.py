import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the processed dataset from Task 2
df = pd.read_csv("cleaned_books_eda.csv")

# Set overall visual theme
sns.set_theme(style="whitegrid")

# ---------------------------------------------------------
# Chart 1: Distribution of Book Prices (Histogram + KDE)
# ---------------------------------------------------------
plt.figure(figsize=(8, 5))
sns.histplot(df["Price (£)"], bins=15, kde=True, color="#2b5c8f")
plt.title("Distribution of Book Prices", fontsize=14, fontweight="bold")
plt.xlabel("Price (£)", fontsize=12)
plt.ylabel("Number of Books", fontsize=12)
plt.tight_layout()
plt.savefig("1_price_distribution.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# Chart 2: Book Count by Star Rating (Bar Chart)
# ---------------------------------------------------------
plt.figure(figsize=(8, 5))
sns.countplot(x="Rating (out of 5)", data=df, palette="viridis", hue="Rating (out of 5)", legend=False)
plt.title("Number of Books by Star Rating", fontsize=14, fontweight="bold")
plt.xlabel("Star Rating (1 to 5)", fontsize=12)
plt.ylabel("Count of Books", fontsize=12)
plt.tight_layout()
plt.savefig("2_rating_counts.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# Chart 3: Average Book Price by Star Rating (Bar Plot)
# ---------------------------------------------------------
plt.figure(figsize=(8, 5))
sns.barplot(x="Rating (out of 5)", y="Price (£)", data=df, estimator="mean", errorbar=None, palette="magma", hue="Rating (out of 5)", legend=False)
plt.title("Average Book Price by Star Rating", fontsize=14, fontweight="bold")
plt.xlabel("Star Rating (1 to 5)", fontsize=12)
plt.ylabel("Average Price (£)", fontsize=12)
plt.tight_layout()
plt.savefig("3_avg_price_by_rating.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# Chart 4: Books Share by Price Category (Pie Chart)
# ---------------------------------------------------------
category_counts = df["Price_Category"].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(
    category_counts,
    labels=category_counts.index,
    autopct="%1.1f%%",
    startangle=140,
    colors=["#66c2a5", "#fc8d62", "#8da0cb"]
)
plt.title("Share of Books by Price Category", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("4_price_category_share.png", dpi=300)
plt.close()

print("All 4 charts have been generated and saved as PNG images successfully!")