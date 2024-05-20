#!/usr/bin/env python
# coding: utf-8

# # Import Libriries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Load Data

# In[4]:


df =pd.read_csv("Salary Data.csv")


# In[5]:


df.sample(2)


# # Data Pre-processing

# In[6]:


df.info()


# In[7]:


df.isna().sum()


# In[8]:


df.dropna(inplace=True)


# In[9]:


df.isna().sum()


# In[10]:


df.duplicated().sum()


# In[11]:


df.drop_duplicates(inplace=True)


# In[12]:


df.duplicated().sum()


# In[13]:


df.describe()


# In[14]:


df.head()


# # Data Exploratory

# In[15]:


df['Gender'].value_counts()


# In[16]:


plt.figure(figsize=(10,8))
sns.countplot(data=df, x='Gender',palette='pink')
plt.title("Male VS Female")
plt.show()          


# In[17]:


df['Job Title'].value_counts()


# In[18]:


top_jobs= df['Job Title'].value_counts().head(10)
plt.figure(figsize=(15,8))
plt.xticks(rotation=90)
sns.barplot(data=df, x=top_jobs.index,y=top_jobs.values,palette='plasma')
plt.title("Top 10 Jobs")
plt.xlabel('Jobs')
plt.ylabel('Count')
plt.show()   


# In[19]:


df.sample(2)


# In[20]:


sal= df.groupby('Job Title')['Salary'].sum()


# In[21]:


sal


# In[22]:


tob_salary = sal.sort_values(ascending=False).head(10)


# In[23]:


tob_salary


# In[24]:


plt.figure(figsize=(15,8))
plt.xticks(rotation=90)
sns.barplot(data=df, x=tob_salary.index,y=tob_salary.values,palette='plasma')
plt.title("Top 10 Salary in Jobs")
plt.xlabel('Jobs')
plt.ylabel('Sum')
plt.show()  


# In[25]:


df['Years of Experience'].value_counts()


# In[26]:


Experience=df.groupby('Years of Experience')['Salary'].sum()
Experience


# In[27]:


Experience.sort_values(ascending=False).head(10)


# In[28]:


plt.figure(figsize=(15,8))
# plt.xticks(rotation=90)
sns.barplot(data=df, x=Experience.index,y=Experience.values,palette='plasma')
plt.title("Top 10 Salary With Years of Experience")
plt.xlabel('Years of Experience')
plt.ylabel('Sum of Salary')
plt.show() 


# In[29]:


df.sample(3)


# In[30]:


Balance = df.groupby('Gender')['Salary'].sum()
Balance


# In[31]:


plt.figure(figsize=(15,8))
# plt.xticks(rotation=90)
sns.barplot(data=df, x=Balance.index,y=Balance.values,palette='plasma')
plt.title("Salary Male VS Female")
plt.xlabel('Type')
plt.ylabel('Sum of Salary')
plt.show() 


# # Thanks!

# In[ ]:




