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


# In[13]:


# importing pandas package
import pandas as pd


# In[14]:


# making data frame from csv file
data = pd.read_csv("nba.csv" , index_col="Name")


# In[15]:


data.head()


# In[19]:


# retrieving columns by indexing operator
first = data["Age"]


# In[20]:


first


# In[21]:


# importing pandas package
import pandas as pd
# making data frame from csv file
data = pd.read_csv("nba.csv", index_col="Name")


# In[25]:


# retrieving multiple columns by indexing operator
first = data[["Age" , "College" , "Salary"]]


# In[23]:


first


# In[26]:


# importing pandas package 
import pandas as pd
# making data frame from csv file
data = pd.read_csv("nba.csv" , index_col = "Name")


# In[27]:


data.head()


# In[28]:


# retrieving row by loc[] method
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]


# In[29]:


print(first,"\n\n\n",second)


# In[30]:


import pandas as pd
# making data frame from csv file
data = pd.read_csv("nba.csv" , index_col = "Name")


# In[31]:


data.head()


# In[32]:


# retrieving multiple rows by loc method
first = data.loc[["Avery Bradley" , "R.J. Hunter"]]


# In[33]:


first


# In[35]:


import pandas as pd
# making data frame from csv file 
data = pd.read_csv("nba.csv" , index_col = "Name")
# retrieving two rows and three colums by loc method
first = data.loc[["Avery Bradley" , "R.J. Hunter"] , ["Team" , "Number" , "Position"]]


# In[36]:


first


# In[37]:


import pandas as pd


# In[38]:


# making data frame from csv file
data = pd.read_csv("nba.csv" , index_col = "Name")


# In[40]:


# retrieving all rows and some columns by loc method 
first = data.loc[: , ["Team" , "Number" , "Position"]]


# In[41]:


first


# In[42]:


import pandas as pd
data =pd.read_csv("nba.csv" , index_col="Name")


# In[43]:


#retrieving rows by iloc method
row2 = data.iloc[3]


# In[44]:


row2


# In[45]:


frow2= data.iloc[[3,5,7]]


# In[46]:


frow2


# In[47]:


import pandas as pd
# making data frame from csv file
data =pd.read_csv("nba.csv" , index_col = "Name")
# retrieving multiple rows by iloc method
row2 = data.iloc[[3,5,7]]


# In[48]:


row2


# In[49]:


import pandas as pd
# making dataframe from csv file
data =pd.read_csv("nba.csv" , index_col = "Name")
# retrieving two rows and two columns by iloc method
row2 = data.iloc[[3,4] , [1,2]]


# In[50]:


row2


# In[51]:


import pandas as pd
# making data frame from csv file
data = pd.read_csv("nba.csv" , index_col = "Name")


# In[56]:


# retrieving all rows and some columns by iloc method
row2 = data.iloc[: , [1,2]]


# In[57]:


row2


# In[ ]:




