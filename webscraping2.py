from splinter import Browser
from bs4 import BeautifulSoup
import re
import time
import requests
import csv
from selenium import webdriver
import time as t
from pprint import pprint
from scraper import scrape_site
from pathlib import Path
import pandas as pd
from config import API_KEY, SEARCH_ENGINE_ID
from urllib.error import HTTPError

file_to_output = Path("Data_Scraped/Contacts.csv") 

def scrape_site(soup):
    links = []
    #Get all the links to each contact
    for link in soup.find_all("a", class_="item", href=True):
        links.append(link.get('href'))
    #Get Next button
    for link in soup.find_all("a", class_="btn btn--primary pull-right", href=True):
        button = link.get('href')

    dict_list =[]
    for i in links:
        if '/houston/potmsearch/detail/submission' in i:
            d = {}
            link = "https://www.bizjournals.com/" + i
            newI = i.split("?")
            slicefront = (newI[0])
            name = slicefront[46:]
            final_name = name.replace('_', " ")
            d["Name"] = final_name
            d["Link"] = link
            dict_list.append(d)
        else:
            pass
    print(dict_list)
    print("Finished with this page.")
    for i in dict_list:

        try:
                browser.visit(i["Link"])
                # t.sleep(1)
                html = browser.html
                soup = BeautifulSoup(html, 'html.parser')
                info_list = soup.find_all('p', class_ = 'cXenseParse')
                i["Title"] = info_list[0].text
                i["Blurb"] = info_list[1].text
                Final_List.append(i)

        except HTTPError as error:
            print(error)
        
    try:
        browser.visit(button)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        scrape_site(soup)
    except:
        print("Writting to file!")
        
        for i in Final_List:
             
            #Google Search query
                query = str(i['Name']) + ' ' + str(i["Title"])
                # print(len(query))
                # print(query)
                # Using the first page of Google
                page = 1
                start = (page - 1) * 10 + 1
                url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
                # print(i["Name"])
                # print(url)
                # search_name = i["Name"]
                data = requests.get(url).json()
                # print(data)
                search_items = data.get("items")
                # print(type(search_items))
                link = search_items[0].get("link")
                # print(link)
                i["Business Link"] = link

        try:
          with open(file_to_output, 'w', encoding='utf8', newline='') as csvfile:
              writer = csv.DictWriter(csvfile, fieldnames=Final_List[0].keys())
              writer.writeheader()
              writer.writerows(Final_List)
        except IOError as error:
            print(error)
        


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', headless=False, **executable_path)
try: 
    url = 'https://www.bizjournals.com/houston/potm?l=&time=&type=&ind=86'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    Final_List = []
    scrape_site(soup)
    # scrape_individuals(dict_list)
    # print(new_dict)
    
    # try:
    #     executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    #     browser = Browser('chrome', headless=False, **executable_path)
    #     browser.visit(button)
    #     # t.sleep(2)
    #     # html = browser.html
    #     # soup = BeautifulSoup(html, 'html.parser')
    #     # scrape_site(soup)
    # except:
    #     print("didn't visit")
        # print(dict_list)
#         # print(dict_list)
#         # scrape_individuals(dict_list)
#         new_dict = []
#         for i in dict_list:

    
    # html = browser.html
    # soup = BeautifulSoup(html, 'html.parser')
    # t.sleep(2)
    # scrape_site(soup)
except:
    print("Finished Scarpping as this works!")