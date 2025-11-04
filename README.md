# Titanic Dataset Cleaning and Preprocessing

## 📘 Project Title
**Titanic Dataset Cleaning and Preprocessing**

---

## 📄 Description
This project involves cleaning and preprocessing the **Titanic dataset** from Kaggle.  
The dataset contains passenger information such as age, class, sex, and fare.  
The goal is to prepare the data for analysis and machine learning by handling missing values, removing duplicates, treating outliers, and fixing data types.

---

## 🧠 Objectives
1. Load the dataset into Pandas.  
2. Identify and handle missing values in *Age* and *Cabin*.  
3. Remove duplicates.  
4. Detect and treat outliers in *Fare*.  
5. Fix incorrect data types.  
6. Save the cleaned version as `titanic_clean.csv`.

---

## ⚙️ Tools & Libraries
- Python  
- Pandas  
- Matplotlib  

---

## 🪜 Steps Performed

### 1. Data Loading
Loaded the dataset using `pd.read_csv("train_and_test2.csv")`.

### 2. Handling Missing Values
- Replaced missing values in `Age` with the **median**.  
- Dropped the `Cabin` column due to excessive missing entries.

### 3. Removing Duplicates
Removed all duplicate rows using `df.drop_duplicates()`.

### 4. Detecting & Treating Outliers
- Created a **boxplot** to visualize outliers in the `Fare` column.  
- Applied the **Interquartile Range (IQR)** method to cap extreme values.

### 5. Fixing Data Types
Converted columns to appropriate types:
- `Survived`, `Pclass`, `Sex`, `Embarked` → categorical.

### 6. Exporting Cleaned Data
Saved the final cleaned dataset as:
