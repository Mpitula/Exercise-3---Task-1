import pandas as pd

# Load the dataset
df = pd.read_csv("train_and_test2.csv")

# Display first few rows
print(df.head())

# Check dataset info
print(df.info())
