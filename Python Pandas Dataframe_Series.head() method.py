#!/usr/bin/env python
# coding: utf-8

# In[1]:


# https://www.geeksforgeeks.org/python-pandas-dataframe-series-head-method/?ref=lbp
# importing pandas module
import pandas as pd


# In[2]:


# making data frame
data = pd.read_csv("nba.csv")
# calling head() method
# storing in new variable
data_top = data.head()


# In[3]:


data_top


# In[4]:


# importing pandas module
import pandas as pd


# In[5]:


#making data frame
data = pd.read_csv("nba.csv")


# In[6]:


#number of rows to return
n = 9


# In[7]:


#creating series
Series = data["Name"]


# In[8]:


Series


# In[11]:


# returning top n rows
top = Series.head(n=n)


# In[12]:


top


# In[ ]:




