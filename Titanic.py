import pandas as pd
import matplotlib.pyplot as plt

## Load the dataset
df = pd.read_csv("CSV_Files/titanic.csv")

# Display first few rows
print(df.head())

# Check dataset info
print(df.info())


## Check for missing values
print("\nMissing values in 'Age' column before handling:")
if 'Age' in df.columns:
    print(f"Age: {df['Age'].isnull().sum()}")
else:
    print("No Age column found in the dataset")

print("Missing values in 'Cabin' column before handling:")
if 'Cabin' in df.columns:
    print("Cabin:", df['Cabin'].isnull().sum())
else:
    print("No Cabin column found in the dataset")

## Handle missing values
# For Age: impute with median
if 'Age' in df.columns:
    if df['Age'].isnull().sum() > 0:
        median_age = df['Age'].median()
        # avoid chained-assignment / future warning by assigning the result back
        df['Age'] = df['Age'].fillna(median_age)
        print("\nMissing values in 'Age' column after imputation:")
        print(f"Age: {df['Age'].isnull().sum()}")

# For Cabin: drop the column
if 'Cabin' in df.columns:
    # drop Cabin column as it's sparse / not useful for this analysis
    df.drop('Cabin', axis=1, inplace=True)
    print("\nCabin column has been dropped from the dataset")

## Remove duplicates

# Check for duplicates
print(f"\nNumber of duplicates found: {df.duplicated().sum()}")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Confirm
print(f"\nNumber of duplicates remaining: {df.duplicated().sum()} ")


# Create boxplot to visualize outliers (before outlier treatment)
if 'Fare' in df.columns:
    plt.figure()
    plt.boxplot(df['Fare'].dropna())
    plt.title("Boxplot of Fare before Outlier Treatment")
    # save before show so the file contains the figure
    plt.savefig('Boxplot/my_boxplot1.png')
    plt.show()
    plt.close()
else:
    print("Column 'Fare' not found — skipping initial boxplot")

# Calculate IQR (Interquartile Range)
Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 - Q1

# Define boundaries for acceptable range
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Remove outliers
df = df[(df['Fare'] >= lower_bound) & (df['Fare'] <= upper_bound)]


# Check boxplot again after outlier treatment
if 'Fare' in df.columns and not df['Fare'].dropna().empty:
    plt.figure()
    plt.boxplot(df['Fare'].dropna())
    plt.title("Boxplot of Fare after Outlier Treatment")
    plt.savefig('Boxplot/my_boxplot2.png')
    plt.show()
    plt.close()
else:
    print("Column 'Fare' not found or empty after outlier removal — skipping final boxplot")


# Check data types
print("\n Data types before conversion:")
print(df.dtypes)

# Convert columns to correct types (categorical where applicable)
if 'Survived' in df.columns:
    df['Survived'] = df['Survived'].astype('category')

if 'Pclass' in df.columns:
    df['Pclass'] = df['Pclass'].astype('category')

if 'Sex' in df.columns:
    df['Sex'] = df['Sex'].astype('category')

if 'Embarked' in df.columns:
    df['Embarked'] = df['Embarked'].astype('category')


print("\n Data types after conversion:")
print(df.dtypes)

# Save cleaned version
df.to_csv("CSV_Files/cleaned_titanic.csv", index=False)
print("\nCleaned dataset saved as cleaned_titanic.csv")
