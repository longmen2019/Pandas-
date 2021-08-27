#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing pandas package
import pandas as pd
# making data frame from csv file
data = pd.read_csv("nba.csv")


# In[2]:


data


# In[4]:


# retrieving row by loc[] method
row1 = data.loc[3]


# In[6]:


# retrieving row by iloc[] method
row2 = data.iloc[3]

row1==row2
# In[8]:


# importing pandas package
import pandas as pd


# In[9]:


# <!-- making data frame from csv file -->
data = pd.read_csv("nba.csv")
data


# In[10]:


# retrieving rows by loc method
row1 = data.iloc[[4,5,6,7]]


# In[11]:


# retrieving rows by loc[] method
row2 = data.iloc[4:8]


# In[12]:


row1==row2


# In[ ]:




