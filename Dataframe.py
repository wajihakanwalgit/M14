import pandas as pd
import numpy as np

exam_data={'name':['Anil','Gaurav','Pankaj','Shivam','Rahul','Saurabh,','Vishal','ali','usman','ajay'],
           "score":[12,18,25,24,19,18,20,15,21,22],
           "attempts":[1,2,2,3,2,3,1,1,2,1],
           "qualify":[True,False,True,True,False,True,True,False,True,True]}
labels=['a','b','c','d','e','f','g','h','i','j']
df=pd.DataFrame(exam_data,index=labels)

print(df.info())


