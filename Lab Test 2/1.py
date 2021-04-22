import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

data = load_wine(as_frame=True)

X, y = data['data'], data['target']

print(X.shape, y.shape)

# 1
print("Features Name :", data.feature_names)
print("Number of Features :", len(data.feature_names))

# 2
print(X.describe())
numerical = X.select_dtypes(include=['number']).shape[1]
categorical = X.select_dtypes(include=['category']).shape[1]

print("Number of categorical is {} and Number of Numerical Features are {}".format(categorical, numerical))

# 3
print("Number of Classes :", len(data.target_names))

# 4
X = X.fillna(X.mean())
print(np.isnan(X))

# 5
accuracy1 = []
accuracy2 = []
for i in range(1, 4):
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.1 * i, random_state=0)
    model1 = KNeighborsClassifier()
    model1.fit(X_train, Y_train)
    acc1 = model1.score(X_test, Y_test)
    accuracy1.append(acc1)

    model2 = GaussianNB()
    model2.fit(X_train, Y_train)
    acc2 = model2.score(X_test, Y_test)
    accuracy2.append(acc2)

mean1 = np.mean(accuracy1)
mean2 = np.mean(accuracy2)

plt.bar(["KNN", "GaussianNB"], [mean1, mean2])
plt.show()
