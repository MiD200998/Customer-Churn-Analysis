import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier


def value(form_data):
	list1 = []
#	print(form_data.values())
	for x in form_data.values():
#		print(x)
		list1.append(x)
#	print(list1[0])	
	if list1[0] == 'yes':
		list1.insert(0, 1)
	else:
		list1.insert(0, 0)
	del(list1[1])
	if list1[1] == 'yes':
		list1.insert(1, 1)
	else:
		list1.insert(1, 0)
	del(list1[2])
	arr = [int(x) for x in list1]
	with open("trained_model.pkl", "rb") as f:
		models = pickle.load(f)
	arr = np.array(arr).reshape(1,-1)
	result = models["Random Forest"].predict(arr)
	result_final = models["labelencoder_y"].inverse_transform(result)
	if result_final == "True":
		return "churn"
	else:
		return "not churn"
	