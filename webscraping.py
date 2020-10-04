from splinter import Browser
from bs4 import BeautifulSoup
import re
import time
import requests
from selenium import webdriver
import time as t
from pprint import pprint
from scraper import scrape_site

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', headless=False, **executable_path)
try: 
    url = 'https://www.bizjournals.com/houston/potm?l=&time=&type=&ind=86'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    scrape_site(soup)
    
    # html = browser.html
    # soup = BeautifulSoup(html, 'html.parser')
    # t.sleep(2)
    # scrape_site(soup)
except:
    print("Finished Scarpping as this works!")