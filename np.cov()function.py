# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 16:20:00 2021

@author: User
"""

#Python code to demonstrate the use of numpy.cov
import numpy as np

x = np.array([[0,3,4] , [1,2,4] , [3,4,5]])
print("Shape of array:\n" , np.shape(x))
print("Covariance matrix of x:\n" , np.cov(x))

#Python code to demonstrate the use of numpy.cov
import numpy as np

x = [1.23 , 2.12 , 3.34, 4.5]

y = [2.56 , 2.89 , 3.76 , 3.95]

#find out covariance with respect columns 
cov_mat = np.stack((x,y) , axis = 0)

print(np.cov(cov_mat))

#Python code to demonstrate the use of numpy.cov

import numpy as np
x = [1.23 , 2.12 , 3.34, 4.5]
y = [2.56 , 2.89 , 3.76 , 3.95]

#find out covariance with respect rows
cov_mat = np.stack((x,y) , axis = 1)
print("Shape of matrix x and y:" , np.shape(cov_mat))
print("Shape of covariance matrix:" , np.shape(np.cov(cov_mat)))
print(np.cov(cov_mat))