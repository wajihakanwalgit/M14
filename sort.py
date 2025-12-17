import numpy as np

data_type=[("name","S15"),("class",int),("height",float)]
student_details=[("james",5,48.5),("kate",3,38.5),("lucy",2,32.5),("jim",4,42.5),("tom",1,36.5)]
student=np.array(student_details,dtype=data_type)
print(student)
print("sorting by name")
print(np.sort(student,order="name"))
print("sorting by class")
print(np.sort(student,order="class"))
print("sorting by height")
print(np.sort(student,order="height"))
