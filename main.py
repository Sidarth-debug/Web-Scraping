from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome('chromedriver')
browser.get(start_url)
time.sleep(10)

def web_scrape():
    headers = ['proper_name','distance','mass','radius']
    star_data = []