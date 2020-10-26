import csv
from bs4 import BeautifulSoup as bs4
from selenium import webdriver


def get_url(search_term):
    #generate URL from search_term
    template = "https://www.amazon.de/s?k={}"
    search_term = search_term.replace(" ", "+")
    return template.format(search_term)


if __name__ = "__main__":
    #startup the webdriver
    driver = webdriver.Chrome()

    #include keyword to url
    url = get_url("organizer")
    driver.get(url)
    print(url)

    #get page soup
    soup = bs4(driver.page_source, "html.parser")

    #get item
    results = soup.find_all("div", {"data-component-type": "s-search-result"})

    for idx, item in enumerate(results):
        ASIN = item["data-asin"]
        Index = item["data-index"]
        print(ASIN)
        print("Index AMZ: " + Index)
        idx = idx + 1
        print("Current Position: " + str(idx))
        print("########")

    #close webdriver
    driver.close()
