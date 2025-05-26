# Titanic Dataset - Data Cleaning and Preprocessing

This project involves cleaning and preprocessing the Titanic dataset to prepare it for machine learning and data analysis.

## 📁 Dataset
The dataset is based on the classic [Titanic](https://www.kaggle.com/c/titanic) problem from Kaggle.

## ✅ Steps Performed

1. **Dropped Unnecessary Columns**
   - Removed `Cabin`, `Ticket`, and `Name`.

2. **Handled Missing Values**
   - Filled `Age` with median.
   - Filled `Embarked` with mode (most common value).

3. **Converted Categorical Variables**
   - Converted `Sex` to numeric (`male` = 0, `female` = 1).
   - Applied one-hot encoding to `Embarked`.

4. **Feature Engineering**
   - Created `FamilySize` from `SibSp + Parch`.

5. **Feature Scaling**
   - Scaled `Age` and `Fare` using `StandardScaler`.

## 📂 Files

- `Titanic-Dataset.csv` — Original dataset.
- `Titanic-Dataset-Cleaned.csv` — Cleaned version of the dataset.
- `data_cleaning.py` — Python script used to clean the data.

## 🚀 How to Use

1. Clone the repo or download the files.
2. Open `data_cleaning.py` in any Python IDE.
3. Run the script to clean the data.
4. Use the cleaned dataset for your machine learning tasks.

---

## 📌 Requirements

- Python 3.x
- pandas
- scikit-learn

Install dependencies:
```bash
pip install pandas scikit-learn
