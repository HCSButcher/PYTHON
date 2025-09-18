# Part 1: Data Loading and Basic Exploration
import pandas as pd

# Load data
df = pd.read_csv('metadata.csv')

# Preview data
print("First 5 rows:")
print(df.head())

# Dimensions
print(f"\nDataset Shape: {df.shape}")

# Data types
print("\nColumn Data Types:")
print(df.dtypes)

# Missing values
print("\nMissing Values per Column:")
print(df.isnull().sum())

# Summary statistics
print("\nSummary Statistics for Numerical Columns:")
print(df.describe())

# Part 2: Data Cleaning and Preparation

# Drop rows with missing 'title' or 'publish_time'
df_clean = df.dropna(subset=['title', 'publish_time'])

# Convert publish_time to datetime
df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')

# Create year column
df_clean['year'] = df_clean['publish_time'].dt.year

# Create a new column: abstract word count
df_clean['abstract_word_count'] = df_clean['abstract'].fillna("").apply(lambda x: len(x.split()))

print("\nCleaned Dataset Shape:", df_clean.shape)
print(df_clean[['title', 'year', 'abstract_word_count']].head())


import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud

# Part 3: Data Analysis and Visualization

# 1. Count papers by publication year
year_counts = df_clean['year'].value_counts().sort_index()

plt.figure(figsize=(8, 4))
plt.bar(year_counts.index, year_counts.values)
plt.title('Publications by Year')
plt.xlabel('Year')
plt.ylabel('Number of Publications')
plt.show()

# 2. Top journals publishing COVID-19 research
top_journals = df_clean['journal'].value_counts().head(10)

plt.figure(figsize=(8, 4))
top_journals.plot(kind='bar')
plt.title('Top 10 Journals Publishing COVID-19 Research')
plt.xlabel('Journal')
plt.ylabel('Number of Publications')
plt.xticks(rotation=45, ha='right')
plt.show()

# 3. Most frequent words in titles
titles = " ".join(df_clean['title'].dropna())
word_freq = Counter(titles.lower().split())
common_words = word_freq.most_common(20)
print("\nMost Frequent Words in Titles:")
print(common_words)

# 4. Word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud of Paper Titles")
plt.show()
