#!/usr/bin/env python
# coding: utf-8

# In[29]:


import numpy as np
from sklearn.model_selection import train_test_split
from scipy.io import arff
import pandas as pd

df = pd.read_csv("Week2_Problem2.csv")

df = df.apply(lambda x: x.astype(str).str.lower())

df = df.replace('geo', 0)
df = df.replace('leo', 1)
df = df.replace('meo', 10)


df.head(200)


# In[31]:


xVar = list(['Class of Orbit'])


# In[ ]:




