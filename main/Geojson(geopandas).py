#!/usr/bin/env python
# coding: utf-8

# In[4]:


import geopandas
import matplotlib.pyplot as plt

df = geopandas.read_file("railways.shp")


# In[5]:


df.plot()


# In[6]:


df2 = df.to_json()


# In[7]:


df2


# In[6]:


import geojsonio
geojsonio.display(df2)


# In[ ]:




