#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing pandas as pd
import pandas as pd
# importing regex module
import re
# making data frame
data = pd.read_csv("nba.csv")


# In[2]:


# removing null values to avoid errors
data.dropna(inplace = True)


# In[3]:


# percentile list
perc = [.20, .40 , .60 , .80]
# list of dtypes to include
include = ["object" , "float" , "int"]


# In[4]:


# calling describe method
desc = data.describe(percentiles = perc, include = include)
desc


# In[5]:


# importing pandas module
import pandas as pd


# In[6]:


# importing regex module
import re


# In[7]:


# making data frame
data = pd.read_csv("nba.csv")


# In[8]:


data.dropna(inplace = True)


# In[9]:


desc = data["Name"].describe


# In[10]:


desc


# In[ ]:




