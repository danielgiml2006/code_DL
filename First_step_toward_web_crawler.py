#!/usr/bin/env python
# coding: utf-8

# ## 1. Get webpage using *requests*

# In[34]:


import os
print(os.getcwd())


# In[28]:


import requests

req = requests.get('https://en.wikipedia.org/wiki/Data_science')
 #                  https://en.wikipedia.org/wiki/Data_science


# In[29]:


req


# In[30]:


webpage = req.text


# In[31]:


with open("filename", 'w',encoding='utf-8') as f:
    f.write(webpage)


# In[32]:


print(webpage)


# ## 2. Get specific contents using BeatifulSoup

# In[ ]:





# In[6]:


from bs4 import BeautifulSoup

soup = BeautifulSoup(webpage, 'html.parser')


# ### 2.1 Prettify the webpage

# In[7]:


print(soup.prettify())


# ### 2.2 Get the first paragraph

# You can try to remove "attrs" to see how it works.

# In[8]:


paragraph = soup.find_all('p')


# In[9]:


paragraph


# In[10]:


paragraph = soup.find('p', attrs={"class":False})


# In[11]:


paragraph


# ### 2.3 Get all the links in this paragraph which point to other webpages

# In[12]:


paragraph.find_all('a')


# In[13]:


paragraph.find_all('a', attrs={"title":True})


# In[14]:


data = {"title":[], "href":[]}
for link in paragraph.find_all('a', attrs={"title":True}):
    data["title"].append(link["title"])
    data["href"].append(link["href"])


# In[15]:


import pandas as pd
df = pd.DataFrame(data)


# In[16]:


df


# ## 3. Get the contents from all the webpages

# In[17]:


webpages = []
head = "https://en.wikipedia.org"
for href in data["href"]:
    link = head + href
    req = requests.get(link)
    webpage = req.text
    webpages.append(webpage)


# ## 4. Futher readings

# ### 4.1 robots.txt

# Check robots.txt of the website to find out what are allowed.

# In[18]:


req = requests.get("https://en.wikipedia.org/robots.txt")
webpage = req.text


# In[19]:


soup = BeautifulSoup(webpage, 'html.parser')
print(soup.text)


# ### 4.2 Sleep

# You would be banned, if you scrape a website too fast. Let your crawler sleep for a while after each round.

# In[20]:


import time

for i in range(5):
    time.sleep(3)
    print(i)


# ### 4.3 Randomness

# Pausing for extactly three seconds after each round is too robotic. Let's add some randomness to make your crawler looks more like a human.

# In[21]:


from random import random

for i in range(5):
    t = 1 + 2 * random()
    time.sleep(t)
    print(i)


# ### 4.4 Separate the codes for scraping from the ones for data extraction

# 1. Scraping is more vulnerable. Nothing is more annoying than your crawler breaks because of a bug in the data extraction part.  
# 2. You never know what data you would need for modeling. So keep all the webpages you obtain. 

# ### 4.5 Chrome Driver and Selenium

# These are the tools make your crawler act even more like a human.

# In[ ]:




