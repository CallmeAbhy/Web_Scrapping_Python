#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
import bs4
from bs4 import BeautifulSoup


# In[5]:


url = 'https://www.noon.com/egypt-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/'


# In[6]:


headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}


# In[7]:


r = requests.get(url,{'headers':headers})


# In[8]:


soup = bs4.BeautifulSoup(r.text,'html.parser')


# In[6]:


# Product name currency price
i = 0
length = len(soup.find_all('div',{'class':'sc-f8165ac8-17 WwCBf'}))
while i < length:
    product = soup.find_all('div',{'class':'sc-f8165ac8-17 WwCBf'})[i].find('span').text
    print(str(i+1) +" " + product)
    #print(soup.find_all('div',{'class':'sc-f8165ac8-17 WwCBf'})[i].find('span').text)
    print(str(soup.find_all('div',{'class':'sc-f8165ac8-18 kOXsff'})[i].find('span').text) + str(soup.find_all('div',{'class':'sc-f8165ac8-18 kOXsff'})[i].find('strong').text))
    # print(soup.find_all('div',{'class':'sc-f8165ac8-18 kOXsff'})[i].find('strong').text)
    
    i+=1


# In[9]:


len(soup.find_all('div',{'class':'sc-f8165ac8-17 WwCBf'}))


# In[10]:



i = 0
length = len(soup.find_all('div',{'class':'sc-f8165ac8-17 WwCBf'}))
while i < length:
    product = soup.find_all('div',{'class':'sc-f8165ac8-17 WwCBf'})[i].find('span').text
    print(str(i+1) +" " + product)
    currency = soup.find_all('div',{'class':'sc-f8165ac8-18 kOXsff'})[i].find('span').text
    currentPrice = soup.find_all('div',{'class':'sc-f8165ac8-18 kOXsff'})[i].find('strong').text
    print("Price"+":  "+currency+""+currentPrice)
    
    i+=1


# In[67]:



i = 0
length = len(soup.find_all('div',{'class':'sc-f8165ac8-17 WwCBf'}))
while i < length:
    product = soup.find_all('div',{'class':'sc-f8165ac8-17 WwCBf'})[i].find('span').text
    print(str(i+1) +" " + product)
    currency = soup.find_all('div',{'class':'sc-f8165ac8-18 kOXsff'})[i].find('span').text
    currentPrice = soup.find_all('div',{'class':'sc-f8165ac8-18 kOXsff'})[i].find('strong').text
    print("Price"+":  "+currency+""+currentPrice)
    try:
        discount = soup.find_all('div',{'class':'sc-ac248257-2 kdTNiL'})[i].find('span',{'class':'discount'}).text
        print("Discount"+": "+discount)
    except:
        print("NA")
    try:
        oldPrice = soup.find_all('div',{'class':'sc-ac248257-2 kdTNiL'})[i].find('span',{'class':'oldPrice'}).text
        print("PriceWas"+": "+oldPrice)
    except:
        print("NA")
    

    i+=1


# In[74]:


print(soup.find_all('div',{'class':'sc-f8165ac8-19 bOilcU'})[2].find('span',{'class':'ratingValue'}).text)


# In[75]:


soup.find_all('div',{'class':'sc-f8165ac8-19 bOilcU'})[2].find('span',{'class':'ratingCount'}).text


# In[ ]:



    i = 0
    length = len(soup.find_all('div',{'class':'sc-f8165ac8-17 WwCBf'}))
    while i < length:

        product =soup.find_all('div',{'class':'sc-f8165ac8-17 WwCBf'})[i].find('span').text
    #product name
    print(str(i+1) +" " + product)
    currency = soup.find_all('div',{'class':'sc-f8165ac8-18 kOXsff'})[i].find('span').text
    currentPrice = soup.find_all('div',{'class':'sc-f8165ac8-18 kOXsff'})[i].find('strong').text
    # Currency and Current price
    print("Price"+":  "+currency+""+currentPrice)
    #discount info
    try:
        discount = soup.find_all('div',{'class':'sc-ac248257-2 kdTNiL'})[i].find('span',{'class':'discount'}).text
        print("Discount"+": "+discount)
    except:
        print("NA")
    #past price info
    try:
        oldPrice = soup.find_all('div',{'class':'sc-ac248257-2 kdTNiL'})[i].find('span',{'class':'oldPrice'}).text
        print("PriceWas"+": "+oldPrice)
    except:
        print("NA")
    #Rating info
    try:
        Rating = soup.find_all('div',{'class':'sc-f8165ac8-19 bOilcU'})[i].find('span',{'class':'ratingValue'}).text
        print("Rating"+": "+Rating)
    except:
        print("NA")
    #Rating Count info
    try:
        Rating_Count = soup.find_all('div',{'class':'sc-f8165ac8-19 bOilcU'})[i].find('span',{'class':'ratingCount'}).text
        print("Rating Count"+": "+Rating_Count)
    except:
        print("NA")

    i+=1


# In[ ]:




