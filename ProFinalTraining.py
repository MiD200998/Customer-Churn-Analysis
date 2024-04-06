# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:41:28 2020

@author: desai_prerna
"""


from sklearn.preprocessing import normalize
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

train = pd.read_csv('Train_data.csv')
test = pd.read_csv('Test_data.csv')
models_dict = {}
X_train = train.iloc[:, [4,5,7,9,18,19]]
y_train = train.iloc[:, -1]


#X_test = test.iloc[:, [4,5,7,9,18,19]]
#y_test = test.iloc[:, -1]


from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
X_train.iloc[:,0] = labelencoder.fit_transform(X_train.iloc[:,0]).astype('float64')
#X_test.iloc[:,0] = labelencoder.fit_transform(X_test.iloc[:,0]).astype('float64')
models_dict["labelencoder"] = labelencoder

labelencoder1 = LabelEncoder()
X_train.iloc[:,1] = labelencoder1.fit_transform(X_train.iloc[:,1]).astype('float64')
#X_test.iloc[:,1] = labelencoder1.fit_transform(X_test.iloc[:,1]).astype('float64')
models_dict["labelencoder1"] = labelencoder1

labelencoder_y = LabelEncoder()
y_train = labelencoder_y.fit_transform(y_train)
#y_test = labelencoder_y.fit_transform(y_test)
models_dict["labelencoder_y"] = labelencoder_y

from sklearn.ensemble import RandomForestClassifier
classifier_RandForest = RandomForestClassifier(n_estimators = 100, criterion='gini', random_state = 0)

classifier_RandForest.fit(X_train, y_train)
#y_pred = classifier_RandForest.predict(X_test)

from sklearn.metrics import confusion_matrix, accuracy_score
#cm_RandForest = confusion_matrix(y_test, y_pred)
#print(accuracy_score(y_test, y_pred))

y_train_pred = classifier_RandForest.predict(X_train)
cm_RandForest = confusion_matrix(y_train, y_train_pred)
print(accuracy_score(y_train, y_train_pred))

models_dict["Random Forest"] = classifier_RandForest

with open("trained_model.pkl", "wb") as f:
	pickle.dump(models_dict, f)