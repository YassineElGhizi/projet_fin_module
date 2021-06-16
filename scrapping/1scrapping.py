from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq  # Web client
import io
from selenium import webdriver
import time
import json
from pymongo import MongoClient
import re

page_url = "https://arabic.rt.com/tags/Corona_virus/"
driver = webdriver.Chrome()
driver.get(page_url)

def lastItem():
    return '/html/body/div[1]/div[3]/div/div[2]/div[3]/div/div/div/ul/li[10]'

def toBeClicked():
    return '/html/body/div[1]/div[3]/div/div[2]/div[3]/div/div/div/div/div/button'

def coockies():
    time.sleep(2)
    print("--------------Accepting Coockies--------------")
    driver.find_element_by_xpath('/html/body/div[3]/div/a').click()

def scrollScrapAndClickForMoreNews(driver):
    time.sleep(4)
    print("--------------Scrolling Down--------------")
    driver.execute_script("arguments[0].scrollIntoView()", driver.find_element_by_xpath(lastItem()))
    time.sleep(4)
    print("--------------Clicking for more news--------------")
    driver.find_element_by_xpath(toBeClicked()).click()

def scrapNnews(nNews,driver):
    for i in range(nNews):
        scrollScrapAndClickForMoreNews(driver)
        print(str(((i+1)*10)+10) + " news are scrapped")

coockies()
scrapNnews(98,driver)

print("--------------Writing results in a txt file--------------")
uClient = uReq(page_url)
page_soup = soup(driver.page_source,"html.parser")
uClient.close()
with io.open("FakeNews.txt", "a", encoding="utf-8") as f:
    f.write("text" + ";" + "label" + "\n")
    buffer = page_soup.findAll("div", {"class": "list-news_text"})
    for b in buffer:
        my_new_string = re.sub(r'[^0-9\u0600-\u06ff\u0750-\u077f\ufb50-\ufbc1\ufbd3-\ufd3f\ufd50-\ufd8f\ufd50-\ufd8f\ufe70-\ufefc\uFDF0-\uFDFD]+', ' ', b.find('a').text.strip())
        f.write(my_new_string + ";" + "REAL" +"\n")

print("--------------Finished--------------")