#!/usr/bin/env python
# coding: utf-8

# # Task : 3

# Visualization using Histogram
# 
# Create a histogram or bar chart to visualize
# the distribution of data in a dataset

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


# Load the dataset
iris = pd.read_csv(r"C:\Users\afsir\Downloads\iris.csv")
iris


# In[4]:


#Checking missing values
iris.isnull().sum()


# There is no missing values in this dataset.

# In[5]:


iris["Species"].value_counts()


# There is only three types of Species.
# 
# 1. Iris-setosa
# 2. Iris-versicolor
# 3. Iris-virginica

# In[6]:


# The distribution of the Species

sns.countplot(x = "Species", data = iris, palette = "pastel")
plt.title("Count of Each Iris Species")
plt.xlabel("Species")
plt.ylabel("Count")
plt.show()


# All the Species are equally distributed.

# In[7]:


# Plot histogram for all numeric columns

iris.hist(figsize=(10,8), bins = 15, color = "skyblue", edgecolor = "black")
plt.suptitle("Distribution of Iris Dataset Features", fontsize = 16)
plt.tight_layout()
plt.show()


# These histograms revealed the frequency distribution of each feature, helping to understand how values are spread across the dataset. For instance:
# 
# Petal length and width showed clear separation patterns among species.
# 
# Sepal length values were more normally distributed, while sepal width showed a wider spread.

# In[ ]:




