from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

#1.加载数据
iris=load_iris()

X=iris.data
y=iris.target


#2.划分训练集和测试集
X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


#3.创建模型
model=LogisticRegression()


#4.训练模型
model.fit(X_train,y_train)


#5.预测
y_pred=model.predict(X_test)


#6.模型评价
accuracy=accuracy_score(y_test,y_pred)


print("Accuracy:",accuracy)


print("\nClassification Report:")
print(classification_report(y_test,y_pred))


print("Confusion Matrix:")
print(confusion_matrix(y_test,y_pred))