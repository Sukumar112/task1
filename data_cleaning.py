import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("Titanic-Dataset.csv")

df_cleaned = df.drop(columns=['Cabin', 'Ticket', 'Name'])

df_cleaned['Age'].fillna(df_cleaned['Age'].median(), inplace=True)
df_cleaned['Embarked'].fillna(df_cleaned['Embarked'].mode()[0], inplace=True)

df_cleaned['Sex'] = df_cleaned['Sex'].map({'male': 0, 'female': 1})
df_cleaned = pd.get_dummies(df_cleaned, columns=['Embarked'], drop_first=True)

df_cleaned['FamilySize'] = df_cleaned['SibSp'] + df_cleaned['Parch']

scaler = StandardScaler()
df_cleaned[['Age', 'Fare']] = scaler.fit_transform(df_cleaned[['Age', 'Fare']])

df_cleaned.to_csv("Titanic-Dataset-Cleaned.csv", index=False)
