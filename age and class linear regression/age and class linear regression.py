import numpy as np
import pandas as pd
import pylab as pl
from sklearn import linear_model
import matplotlib.pyplot as plt

file = pd.read_csv('age and class cs version.csv')





regr = linear_model.LinearRegression()
regr.fit(file[['Age ']],file.Class)

rt = input('Enter the age you want to calculate the class of: ')
print(regr.predict([[rt]]))
