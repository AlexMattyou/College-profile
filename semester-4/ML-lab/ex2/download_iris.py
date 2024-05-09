# run this code before working on code.ipynb
# this script will convert iris dataset into a csv file
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['species'] = iris.target_names[iris.target]
data.to_csv("iris.csv", index=False)

print("Iris dataset saved as iris.csv")