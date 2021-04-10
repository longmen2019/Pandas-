#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('subset_census-income_data.csv')


# In[3]:


print(df)


# In[8]:


print(df.to_string())


# In[5]:


print(df.info())


# In[6]:


x = df["age"].mean()
print(x)


# In[7]:





# In[10]:


y = df["age"].median()


# In[11]:


print(y)


# In[12]:


z = df["age"].mode()


# In[13]:


print(z)


# In[ ]:




