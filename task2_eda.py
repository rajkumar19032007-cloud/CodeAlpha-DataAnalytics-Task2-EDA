import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

df = pd.read_csv('custom_books_dataset.csv')
print("Shape:", df.shape)
print("Missing values:\n", df.isnull().sum())
print("Stats:\n", df.describe())

# Plot 1: Price histogram
plt.figure(figsize=(10,6))
sns.histplot(df['price'], bins=30, kde=True)
plt.title('Book Price Distribution')
plt.savefig('price_distribution.png')
plt.close()

# Plot 2: Price vs Rating
plt.figure(figsize=(10,6))
sns.scatterplot(x='rating', y='price', data=df)
plt.title('Price vs Rating')
plt.savefig('price_vs_rating.png')
plt.close()

# Plot 3: Top categories
if 'category' in df.columns:
    plt.figure(figsize=(12,6))
    df['category'].value_counts().head(10).plot(kind='barh')
    plt.title('Top 10 Categories')
    plt.savefig('top_categories.png')
    plt.close()

print("EDA Complete. 3 plots saved!")
