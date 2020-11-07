#import the modues
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv('london housing.csv')

plt.scatter(df[['year']],df.price,color='green')


#making and training the model

regr = linear_model.LinearRegression()
regr.fit(df[['year']],df.price)


print(regr.predict([[2080]]))

