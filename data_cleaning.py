df_cleaned = df.drop(columns=['Cabin', 'Ticket', 'Name'])

df_cleaned['Age'].fillna(df_cleaned['Age'].median(), inplace=True)
df_cleaned['Embarked'].fillna(df_cleaned['Embarked'].mode()[0], inplace=True)

df_cleaned['Sex'] = df_cleaned['Sex'].map({'male': 0, 'female': 1})
df_cleaned = pd.get_dummies(df_cleaned, columns=['Embarked'], drop_first=True)

df_cleaned['FamilySize'] = df_cleaned['SibSp'] + df_cleaned['Parch']

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df_cleaned[['Age', 'Fare']] = scaler.fit_transform(df_cleaned[['Age', 'Fare']])

df_cleaned_info = df_cleaned.info()
df_cleaned_head = df_cleaned.head()

df_cleaned_info, df_cleaned_head
