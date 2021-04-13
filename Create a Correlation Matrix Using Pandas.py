# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 17:17:25 2021

@author: User
"""

#Create a DataFrame using Pandas to capture the dataset

import pandas as pd

data = {
        'A': [45, 37 , 42, 35 , 39],
        'B': [38, 31 , 26, 28 , 33],
        'C': [10, 15 , 17, 21 , 12]
        }
df = pd.DataFrame(data, columns = ['A' , 'B' , 'C'])

# Create a correlation matrix using this template 
# df.corr()
corrMatrix = df.corr()
print(df)