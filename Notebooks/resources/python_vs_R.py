import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm

def main():

    names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "Name"]
    iris_data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", names = names)
    train, test = train_test_split(iris_data, test_size=0.2)

    X_train = train.drop('Name', axis=1)
    y_train = train['Name']
    X_test = test.drop('Name', axis=1)
    y_test = test['Name']

    # logistic regression
    lr = LogisticRegression(solver='lbfgs', multi_class='auto', max_iter=1000)
    lr.fit(X_train, y_train)

    # linear discriminant analysis
    lda = LinearDiscriminantAnalysis()
    lda.fit(X_train,y_train)

    # KNN (k-nearest neighbours)
    parameters = {'n_neighbors': range(1,11)}
    knn = GridSearchCV(KNeighborsClassifier(), parameters, scoring = 'accuracy', cv = KFold(n_splits=5))
    knn.fit(X_train,y_train)

    # SVM
    parameters = {'C': range(1,11)}
    svc = GridSearchCV(svm.SVC(kernel = 'linear'), parameters, scoring = 'accuracy', cv = KFold(n_splits=5))
    svc.fit(X_train,y_train)

    # evaluate
    lr_test_acc = lr.score(X_test,y_test)
    lda_test_acc = lda.score(X_test,y_test)
    knn_test_acc = knn.best_estimator_.score(X_test,y_test)
    svc_test_acc= svc.best_estimator_.score(X_test,y_test)

    # print(lr_test_acc, lda_test_acc, knn_test_acc, svc_test_acc)
