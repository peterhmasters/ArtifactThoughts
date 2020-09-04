from sklearn import tree

def generate_classifier(data):
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    clf = tree.DecisionTreeRegressor()
    clf = clf.fit(X, y)
    return clf