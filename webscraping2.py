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
                
                #Google Search query
                query = i['Name'] + ' ' + i["Title"]
                # Using the first page of Google
                page = 1
                start = (page - 1) * 10 + 1
                url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
                # print(i["Name"])
                search_name = i["Name"]
                try: 
                    # make the API request
                    data = requests.get(url).json()
                    search_items = data.get("items")
                    link = search_item.get("link")
                    i["Business Link"] = link
                    print(link)
                except:
                    print(f"Could not get {search_name}")
                Final_List.append(i)
        except:
            name = i["Name"]
            print(f"Couldn't find {name}")
    try:
        browser.visit(button)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        scrape_site(soup)
    except:
        print("Finished with HBJ! Now moving to Google Search")
        for i in Final_List:

        # print(Final_List)
        # try:
        #     df = pd.DataFrame(Final_List)
        #     df.to_csv("Data_Scraped/Contacts.csv", index=False)
        # except IOError:
        #     print("I/O Error")

        # df = pd.DataFrame(dict_list)
        # df.to_csv("Contacts.csv", index=True)
        # csv_columns = ['Name','Link','Title', 'Blurb']

        # with open(file_to_output, 'w') as csvfile:
        #     writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        #     writer.writeheader()
        #     for data in Final_List:
        #         writer.writerow(data)
        # except IOError:
        #     print("I/O error")
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