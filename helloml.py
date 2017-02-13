from sklearn import tree

#features 1 --> Smooth 2-->bumbpy
features = [[140, 1], [138, 1], [150, 0], [170, 0]]

#labels 0 --> Apple, 1 --> Smooth
labels = [0,0,1,1]

#classifier
clf = tree.DecisionTreeClassifier()

#train the classifier
clf = clf.fit(features, labels)

#predict the fruit
print clf.predict([[150, 1]])