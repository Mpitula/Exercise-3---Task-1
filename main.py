import pandas as pd

# Load the dataset
df = pd.read_csv("train_and_test2.csv")

# Display first few rows
print(df.head())

# Check dataset info
print(df.info())


# Check for missing values
print(df.isnull().sum())
# Fill missing values with column mean
df.fillna(df.mean(), inplace=True)
# Verify no missing values remain
print(df.isnull().sum())
