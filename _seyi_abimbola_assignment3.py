
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


gapminder = pd.read_csv(r'\Users\HP\Downloads\gapminder-FiveYearData.csv')
print(gapminder.head(3))


# In[4]:


df1 = gapminder[['country', 'year','lifeExp']]
print(df1.tail())


# In[5]:


heatmap1_data = pd.pivot_table(df1, values='lifeExp', 
                     index=['country'], 
                     columns='year')


# In[6]:


sns.heatmap(heatmap1_data, cmap="YlGnBu")

