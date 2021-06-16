from bs4 import BeautifulSoup as soup 
import requests
import io
from selenium import webdriver
import time
import json
from pymongo import MongoClient
import re

page_url = "https://www.bbc.com/arabic/topics/c95y3q41dq0t"
driver = webdriver.Chrome()
driver.get(page_url)

def lastItem():
    return '/html/body/div[2]/div[10]'

def procedeToNextPage(i):
    if i == 0:
        NexPage = i+2
    else:
        NexPage = i+1
    path = '/page/'+str(NexPage)
    driver.get('https://www.bbc.com/arabic/topics/c95y3q41dq0t' + path)

def scrollScrapAndClickForMoreNews(driver , i):
    time.sleep(4)
    print("--------------Scrolling Down--------------")
    driver.execute_script("arguments[0].scrollIntoView()", driver.find_element_by_xpath(lastItem()))
    time.sleep(4)
    print("--------------Clicking for more news--------------")
    procedeToNextPage(i)

def storingData(ucli , d):
    print("--------------Writing results in a txt file--------------")
    uClient = ucli
    page_soup = soup(d.page_source,"html.parser")
    uClient.close()
    with io.open("FakeNews.txt", "a", encoding="utf-8") as f:
        buffer = page_soup.findAll("div", {"class": "gel-5/8@l"})
        for b in buffer:
            if 'كورونا' in b.find('p').text.strip() or 'كوفيد' in b.find('p').text.strip():
                my_new_string = re.sub(r'[^0-9\u0600-\u06ff\u0750-\u077f\ufb50-\ufbc1\ufbd3-\ufd3f\ufd50-\ufd8f\ufd50-\ufd8f\ufe70-\ufefc\uFDF0-\uFDFD]+', ' ', b.find('p').text.strip())
                f.write(b.find('p').text.strip() + ";" + "FAKE" +"\n")

def scrapNnews(nNews,driver ,par3):
    for i in range(nNews):
        storingData(par3 , driver)
        scrollScrapAndClickForMoreNews(driver , i)
        print("News are scrapped")

scrapNnews(6,driver,requests.get(page_url))

print("--------------Finished--------------")