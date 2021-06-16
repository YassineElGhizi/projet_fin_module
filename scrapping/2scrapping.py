from bs4 import BeautifulSoup as soup 
import requests
import io
from selenium import webdriver
import time
import json
from pymongo import MongoClient
import re

page_url = "https://fatabyyano.net/category/medical-rumors/"
driver = webdriver.Chrome()
driver.get(page_url)

def lastItem():
    return '/html/body/div[1]/main/section/div/div/div/div/div/div[2]/div/div/div/div/div[1]/article[10]/div'

def toBeClicked():
    return '/html/body/div[1]/main/section/div/div/div/div/div/div[2]/div/div/div/div/div[3]/a'

def scrollScrapAndClickForMoreNews(driver):
    time.sleep(4)
    print("--------------Scrolling Down--------------")
    driver.execute_script("arguments[0].scrollIntoView()", driver.find_element_by_xpath(lastItem()))
    time.sleep(4)
    print("--------------Clicking for more news--------------")
    driver.find_element_by_xpath(toBeClicked()).click()
    time.sleep(12)

def scrapNnews(nNews,driver):
    for i in range(nNews):
        scrollScrapAndClickForMoreNews(driver)
        print("News are scrapped")

scrapNnews(15,driver)

print("--------------Writing results in a txt file--------------")
uClient = requests.get(page_url)
page_soup = soup(driver.page_source,"html.parser")
uClient.close()
with io.open("FakeNews.txt", "a", encoding="utf-8") as f:
    buffer = page_soup.findAll("h2", {"class": "w-post-elm post_title usg_post_title_1 entry-title color_link_inherit has_text_color"})
    for b in buffer:
        if 'كورونا' in b.find('a').text.strip() or 'كوفيد' in b.find('a').text.strip() or 'لقاح' in b.find('a').text.strip() or 'كمامات' in b.find('a').text.strip():
            my_new_string = re.sub(r'[^0-9\u0600-\u06ff\u0750-\u077f\ufb50-\ufbc1\ufbd3-\ufd3f\ufd50-\ufd8f\ufd50-\ufd8f\ufe70-\ufefc\uFDF0-\uFDFD]+', ' ', b.find('a').text.strip())
            f.write(my_new_string + ";" + "Fake" +"\n")

print("--------------Finished--------------")