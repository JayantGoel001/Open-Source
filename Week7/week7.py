import pandas as pd

columns_ = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital', 'occupation', 'relationship', 'race',
            'sex', 'capital_gain', 'capital_loss', 'hours_week', 'native_country', 'label']

df_train = pd.read_csv("adult.csv", skipinitialspace=True, names=columns_, index_col=False)
print(df_train.head())

# listing Categorical features
print("Categorical Data : \n", list(df_train.select_dtypes('object').columns))

# listing numerical features
print("Numerical Data : \n", list(df_train._get_numeric_data().columns))

# describtion
print("Describtion :\n", df_train.describe())

# describtion of all features
print("Describtion of all features :\n", df_train.describe(include="all"))

