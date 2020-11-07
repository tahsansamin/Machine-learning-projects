import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression


satisfaction_level = input('pls enter employee satisfaction based on a scale of 0.00 to 1.00: ')
last_evalutation = input('pls enter last evalutation on a scale of 0.00 to 1.00: ')
numberofprojects = input('enter the number of projects they did: ')
average_monthly_hours = input('his or her average monthly hours: ')
department = input('which department: ')
salary = input('what was their salary low medium or high: ')
#making encoders
le_department = LabelEncoder()
le_salary = LabelEncoder()





df = pd.read_csv('HR_comma_sep.csv')
target = df[['left']]



#dropping unnecessary column variables
inputs = df.drop(['left','promotion_last_5years','Work_accident'],axis='columns')

#transforming the word variables into numbers
inputs['department_n'] = le_department.fit_transform(inputs['Department'])
inputs['salary_n'] = le_department.fit_transform(inputs['salary'])

#dropping the inputs with words
new_inputs = inputs.drop(['Department','salary'],axis='columns')

#transforming the inputs of  department and salary into numbers
new_department = le_department.fit_transform([department])
new_salary = le_department.fit_transform([salary])

#user input list
lst = [[satisfaction_level,last_evalutation,numberofprojects,average_monthly_hours,department,salary]]


#splitting the data
X_train, X_test, y_train, y_test = train_test_split(new_inputs[['satisfaction_level','last_evaluation','number_project','average_montly_hours','department_n','salary_n']],df.left,train_size=0.9)

model = LogisticRegression(solver='lbfgs')
model.fit(X_train,y_train)

print(model.predict([[satisfaction_level,last_evalutation,numberofprojects,average_monthly_hours,new_department,new_salary]]))













