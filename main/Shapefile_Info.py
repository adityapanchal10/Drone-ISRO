#!/usr/bin/env python
# coding: utf-8

# In[1]:


import shapefile
import matplotlib.pyplot as plt


# In[2]:


sf = shapefile.Reader("railways.shp")


# In[3]:


sf.shapeType


# In[4]:


len(sf)


# In[5]:


shapes = sf.shapes()


# In[6]:


len(shapes)


# In[7]:


sf.shape(6)


# In[8]:


sf.shape(6).shapeTypeName


# In[9]:


sf.fields


# In[10]:


sf.records()


# In[11]:


sf.shapeRecords()
Xcor = []
Ycor = []


# In[ ]:





# In[12]:


plt.figure()
for shape in sf.shapeRecords():
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    plt.plot(x,y)
plt.show()


# In[ ]:





# In[18]:


for shape in sf.shapeRecords():
     poly = shape.shape.__geo_interface__
     print(poly)