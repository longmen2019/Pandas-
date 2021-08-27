#!/usr/bin/env python
# coding: utf-8

# In[1]:


# https://www.geeksforgeeks.org/python-pandas-extracting-rows-using-loc/
# importing pandas package
import pandas as pd


# In[2]:


# making data frame from csv files
data = pd.read_csv('nba.csv' , index_col="Name")


# In[3]:


first = data.loc["Avery Bradley"]


# In[4]:


second = data.loc["R.J. Hunter"]


# In[7]:


print(first,"\n\n\n",second)


# In[8]:


# importing pandas package
import pandas as pd


# In[9]:


# making data frame from csv file
data = pd.read_csv("nba.csv" , index_col="Name")


# In[11]:


# retrieving rows by loc method
rows = data.loc[["Avery Bradley" , "R.J. Hunter"]]


# In[14]:


print(type(rows))


# In[15]:


rows


# In[20]:


# importing pandas package 
import pandas as pd
# making dataframe from csv file
data = pd.read_csv("nba.csv" , index_col="Team")
# retrieving row by loc method
rows = data.loc["Utah Jazz"]
# checking data type of rows
print(type(rows))
# display
rows


# In[21]:


# importing pandas package
import pandas as pd
data =pd.read_csv("nba.csv" , index_col="Name")


# In[22]:


#retrieving rows by loc method
rows = data.loc["Avery Bradley":"Isaiah Thomas"]


# In[23]:


print(type(rows))


# In[24]:


rows


# In[ ]:




