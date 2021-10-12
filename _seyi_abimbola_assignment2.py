
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



# In[3]:


data = pd.read_excel(r'\Users\HP\Desktop\dummydata.xlsx')
print(data.head())


# In[8]:


dummy =  r'\Users\HP\Desktop\dummydata.xlsx'
dummy_d = pd.read_excel(dummy, sheet_name='Sheet1')
print(dummy_d.head())


# In[9]:


dummy_d.to_csv('dummy_d.csv')


# In[13]:


dd = pd.read_csv('dummy_d.csv')
print(dd.info())


# In[15]:


dummy =  r'\Users\HP\Desktop\dummydata.xlsx'
dummy_a = pd.read_excel(dummy, sheet_name='Sheet2')
print(dummy_a.head())


# In[16]:


dummy_a.to_csv('dummy_a.csv')
da = pd.read_csv('dummy_a.csv')
print(da.head())


# In[17]:


dummy_b = pd.read_excel(dummy, sheet_name='Sheet3')
print(dummy_b.head())


# In[18]:


dummy_b.to_csv('dummy_b.csv')
db = pd.read_csv('dummy_b.csv')
print(db.tail())


# In[20]:


dummy_c = pd.read_excel(dummy, sheet_name='Sheet5')
print(dummy_c.head())


# In[22]:


dummy_c.to_csv('dummy_c.csv')
dc = pd.read_csv('dummy_c.csv')
print(dc.describe())


# In[23]:


dummy_e = pd.read_excel(dummy, sheet_name='Sheet6')
print(dummy_e.tail())


# In[25]:


dummy_e.to_csv('dummy_e.csv')
de = pd.read_csv('dummy_e.csv')
print(de.head())


# In[26]:


dummy_f = pd.read_excel(dummy, sheet_name='Sheet7')
print(dummy_f.tail())


# In[27]:


dummy_f.to_csv('dummy_f.csv')
df = pd.read_csv('dummy_f.csv')
print(df.tail())


# In[29]:


dummy_g = pd.read_excel(dummy, sheet_name='Sheet8')
print(dummy_g.info())


# In[31]:


dummy_g.to_csv('dummy_g.csv')
dg = pd.read_csv('dummy_g.csv')
print(dg.head())


# In[33]:


dummy_h = pd.read_excel(dummy, sheet_name='Sheet9')
print(dummy_h.describe())


# In[34]:


dummy_h.to_csv('dummy_h.csv')
dh = pd.read_csv('dummy_h.csv')
print(dh.head())


# In[35]:


dummy_i = pd.read_excel(dummy, sheet_name='Sheet10')
print(dummy_i.describe())


# In[36]:


dummy_i.to_csv('dummy_i.csv')
di = pd.read_csv('dummy_i.csv')
print(di.tail())


# In[37]:


dummy_j = pd.read_excel(dummy, sheet_name='Sheet11')
print(dummy_j.describe())


# In[38]:


dummy_j.to_csv('dummy_j.csv')
dj = pd.read_csv('dummy_j.csv')
print(dj.head())

