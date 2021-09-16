# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 17:58:40 2021

@author: Atrey
"""

#import necessary libraries for data wrangling
import pandas as pd


#Import model saver
import pickle 

#import machine learning libraries and modules
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

#Read file
fire_nrt_2_viirs = pd.read_csv(r'C:\Users\Atrey\Documents\fire_nrt_V1_96617.csv')

#Get features
X_nrt = fire_nrt_2_viirs[['latitude','longitude','bright_ti4','scan','track', 'bright_ti5', 'frp']]

#Get target
y_nrt = fire_nrt_2_viirs[['confidence']]

#Split data
X_train_nrt, X_test_nrt, y_train_nrt, y_test_nrt = train_test_split(X_nrt, y_nrt, test_size=0.33, random_state=42)

#Initialize decision tree and parameters 
dt_nrt = DecisionTreeClassifier(max_depth = 10, min_samples_split = 20)

#Perform grid search to find best parameters 
gs_nrt = GridSearchCV(dt_nrt,
                  param_grid = {'max_depth': range(1, 20),
                                'min_samples_split': range(10, 40, 10)},
                  n_jobs=1,
                  scoring='accuracy', verbose = 10)

#Find optimal tuned parameters 
gs_nrt.fit(X_train_nrt, y_train_nrt)

#fit decision tree model
dt_nrt.fit(X_train_nrt, y_train_nrt)

#Save model 
pickle.dump(dt_nrt, open('model.pkl', 'wb'))