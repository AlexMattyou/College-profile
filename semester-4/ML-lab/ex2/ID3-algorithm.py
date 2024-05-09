from collections import Counter
import math
import pandas as pd

class Node:
    def __init__(self, attribute=None, value=None, results=None, tb=None, fb=None):
        self.attribute = attribute
        self.value = value
        self.results = results
        self.tb = tb
        self.fb = fb

def entropy(data):
    counts = Counter(data)
    entropy_val = 0.0
    total = len(data)
    for key in counts:
        prob = counts[key] / total
        entropy_val -= prob * math.log(prob, 2)
    return entropy_val

def split_data(data, attribute, value):
    true_rows = data[data[attribute] == value]
    false_rows = data[data[attribute] != value]
    return true_rows, false_rows

def unique_values(data, attribute):
    return data[attribute].unique()

def build_tree(data, features):
    if len(features) == 0:
        return Node(results=Counter(data.iloc[:, -1]))
    
    current_entropy = entropy(data.iloc[:, -1])
    best_gain = 0.0
    best_criteria = None
    best_sets = None
    
    for feature in features:
        values = unique_values(data, feature)
        for value in values:
            true_data, false_data = split_data(data, feature, value)
            p = len(true_data) / len(data)
            gain = current_entropy - (p * entropy(true_data.iloc[:, -1]) + (1 - p) * entropy(false_data.iloc[:, -1]))
            if gain > best_gain:
                best_gain = gain
                best_criteria = (feature, value)
                best_sets = (true_data, false_data)
    
    if best_gain > 0:
        true_branch = build_tree(best_sets[0], features)
        false_branch = build_tree(best_sets[1], features)
        return Node(attribute=best_criteria[0], value=best_criteria[1], tb=true_branch, fb=false_branch)
    else:
        return Node(results=Counter(data.iloc[:, -1]))

def classify(sample, tree):
    if tree.results is not None:
        return tree.results.most_common(1)[0][0]
    else:
        val = sample[tree.attribute]
        branch = None
        if isinstance(val, int) or isinstance(val, float):
            if val >= tree.value: branch = tree.tb
            else: branch = tree.fb
        else:
            if val == tree.value: branch = tree.tb
            else: branch = tree.fb
        return classify(sample, branch)

# Example usage
data = pd.read_csv("iris.csv")
features = data.columns[:-1].tolist()
tree = build_tree(data, features)

# Example classification
sample = {'sepal_length': 5.0, 'sepal_width': 3.0, 'petal_length': 1.0, 'petal_width': 0.1}
classification = classify(sample, tree)
print("Classification for sample:", classification)


'''
OUTPUT:

Classification for sample: setosa

'''