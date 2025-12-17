import matplotlib .pyplot as plt
import numpy as np

student_names=["ali","usman","omer","ahsan","hassan","ahmed","saad","fahad"]
student_marks=[35,50,20,25,35,45,60,75]
mark_perc=[] 
for i in student_marks:
    mark_perc.append(i/100*100)

print(mark_perc)

def line_chart__of_marks():
    plt.plot(student_names,mark_perc)
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.title("Marks of Students")
    plt.show()

line_chart__of_marks()

def per_bar_chart():
    plt.bar(student_names,mark_perc)
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.title("Marks of Students")
    plt.show()
