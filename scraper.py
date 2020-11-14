import csv
from bs4 import BeautifulSoup as bs4
from selenium import webdriver


def get_url(search_term, page):
    #generate URL from search_term
    template = "https://www.amazon.de/s?k={}&page=" + str(page)
    search_term = search_term.replace(" ", "+")
    return template.format(search_term)


def get_soup(page):
    #startup the webdriver
    driver = webdriver.Chrome()

    #include keyword to url
    url = get_url("organizer", page)

    #load webpage
    driver.get(url)

    #get page soup
    soup = bs4(driver.page_source, "html.parser")

    #close webdriver
    driver.close()

    return soup


def get_items(soup):
    #get all individual items from the webpage
    results = soup.find_all("div", {"data-component-type": "s-search-result"})

    for idx, item in enumerate(results):
        asin = item["data-asin"]
        index = item["data-index"]

        sponsored = item.find("span", {"class": "aok-inline-block s-sponsored-label-info-icon"})
        if sponsored == None:
            not_sponsored = True
        else:
            not_sponsored = False

        print(asin)
        print("Index AMZ: " + index)
        idx = idx + 1
        print("Current Position: " + str(idx))
        print("Is Product Organic: " + str(not_sponsored))
        print("########")


if __name__ == "__main__":
    for page in range(1,2):     #!!! can be changed!
        soup = get_soup(page)
        get_items(soup)
