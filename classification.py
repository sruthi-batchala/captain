import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
%matplotlib inline

data=pd.read_csv('https://raw.githubusercontent.com/sruthi-batchala/ai/master/mnist_test.csv')

df_x=data.iloc[:,1:]
df_y=data.iloc[:,0]

x_train,x_test, y_train, y_test=train_test_split(df_x, df_y, test_size = 0.2, random_state=4)

rf=RandomForestClassifier(n_estimators=100)

rf.fit(x_train, y_train)

pred=rf.predict(x_test)

s=y_test.values

count=0
for i in range(len(pred)):
    if pred[i]==s[i]:
        count=count+1
print(count)#prints the count 
print(len(pred))#prints the length of te predicted array of values
print(count/(len(pred)))#estimates the accuracy


# output

1900 # count
2000 #len(pred)
0.95 #accuracy
