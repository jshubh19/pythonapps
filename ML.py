from sklearn import tree
import sklearn


#collection of training data

features= [[140,1],[130,1],[150,0],[170,0]]
labels= [0,0,1,1]

#train the data

clf=tree.DecisionTreeClassifier()
clf= clf.fit(features, labels)

#prediction
print (clf.predict([[150,0]]))
