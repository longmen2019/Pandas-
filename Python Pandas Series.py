#!/usr/bin/env python
# coding: utf-8

# In[1]:


https://www.geeksforgeeks.org/python-pandas-series/?ref=lbp
import pandas as pd


# In[2]:


import numpy as np


# In[3]:


data = np.array(['g','e','e','k','s'])


# In[4]:


ser =pd.Series(data)


# In[5]:


print(ser)


# In[6]:


import pandas as pd


# In[7]:


list = ['g' , 'e' , 'e' , 'k' , 's']


# In[8]:


ser = pd.Series(list)


# In[9]:


ser


# In[10]:


#import pandas as numpy
import pandas as pd
import numpy as np

data = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
ser = pd.Series(data)


# In[11]:


ser[:5]


# In[12]:


import pandas as pd
import numpy as np


# In[13]:


data = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
ser = pd.Series(data, index = [10,11,12,13,14,15,16,17,18,19,20,21,22])


# In[14]:


ser[16]


# In[16]:


import pandas as pd


# In[17]:


df = pd.read_csv("nba.csv")


# In[18]:


ser = pd.Series(df["Name"])


# In[19]:


data = ser.head(10)


# In[20]:


data


# In[21]:


data[3:6]


# In[22]:


# importing pandas as module
import pandas as pd
# making data frame
df = pd.read_csv("nba.csv")


# In[23]:


df


# In[24]:


ser = pd.Series(df["Name"])


# In[25]:


ser


# In[26]:


data = ser.head(10)


# In[27]:


data


# In[29]:


# using .loc[] function
data.loc[3:6]


# In[30]:


# importing pandas module
import pandas as pd
df = pd.read_csv("nba.csv")


# In[31]:


ser = pd.Series(df["Name"])


# In[32]:


data = ser.head(10)


# In[33]:


data


# In[35]:


# using iloc[] function
data.iloc[3:6]


# In[36]:


#import pandas module
import pandas as pd


# In[37]:


# creating a series
data = pd.Series([5,2,3,7] , index = ['a' , 'b' , 'c' , 'd'])


# In[38]:


# creating a series
data1 = pd.Series([1,6,4,9] , index = ['a' , 'b' , 'd' , 'e'])


# In[39]:


print(data, "/n/n" , data1)


# In[41]:


# adding two series using .add() function
# .add
data.add(data1 , fill_value=0)


# In[45]:


data.add(data1 , fill_value=0)


# In[46]:


# imporint pandas as module
import pandas as pd 
# creating a series
data = pd.Series([5,2,3,7] , index = ['a', ' b' , 'c' , 'd'])
data1 = pd.Series([1,6,4,9] , index = ['a' , 'b' , 'c' , 'e'])
print(data , '\n\n' , data1)


# In[48]:


# subtracting two series using 
# .sub
data.sub(data1 , fill_value=0)


# In[49]:


# python program using astype
# to convert a data type of series

import pandas as pd
data = pd.read_csv("nba.csv")


# In[50]:


# dropping null value to avoid error
data.dropna(inplace = True)


# In[51]:


# storing dtype before converting
before =data.dtypes


# In[52]:


before


# In[55]:


# converting dtypes using astype
data["Salary"] = data["Salary"].astype(int)
data["Number"] = data["Number"].astype(str)


# In[56]:


# storing dtype after converting
after = data.dtypes


# In[57]:


print(before)


# In[58]:


print(after)


# In[59]:


# # python program using astype
# to convert a datatype of series
# importing pandas module
import pandas as pd
# reading csv file from url
data = pd.read_csv("nba.csv")


# In[60]:


# dropping null value columns to avoid errors
data.dropna(inplace = True)


# In[61]:


# storing dtype before converting
before = data.dtypes


# In[62]:


# converting dtypes using astype
data["Salary"] = data["Salary"].astype(int)
data["Number"] = data["Number"].astype(str)


# In[63]:


after = data.astype


# In[64]:


# printing to compare
print("BEFORE CONVERSION\n" , before, "\n")
print("AFTER CONVERSION\n", after , "\n")


# In[69]:


# Python program converting
# a series into list
# importing regex module
import pandas as pd
# importing regex module
import re
# making data frame
data = pd.read_csv("nba.csv")
#removing null values to avoid errors
data.dropna(inplace = True)
# storing dtype before operation
dtype_before= type(data["Salary"])
# converting to list
salary_list = data["Salary"].tolist()
#storing dtype after after operation
dtype_after = type(salary_list)


# In[72]:


#printing dtype
print("Data type before converting = {}\nData type after converting = {}".format(dtype_before, dtype_after))


# In[73]:


salary_list


# In[ ]:




