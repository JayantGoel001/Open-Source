import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

columns_ = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital', 'occupation', 'relationship', 'race',
            'sex', 'capital_gain', 'capital_loss', 'hours_week', 'native_country', 'label']

df_train = pd.read_csv("adult.csv", skipinitialspace=True, names=columns_, index_col=False)
print(df_train.head())

# listing Categorical features
categorical_data = list(df_train.select_dtypes('object').columns)
print("Categorical Data : \n", categorical_data)

# listing numerical features
numerical_data = list(df_train._get_numeric_data().columns)
print("Numerical Data : \n", numerical_data)

# describtion
print("Describtion :\n", df_train.describe())

# describtion of all features
print("Describtion of all features :\n", df_train.describe(include="all"))

# Column Index of Categorical data
print("Column Index of Categorical data:")
for feature in categorical_data:
    print(df_train.columns.get_loc(feature), end=" ")
print("\n")

# Column Index of Numerical data
print("Column Index of Numerical data:")
for feature in numerical_data:
    print(df_train.columns.get_loc(feature), end=" ")
print("\n")

# Transforming String Data into Integer format.
le = LabelEncoder()
for feature in categorical_data:
    df_train[feature] = le.fit_transform(df_train[feature])

print(df_train.head())

# Replacing missing value with mean value
imp = SimpleImputer(missing_values=0, strategy='mean')
