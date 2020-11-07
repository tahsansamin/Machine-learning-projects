import pandas as pd
#the encoder module helps change the data in the table into numbers since ml doesnt understand words
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

#opening data
df = pd.read_csv('google job data.csv')

#dropping the target column
inputs = df.drop('salary_more_than_100k', axis='columns')
target = df['salary_more_than_100k']


le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()

#adding columns with only numbers to the input table
inputs['company_n'] = le_company.fit_transform(inputs['company'])
inputs['job_n'] = le_company.fit_transform(inputs['job'])
inputs['degree_n'] = le_company.fit_transform(inputs['degree '])

#dropping the columns with words
inputs_n = inputs.drop(['company','job','degree '],axis='columns')



model = tree.DecisionTreeClassifier()
model.fit(inputs_n,target)

prediction = model.predict([[2,2,1]])
print(prediction)
