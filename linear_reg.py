import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

dataset = pd.read_csv('data.csv')
#print("Done")


def recursiveLR(df, number):
	#print(number)
	X_train = df.iloc[:,0]
	Y_train = df.iloc[:,1]
	LR = LinearRegression()
	LR.fit(X_train.values.reshape(-1, 1), Y_train.values)
	predict = LR.predict(X_train.values.reshape(-1, 1))
	Y_train1 = Y_train.to_list()
	X_up = []
	Y_up = []
	X_down = []
	Y_down = []
	df.set_index('y_axis', inplace = True)
	#print(df.index)
	for i in range(len(predict)):
		if predict[i]>Y_train1[i]:
			#print(Y_train1[i])
			Y_down.append(Y_train1[i])
			X_down.append(df.loc[Y_train1[i], 'x_axis'])
		else:
			Y_up.append(Y_train1[i])
			X_up.append(df.loc[Y_train1[i], 'x_axis'])
	data1 = {"x_axis": X_up, "y_axis": Y_up}
	newdf1 = pd.DataFrame(data1, columns = ["x_axis", "y_axis"])
	data2 = {"x_axis": X_down, "y_axis": Y_down}
	newdf2 = pd.DataFrame(data2, columns = ["x_axis", "y_axis"])
	#base case
	if number==1:
		#print("yes")
		plt.plot(X_train, predict, label = 'LR')
		return predict
	ans = []
	ans.append(recursiveLR(newdf1, number-1))
	ans.append(recursiveLR(newdf2, number-1))
	return ans

dataset_copy = dataset.copy()
l = recursiveLR(dataset_copy, 3)
X_train = dataset.iloc[:,0]
Y_train = dataset.iloc[:,1]
plt.scatter(X_train, Y_train, label="Test_data", color='c')
plt.legend()
plt.show()