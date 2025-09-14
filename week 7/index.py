import pandas as pd
import matplotlib.pyplot as plt

#  Load and Explore the Dataset

# We'll use the Iris dataset from sklearn and convert it to a pandas DataFrame
from sklearn.datasets import load_iris

try:
    # Load Iris dataset
    iris_data = load_iris()
    df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)

    # Display first few rows
    print("First 5 rows of the dataset:")
    display(df.head())

    # Check data types and missing values
    print("\nDataset Info:")
    df.info()

    print("\nMissing Values:")
    print(df.isnull().sum())

    # Clean dataset (no missing values in Iris, but if there were, we could drop or fill)
    df = df.dropna()
except FileNotFoundError:
    print("Error: Dataset file not found.")
except Exception as e:
    print(f"An error occurred while loading the dataset: {e}")

# Basic Data Analysis
print("\nBasic Statistics:")
display(df.describe())

# Grouping by species and computing mean for each group
grouped_means = df.groupby('species').mean()
print("\nMean of Numerical Columns by Species:")
display(grouped_means)

# Interesting Finding: Petal measurements seem most discriminative between species
print("\nInteresting Finding:")
print("The petal length and petal width show significant differences between species,"
      " which is why they are very important for classification.")

#  Data Visualization

# 1. Line Chart (We'll plot sepal length as if it were a time series just for visualization)
plt.figure(figsize=(10, 5))
plt.plot(df['sepal length (cm)'], label='Sepal Length')
plt.title('Line Chart of Sepal Length')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.show()

# 2. Bar Chart (Average petal length per species)
plt.figure(figsize=(8, 5))
grouped_means['petal length (cm)'].plot(kind='bar')
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

# 3. Histogram (Distribution of sepal width)
plt.figure(figsize=(8, 5))
plt.hist(df['sepal width (cm)'], bins=15, edgecolor='black')
plt.title('Histogram of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter Plot (Sepal length vs Petal length)
plt.figure(figsize=(8, 5))
for species in df['species'].unique():
    subset = df[df['species'] == species]
    plt.scatter(subset['sepal length (cm)'], subset['petal length (cm)'], label=species)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.show()
