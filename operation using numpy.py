import numpy as np  
matrix_a=np.arange(9,dtype=float).reshape(3,3)  
print("Matrix A: ",matrix_a)
array_b=np.array([10,10,10])
print("Array B: ",array_b)

print("Addition of two matrices: ")  
print(np.add(matrix_a,array_b))
print("Subtraction of two matrices: ")  
print(np.subtract(matrix_a,array_b)  )
print("Multiplication of two matrices: ")  
print(np.multiply(matrix_a,array_b))  
print("Division of two matrices: ")  
print(np.divide(matrix_a,array_b))  
