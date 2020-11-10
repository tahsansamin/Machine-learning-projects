import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC

df = pd.read_csv('dog brees csv.csv')

inputs = df.drop(['dog'],axis='columns')
target = df['dog']
le_colour = LabelEncoder()
le_gender = LabelEncoder()

inputs['gender_n'] = le_gender.fit_transform(inputs['sex'])
inputs['colour_n'] = le_colour.fit_transform(inputs['color'])

new_input = inputs.drop(['sex','color'],axis='columns')


X_train, X_test, y_train, y_test = train_test_split(new_input,target,test_size=0.1)


m = SVC(gamma='auto')
m.fit(X_train,y_train)
print(m.predict([[65,120,1,1]]))


