#Boolean
a=True
if(a==True):
    print("I am Abhijeet")

#defining multiplication..   

def Multiplication(a,b):
    return a*b

print(Multiplication(2,3))

#array multiplication
'''
import numpy as np

def arrayMultiply(a.b):
    c=np.array()
    for(i in range(len(a))):
        c.append(a[i]*b[i])
    
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

c = np.multiply(a, b)

print(c)
'''
'''
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.multiply(a, b)

print(c)

'''

import numpy as np

def multiply_arrays(array1, array2):
  # check if the arrays have the same length
  if len(array1) != len(array2):
    # raise an exception if they don't
    raise ValueError("The arrays must have the same length")
  # create an empty list to store the result
  result = []
  # loop through the elements of the arrays
  for i in range(len(array1)):
    # multiply the corresponding elements and append to the result list
    result.append(array1[i] * array2[i])
  # return the result list as a numpy array
  return np.array(result)

array1 = [1, 2, 3]
array2 = [4, 5, 6]

# call the function and print the result
print(multiply_arrays(array1, array2))
