from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq  # Web client
import io
from selenium import webdriver
import time
import json
from pymongo import MongoClient
import re

page_url = "https://misbar.com/tags/%D9%83%D9%88%D8%B1%D9%88%D9%86%D8%A7"
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(5)
driver.get(page_url)

def lastItem():
    return '/html/body/app-root/div/div[1]/div[2]/keywords-page/div/section/div/div[2]/search-card[10]/div/a/div/div/div[2]/div/p/div'

def toBeClicked():
    return '/html/body/app-root/div/div[1]/div[2]/keywords-page/div/section/div/div[3]/div/span'

def coockies():
    time.sleep(25)
    print("--------------Accepting Coockies--------------")
    driver.find_element_by_xpath('/html/body/app-root/div/misbar-popup/section/span/newsletter-popup/div/div[2]/div/div/button').click()

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
        print("News are scrapped")

coockies()
scrapNnews(25,driver)

print("--------------Writing results in a txt file--------------")
uClient = uReq(page_url)
page_soup = soup(driver.page_source,"html.parser")
uClient.close()
with io.open("FakeNews.txt", "a", encoding="utf-8") as f:
    buffer = page_soup.findAll("p", {"class": "card-text"})
    for b in buffer:
        if 'كورونا' in (b.find('div').text.strip()) or 'كوفيد' in b.find('div').text.strip():
            my_new_string = re.sub(r'[^0-9\u0600-\u06ff\u0750-\u077f\ufb50-\ufbc1\ufbd3-\ufd3f\ufd50-\ufd8f\ufd50-\ufd8f\ufe70-\ufefc\uFDF0-\uFDFD]+', ' ', b.find('div').text.strip())
            f.write(my_new_string + ";" + "FAKE" +"\n")

print("--------------Finished--------------")