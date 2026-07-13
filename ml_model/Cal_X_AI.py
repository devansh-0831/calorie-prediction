
import pandas as pd # working with data(data cleaning,reading,loading)
import matplotlib.pyplot as plt  # graphs
from sklearn.preprocessing import LabelEncoder
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score  
from sklearn.pipeline import Pipeline

#reading the file
CalX_AI_data_frame=pd.read_csv('ml_model/calories_data.csv')


#to count the null values
CalX_AI_data_frame.isnull().sum()

#remove null rows
CalX_AI_data_frame.dropna(inplace=True)

# #finding outliers
# graphs=CalX_AI_data_frame.columns
# for i in graphs:
#     sns.boxplot(CalX_AI_data_frame[i]) 
#     plt.show()
  
# #histplot kde for matrix
# for i in graphs:
#     sns.histplot(CalX_AI_data_frame[i],kde=True) 
#     plt.show()

# dividing featurea and target column
X_Cal=CalX_AI_data_frame.drop(['calories_needed'], axis=1)
Y_Cal=CalX_AI_data_frame['calories_needed']

#object for encoding
le1 = LabelEncoder()
le2 = LabelEncoder()
le3 = LabelEncoder()

#encoding
X_Cal['gender']=le1.fit_transform(X_Cal['gender'])
X_Cal['activity_level']=le2.fit_transform(X_Cal['activity_level'])
X_Cal['purpose']=le3.fit_transform(X_Cal['purpose'])

#savibg objects
joblib.dump(le1,'gender_enocode.joblib')
joblib.dump(le2,'activity_level_encoder.joblib')
joblib.dump(le3,'purpose_enocode.joblib')

#checking correlation
corr = X_Cal.corrwith(Y_Cal)

#droping unwanted columns
X_Cal.drop(['bmi_category_numeric','bmi_squared','fat_mass_kg','age_squared',
            'metabolic_age_factor','lean_mass_percentage','age_group',
            'activity_numeric','purpose_numeric','height_m'],axis=1,inplace=True)

#scalling
ss1=StandardScaler()
X_Cal = ss1.fit_transform(X_Cal)

#saving scaling
joblib.dump(ss1, 'scaler.joblib')

#spilting data
X_train, X_test, Y_train, Y_test = train_test_split(X_Cal, Y_Cal, test_size=0.2, random_state=42)

#training
model=RandomForestRegressor()
model.fit(X_train, Y_train)

#saving model
joblib.dump(model, 'calorie_model.joblib')

#prediction on unseen data
Y_prediction=model.predict(X_test)

#r2 score
r2_score=r2_score(Y_test,Y_prediction) 

pipeline_a = Pipeline([('standard_scaler',StandardScaler()),('model',RandomForestRegressor())])

pipeline_a.fit(X_Cal,Y_Cal)
joblib.dump(pipeline_a,'pipeline_a.joblib')       













