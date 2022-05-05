#!/usr/bin/env python
# coding: utf-8

# Homework #5. Exploratory Data Analysis

# Author: Вікторія Шютева

# Total time spent on h/w (in minutes): 

# In[1]:


import pandas as pd


# In[2]:


DIALOGS_MERGED_DATA_PATH = "/Users/vikavika/PycharmProjects/pythonProject1/data/merged_data/dialogs_data_all.csv"
DIALOGS_META_MERGED_DATA_PATH = "/Users/vikavika/PycharmProjects/pythonProject1/data/merged_data/dialogs_users_all.csv"


# In[3]:


df = pd.read_csv(DIALOGS_MERGED_DATA_PATH)
df_meta = pd.read_csv(DIALOGS_META_MERGED_DATA_PATH)


# 1. How many dialogs with real people do I have?

# In[17]:


df_meta.groupby(["dialog_id"]).count().shape[0]


# 2. How many users I have connection with? (in all chats)

# In[10]:


df_meta.users.count()


# 3. Types of all my messages. Visualization

# In[24]:


df.groupby(["type"])["type"].count()


# ![viz1.jpg](attachment:viz1.jpg)

# 4. Average duration of video/audio

# In[28]:


df["duration"].mean()


# In[ ]:




