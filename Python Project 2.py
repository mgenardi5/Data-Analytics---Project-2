#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plot
df = pd.read_csv('https://raw.githubusercontent.com/niteen11/DataAnalyticsAcademy/master/Python/dataset_diabetes/diabetic_data.csv')
#Import data set and packages


# In[5]:


df.head()


# In[6]:


df.dtypes
#highlevel review of dataset


# In[7]:


df['readmitted'].unique()
#understand values in desired field for analysis


# In[8]:


df['A1Cresult'].unique()
#understand values in desired field for analysis


# In[9]:


df0 = df.loc[:,['encounter_id','patient_nbr', 'num_medications', 'A1Cresult','readmitted']]
df0
#Keep desired columns


# In[10]:


df1=df0[df0['A1Cresult'] != 'None']
df1
#purpose of analysis is to compare A1C reuslts under various conditions; drop any instances where A1C was not measured


# In[11]:


df1['num_medications'].unique()
#confirming that values beyond 0 are still contained in the dataset
#reveals that there is a wide range of values; could benefit from creating smaller buckets


# In[12]:


df1['num_medications'].describe()
#descriptive stats of measurement field


# In[20]:


sn.boxplot(x="A1Cresult",y="num_medications",data=df1)
df1.groupby('A1Cresult').mean()
#create a boxplot based on A1C result


# In[21]:


sn.boxplot(x="A1Cresult",y="num_medications",hue="readmitted",data=df1)
df1.groupby('readmitted').mean()
#create a boxplot based on A1C result


# In[ ]:


#Conclusion - looking at A1C Result alone, there is little evidence to support that the number of medications a patient takes is correlated to their A1C level. 
#However, factoring in whether or not a patient has been readmitted shows that if a patient with an abnormal A1C result was readmitted within 30 days (so would assume a more severe case),they would consume more scripts on average than a patient with an abnormal A1C result that was either not readmitted or readmitted in greater than 30 days 

