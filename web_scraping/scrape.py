import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from typing import List


WEBSITE_URL = "https://www.data.gov.uk/dataset/5b3267d8-4307-4eef-a9af-3a4c28224694/planned-road-works-on-the-national-highways-road-network"

def scrape_site(url: str) -> List:
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("window-size=1920x1080")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    # options.add_argument('--disable-dev-shm-usage') # Not used 
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(5)
    elements = driver.find_elements(
        By.XPATH, "//a[@data-ga-event='download'][@class='govuk-link']"
    )

    file_links = []
    for element in elements:
        element_link = element.get_attribute("href")
        file_links.append(element_link)
        
    driver.close()
    
    return file_links

print(scrape_site(WEBSITE_URL))