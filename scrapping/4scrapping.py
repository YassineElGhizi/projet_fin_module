from bs4 import BeautifulSoup as soup 
import requests
import io
from selenium import webdriver
import time
import json
from pymongo import MongoClient
import re

page_url = "https://www.verify-sy.com/contents/49/%D9%88%D8%A8%D8%A7%D8%A1-%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7"
driver = webdriver.Chrome()
driver.get(page_url)

def lastItem():
    return '/html/body/div[2]/div[5]/div/div[1]/div/div/div/div/div[9]'

def procedeToNextPage(i):
    NexPage = i+1
    path = '?page='+str(NexPage)
    driver.get('https://www.verify-sy.com/contents/49/%D9%88%D8%A8%D8%A7%D8%A1-%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7/' + path)

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
        buffer = page_soup.findAll("div", {"class": "content-list-desc"})
        for b in buffer:
            my_new_string = re.sub(r'[^0-9\u0600-\u06ff\u0750-\u077f\ufb50-\ufbc1\ufbd3-\ufd3f\ufd50-\ufd8f\ufd50-\ufd8f\ufe70-\ufefc\uFDF0-\uFDFD]+', ' ', b.find('p').text.strip())
            f.write(my_new_string + ";" + "FAKE" +"\n")

def scrapNnews(nNews,driver ,par3):
    for i in range(nNews):
        scrollScrapAndClickForMoreNews(driver , i)
        storingData(par3 , driver)
        print("News are scrapped")

scrapNnews(7,driver,requests.get(page_url))

print("--------------Finished--------------")