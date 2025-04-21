#!/usr/bin/env python
# coding: utf-8

# # Task : 1

# Perform Data Cleaning
# 
# Clean a dataset by removing missing values
# and outliers.

# In[1]:


import pandas as pd


# In[3]:


#Load the dataset
df = pd.read_csv(r"C:\Users\afsir\Downloads\gender_submission.csv")
df


# In[6]:


#Checking missing values
df.isnull().sum()


# There is no missing values in this dataset.

# In[18]:


df["Survived"].value_counts()


# The dataset contains two columns:
# 
# PassengerId: Unique identifier for each passenger.
# 
# Survived: Indicates survival status (1 = Survived, 0 = Did not survive)

# In[23]:


# Searching for outliers in PassengerId column
Q1 = df["PassengerId"].quantile(0.25)
Q3 = df["PassengerId"].quantile(0.75)

IQR = Q3 - Q1
IQR


# In[24]:


# Define Lower and upper limits
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

# Find Outliers
outliers = df[(df["PassengerId"] < lower_limit) | (df["PassengerId"] > upper_limit)]
outliers


# ## Task 1: Data Cleaning Summary
# 
# ### Missing Values: No missing values found.
# 
# ### Outliers in Survived: All values are valid (only 0 and 1), so no outliers were found.
# 
# ## Final Cleaned Dataset: Ready for analysis.
