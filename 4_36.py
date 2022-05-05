#!/usr/bin/env python
# coding: utf-8

# # Homework #3. Crowdsourcing tools review

# Author: Вікторія Шютева

# Total time spent on h/w (in minutes): 270

# In[2]:


import pandas as pd


# In[3]:


DIALOGS_MERGED_DATA_PATH = "/Users/vikavika/PycharmProjects/pythonProject1/data/merged_data/dialogs_data_all.csv"
DIALOGS_META_MERGED_DATA_PATH = "/Users/vikavika/PycharmProjects/pythonProject1/data/merged_data/dialogs_users_all.csv"


# In[4]:


df = pd.read_csv(DIALOGS_MERGED_DATA_PATH)
df_meta = pd.read_csv(DIALOGS_META_MERGED_DATA_PATH)


# Task 2.1
# 
# Messages data analysis

# In[5]:


df.head(10)


# In[6]:


df.shape


# In[7]:


min(df["date"]),max(df["date"])


# In[8]:


df.groupby(["type"])["type"].count()


# In[9]:


df.groupby(["type"])["duration"].sum()


# TASKS TO DO

# 1. Define your telegram ID

# In[15]:


USER_ID = 5005476282


# 2. Check on examples that the data you downloaded reflects your telegram messages. Make screenshots (insert your screenshots in this notebook) of 3 different messages in TG and related rows in your dataset here.

# <img src="1.jpg"/>

# <img src="2.jpg"/>

# 3.Find the longest audio message you've ever sent; what's its duration? Make its screenshot (insert your screenshots in this notebook).

# In[72]:


df2 = df.sort_values('duration', ascending=False)
df2.loc[df2["type"] == "voice"].head(1)


# ![%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-04-18%20%D0%BE%2014.58.54.png](attachment:%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-04-18%20%D0%BE%2014.58.54.png)

# 4. Calculate numbers of send and received(s&r) messages.

# In[32]:


df.shape[0]


# 5. Calculate top-10 people to whom you wrote the biggest amount of messages (name, amount of messages).

# In[31]:


df.to_id.value_counts().head(10)


# 6. Calculate top-10 people who wrote the biggest amount of messages to you (name, amount of messages).

# In[22]:


df.from_id.value_counts().head(10)


# Task 2.2
# 
# Dialogs data analysis

# In[12]:


df_meta.shape


# In[13]:


df_meta.head(10)


# In[14]:


df_meta.groupby(["type"])["type"].count()


# Tasks to do:

# 1. Find our TG group. Print its id and list of participants.

# In[77]:


#-1001787503050
df_meta.loc[df_meta["dialog_id"] == "-1001787503050"]

#не знаю, чому не працює, наче повинно було б


# 2. Calculate top-10 the biggest groups/channels.

# In[41]:


df_meta2 = df_meta.groupby(["dialog_id"]).count()
df_meta2['users'].nlargest(10)

