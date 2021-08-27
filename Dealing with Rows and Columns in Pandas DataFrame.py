#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import pandas package
import pandas as pd


# In[2]:


# Define a dictionary containing employee data
data = {
'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']
    
}


# In[3]:


# Convert the dictionary into DataFrame
df = pd.DataFrame(data)


# In[4]:


# Select two frames
print(df[["Name" , "Qualification"]])


# In[5]:


# import pandas package
import pandas as pd


# In[6]:


# Define a dictionary containing students data
data =  {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}


# In[8]:


# Convert the dictionary into DataFrame
df = pd.DataFrame(data)


# In[9]:


df


# In[10]:


# Declare a list that is to be converted into a column
address = ['Delhi' , 'Bangalore' , 'Chennai' , 'Patna']


# In[11]:


# Using 'Address' as the column name
# and equating it to the list
df['Address'] = address


# In[12]:


print(df)


# In[13]:


# importing pandas module
import pandas as pd


# In[14]:


# making data frame from csv file
data = pd.read_csv("nba.csv" , index_col="Name")


# In[15]:


data


# In[16]:


data.drop(["Team" , 'Weight'], axis = 1 , inplace = True)


# In[17]:


data


# In[18]:


# import pandas package 
import pandas as pd
# making data frame from csv file
data = pd.read_csv("nba.csv", index_col = "Name")


# In[19]:


first = data.loc["Avery Bradley"]
second = data.loc["Jonas Jerebko"]


# In[22]:


print(first, '\n\n' , second)


# In[25]:


first = data.iloc[2]


# In[27]:


first


# In[28]:


# importing pandas module
import pandas as pd
# making data frame
df = pd.read_csv('nba.csv' , index_col = 'Name')
df.head(10)


# In[40]:


new_row = pd.DataFrame({'Name':'Geeks', 'Team':'Boston', 'Number':3,
                        'Position':'PG', 'Age':33, 'Height':'6-2',
                        'Weight':189, 'College':'MIT', 'Salary':99999}, index =[0])


# In[41]:


#simply concatenate both dataframe
df = pd.concat([new_row, df]).reset_index(drop=True)


# In[42]:


df.head()


# In[44]:


#importing pandas module 
import pandas as  pd 
# making data frame from csv file 
data = pd.read_csv("nba.csv" , index_col="Name")
# dropping passed values 
data.drop(["Avery Bradley" , "John Holland" , "R.J. Hunter" , "R.J. Hunter" ], inplace = True)


# In[45]:


data


# In[ ]:




