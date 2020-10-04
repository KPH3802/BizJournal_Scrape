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
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', headless=False, **executable_path)
    browser.visit(button)
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

#             try:
#                 browser.visit(i["Link"])
#                 t.sleep(1)
#                 html = browser.html
#                 soup = BeautifulSoup(html, 'html.parser')
#                 info_list = soup.find_all('p', class_ = 'cXenseParse')
#                 i["Title"] = info_list[0].text
#                 i["Blurb"] = info_list[1].text
#                 new_dict.append(i)

#             except:
#                 print("Finished with indidudals")

#     # print("Finished the page!")
#     # browser.visit(button)

# # def scrape_individuals(dict_list):

# #     new_dict = []
#     for i in dict_list:

#         try:
#             browser.visit(i["Link"])
#             t.sleep(1)
#             html = browser.html
#             soup = BeautifulSoup(html, 'html.parser')
#             info_list = soup.find_all('p', class_ = 'cXenseParse')
#             i["Title"] = info_list[0].text
#             i["Blurb"] = info_list[1].text
#             new_dict.append(i)

#         except:
#             print("Error! trying to get")
#     print("done with individuals!")
    

#     # print("Finished Scraping!")