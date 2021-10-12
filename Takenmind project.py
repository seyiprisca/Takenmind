#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter


# In[25]:


data =  r'\Users\HP\Downloads\TakenMind-Python-Analytics-Problem-case-study-1-1.xlsx'
data_1 = pd.read_excel(data, sheet_name='Existing employees')
print(data_1.describe())


# In[12]:


data_2 = pd.read_excel(data, sheet_name='Employees who have left')
print(data_2.describe())


# In[13]:


print(data_1.isnull().sum())


# In[14]:


print(data_2.isnull().sum())


# In[22]:


#job satisfaction greater than 60%
jobsat=data_1[data_1["satisfaction_level"]>0.6]
print(len(jobsat))
print(((len(data_1)-len(jobsat))/len(data_1))*100,"% People are less than 60% satisfied by their job")
print(jobsat["satisfaction_level"].mean(), "average of satisfaction level")


# In[24]:


#people who have left the job and their satisfaction
jobsat_2=data_2[data_2["satisfaction_level"]>0.6]
print(len(jobsat_2))
print(len(data_2))
print(((len(data_2)-len(jobsat_2))/len(data_2))*100,"% People have left job when less than 60% satisfied by job")


# In[27]:


#evaluation of scores
valuate =data_1[data_1["last_evaluation"]>0.5]
print(((len(data_1)-len(valuate))/len(data_1))*100,"% People scored less than 50%")


# In[29]:


#evaluation of scores for thodse who have left the job
val=data_2[data_2["last_evaluation"]>0.5]
print(len(val))
print(len(data_2))
#people left the job despite the fact that they scored good in their evaluation
print(((len(data_2)-len(val))/len(data_2))*100,"% left job whose score where less than 50%")


# In[30]:


#salary count for existing employees
count =Counter(list(data_1["salary"]))
print(count)
#salary count for employees who have left
c_count=Counter(list(data_2["salary"]))
print(c_count)


# In[31]:


#counting employees that got promoted i the last 5 years
promoted =data_1[data_1["promotion_last_5years"]==1]
print(len(promoted),"employee got promotion")
#promotio cout for employees who have left
c_promoted=data_2[data_2["promotion_last_5years"]==1]
print(len(c_promoted),"employee got promotion")


# In[32]:


#average monthly hours spent
hrs=data_2["average_montly_hours"]
print(hrs.mean())
#average hours for existing employees
d=data_1[data_1["average_montly_hours"]>207]
print(len(d))
dd=data_2[data_2["average_montly_hours"]>207]
print(len(dd))


# In[34]:


#time spent at the company
t1=data_2["time_spend_company"]
print(t1.mean())
print(t1.median())
t2=data_1[data_1["time_spend_company"]>4]
print(len(data_2[data_2["time_spend_company"]>4]))
print(len(t2))


# In[35]:


plt.figure(figsize=(16,12))
sns.countplot(data_2["last_evaluation"])
plt.show()


# In[36]:


from sklearn import preprocessing
p = preprocessing.LabelEncoder()
data_1["result"]=0
data_2["result"]=1
s_data=data_1.append(data_2)
s_data


# In[39]:


p.fit(data_1["salary"])
data_1["salary"]=p.transform(data_1["salary"])
p.fit(data_1["dept"])
data_1["dept"]=p.transform(data_1["dept"])
a=data_1.corr()
plt.figure(figsize=(16,12))
sns.heatmap(a,cmap="winter",annot=True)
plt.show()


# In[41]:


s_data
s_d1=data_1[data_1["dept"]==7]
s_d1=s_d1[s_d1["salary"]==1]
s_d1


# In[42]:


data_1.groupby(["dept"])["salary"].value_counts().plot()
plt.show()


# In[ ]:




