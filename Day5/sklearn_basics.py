from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import numpy as np

np.set_printoptions(suppress=True,precision=4)

model=LogisticRegression()#创建了一台没学过任何东西的分类机器

iris=load_iris()

X=iris.data

y=iris.target

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model.fit(X_train,y_train)#让模型根据训练数据开始学习

y_pred=model.predict(X_test)#把模型测试的答案存到y_test

cm=confusion_matrix(y_test,y_pred)

accuracy=accuracy_score(y_test,y_pred)

print(cm)

#print(classification_report(y_test,y_pred))

#print(accuracy)

#print(y_pred)

#print(y_test)

#print(model.score(X_test,y_test))

#print(model.coef_)#每个特征的权重
#print(model.intercept_)#每个特征的偏置

#print(model.predict_proba(X_test[:5]))

#print(X_train.shape)
#print(X_test.shape)
#print(y_train.shape)
#print(y_test.shape)

#print(X.shape)
#print(y.shape)

#print(X[:5])
#print(y[:5])

#print(iris.data[:5])

#print(iris.target[:5])

#print(iris)

#print(iris.data)
#print(iris.target)