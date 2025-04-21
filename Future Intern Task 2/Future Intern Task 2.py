#!/usr/bin/env python
# coding: utf-8

# # Task : 2

# Calculate summary statistics
# 
# Calculate summary statistics (mean, median,
# mode, standard deviation) for a dataset

# In[1]:


import pandas as pd


# In[2]:


#Load the dataset
df = pd.read_csv(r"C:\Users\afsir\Downloads\gender_submission.csv")
df


# In[3]:


df["Survived"].mean()


# About 36.36% of passengers survived (value = 1), and the rest did not survive (value = 0).

# In[4]:


df["Survived"].mode()


# More than 50% of passengers did not survive, so when sorted, the middle falls on a 0.

# In[5]:


df["Survived"].median()


# The most common outcome is 0 = did not survive.

# In[7]:


df["Survived"].std()


# A standard deviation of 0.482 in the Survived column means that the data has a moderate spread, reflecting the fact that there's a mix of survivors and non-survivors — but more people didn't survive than did.

# # Task 2 : Summary Statistics
# 
# ### The statistics collectively indicate that survival was less common than non-survival in this dataset. These insights are helpful for understanding the overall distribution and can guide further analysis, such as identifying patterns in survival based on gender, age, or class.

# In[ ]:




