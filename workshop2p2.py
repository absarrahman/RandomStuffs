import pandas as pd

data = pd.read_csv("/content/iris.csv",names=["sepal_length","sepal_width","petal_length","petal_width","class"])

data

type(data)

data.head()

data.shape

data["petal_width"]

data["sepal_width"]

data[["petal_width","sepal_width"]]

data.shape

data.iloc[:,2]

data.iloc[2]

data.iloc[:,1:4]

data.loc[:,"sepal_width":"petal_width"]

data["sepal_width"]>2

data["sepal_width"]>3

data[data.sepal_width>2]

data[data.sepal_width>4]

data[(data.sepal_width>4) & (data.sepal_width<6)]

data

from sklearn.model_selection import train_test_split as tts

#class is denoted as y and feature as x

features = data.iloc[:,0:4] #(row:coloumFrom:columnTo)

features.head()

label = data.iloc[:,4]

label.head()

X_train,X_test,y_train,y_test = tts(features,label,test_size=0.2,random_state=42)

print(X_train.shape)

print(y_train.shape)

print(X_test.shape)

print(y_test.shape)

from sklearn.ensemble import AdaBoostClassifier as abc

clf = abc()

clf.fit(X_train,y_train)

clf.predict(X_test)

y_pred = clf.predict(X_test)

from sklearn.metrics import accuracy_score as accscore
accscore(y_test,y_pred)

from sklearn.metrics import classification_report as cr
print(cr(y_test,y_pred))

