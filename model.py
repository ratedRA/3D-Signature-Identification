#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on  june 22 23:16:54 2018

@author: aman, bhanu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("features.csv")


# from sklearn.preprocessing import Imputer
# imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
# imputer = imputer.fit(x[:,1:])
# x[:,1:] = imputer.transform(x[:,1:])

x = dataset.iloc[:,0:3]
y = dataset.iloc[:,3:4]

print(y)

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
LabelEncoder_y = LabelEncoder()
y = LabelEncoder_y.fit_transform(y)
onehotencoder = OneHotEncoder(categorical_features = [0])
y = onehotencoder.fit_transform(y).toarray()

y = y.reshape((1600,1))

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

y_act = y_test
from sklearn.preprocessing import StandardScaler
sc_x =  StandardScaler()
sc_y =  StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.fit_transform(x_test)
#y_test = sc_y.fit_transform(y_test)
#y_train = sc_y.fit_transform(y_train)


from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 1000, random_state = 0)
regressor.fit(x_train, y_train)
#print(y_test)
y_pred = (regressor.predict(x_test))
print(y_pred)
print(y_test)





