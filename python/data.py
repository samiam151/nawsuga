import os, time, json, requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = None
url = "http://tracker.diabetes.org/explore/browse/starch-grains/"
payload = {
    'q': 'Python',
}
data_source = requests.get(url % payload)

# Load up the driver for Chrome
def load_driver():
    print("Loading driver...")
    chromedriver = "C:/Users/samia/Downloads/chromedriver_win32/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    global driver
    driver = webdriver.Chrome(chromedriver)

def pull():
    print("Navigating to site...")
    global url
    obj = {}
    links = []

    driver.get(url)

    print("...")
    soup = BeautifulSoup(data_source.text, "html.parser")
    base_url = "http://tracker.diabetes.org"

    left_table = soup.select("ul.bullet a")

    for a_tag in left_table:
        a_href = a_tag.get('href')
        href_string = str(base_url) + str(a_href)
        links.append(href_string)
    
    for link in links:
        
    # right_side = soup.select(".resultslist ul")

    # left_li = left_table[0].findAll('li')
    
    # for li in left_li:
    #     li_a = li.find('a')


    #     li_a_href = li_a.get('href')
    #     next_url = (str(base_url) + str(li_a))
    #     r = requests.get(next_url)


if __name__ == "__main__":
    print("Starting...")
    load_driver()
    pull()
    driver.quit()