import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

df = pd.read_csv('cancer data.csv')
inputs = df.drop(['name','cancer_results'],axis='columns')
target = df['cancer_results']

le_cholestrol = LabelEncoder()
le_gender = LabelEncoder()
le_over40 = LabelEncoder()

inputs['cholestrol_n'] = le_cholestrol.fit_transform(inputs['cholestrol'])
inputs['gender_n'] = le_gender.fit_transform(inputs['gender'])
inputs['over40_n'] = le_over40.fit_transform(inputs['over_40'])

inputs_n = inputs.drop(['cholestrol','gender','over_40'],axis='columns')

t = inputs_n.head()
print(t)

model = tree.DecisionTreeClassifier()
model.fit(inputs_n,target)

f = model.predict([[0,1,1]])
print(f)

