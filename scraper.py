import csv
from bs4 import BeautifulSoup as bs4
from selenium import webdriver
import json
import time


def get_url(search_term, page):
    #generate URL from search_term
    template = "https://www.amazon.de/s?k={}&page=" + str(page)
    search_term = search_term.replace(" ", "+")
    return template.format(search_term)


def get_soup(page):
    #include keyword to url
    url = get_url("organizer", page)

    #load webpage
    driver.get(url)

    #get page soup
    soup = bs4(driver.page_source, "html.parser")

    return soup


def get_items():
    #list for every individual page
    items = []
    #list of all pages
    all_lists = []

    #get the page soup for data
    for page in range(1,6):     #!!! can be changed!
        print("Get data from page - " + str(page))
        soup = get_soup(page)

        #get all individual items from the webpage
        results = soup.find_all("div", {"data-component-type": "s-search-result"})

        #sort out specific bits of data
        for idx, item in enumerate(results):
            asin = item["data-asin"]
            index = item["data-index"] #isn't needed

            sponsored = item.find("span", {"class": "aok-inline-block s-sponsored-label-info-icon"})
            if sponsored == None:
                not_sponsored = True
            else:
                not_sponsored = False

            if not_sponsored == True:
                items.append(asin)

            #print(asin)
            #print("Index AMZ: " + index)
            #idx = idx + 1
            #print("Current Position: " + str(idx))
            #print("Is Product Organic: " + str(not_sponsored))
            #print("########")

        #append  individual pages to the other pages
        all_lists.append(items)
        time.sleep(15) #sleep before load next site

    #sort the list of all pages
    sorted_list = []
    for items in all_lists:
        for item in items:
            sorted_list.append(item)
    #print(sorted_list)

    ranking = 1
    for item in sorted_list:
        if item == searched_asin:
            return ranking
        ranking += 1


def average(lst):
    return sum(lst) / len(lst)


if __name__ == "__main__":
    #list of all try's
    ranking_list = []

    for run in range(1,4): #get average of rankings
        print("#### This is the run " + str(run) + " ####")
        #startup the webdriver
        driver = webdriver.Chrome()

        #get ranking
        searched_asin = "B08L9GS35N"
        ranking = get_items()
        ranking_list.append(ranking)
        print(ranking)

        #close webdriver
        driver.close()
        time.sleep(30) #sleep before load next site

    print(ranking_list)
    lst = []

    #remove all None
    for item in ranking_list:
        if item != None:
            lst.append(item)

    #get average of all rankings
    average = average(lst)
    average = int(average) #round to full numbers
    print("The Overall Rank is: " + str(average))
