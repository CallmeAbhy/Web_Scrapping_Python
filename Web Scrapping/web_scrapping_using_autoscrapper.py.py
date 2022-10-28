#!/usr/bin/env python
# coding: utf-8

# In[1]:


from autoscraper import AutoScraper


# In[2]:


noon_url = "https://www.noon.com/egypt-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/"

wanted_list = ["18D-141 Yoga Roller Pink 30cm",
               "EGP 182.00", "EGP 293.00", "5.0", "1 Rating", "37% Off"]


# In[4]:


scraper = AutoScraper()
result = scraper.build(noon_url, wanted_list)
print(result)


# In[6]:


scraper.get_result_similar(noon_url, grouped=True)


# In[8]:


scraper.set_rule_aliases({'rule_ayd1': 'Title'})
scraper.keep_rules(['rule_ayd1'])
scraper.save('amazon-search')


# In[9]:


results = scraper.get_result_similar(
    'https: // www.noon.com/egypt-en/sports-and -outdoors/exercise-and -fitness/yoga-16328 /?limit=150 & sort % 5Bby % 5D=popularity & sort % 5Bdir % 5D=desc', group_by_alias=True)


# In[10]:


results['Price']


# In[ ]:
