import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

WEBSITE_URL = 'https://www.data.gov.uk/dataset/5b3267d8-4307-4eef-a9af-3a4c28224694/planned-road-works-on-the-national-highways-road-network'

def get_current_links() -> list[str]:
    """
    Scrapes the website and returns a list of the current file links available.

    Returns:
        list[str]: list of file links in AWS S3.
    """
    pwd = os.path.abspath(os.path.join(os.getcwd()))
    chrome_dir = os.path.join(pwd, "chrome_driver")
    driver_path = os.path.join(chrome_dir, 'chromedriver.exe')
    driver = webdriver.Chrome(service=Service(driver_path))

    driver.get(WEBSITE_URL)

    elements = driver.find_elements(By.XPATH, "//a[@data-ga-event='download'][@class='govuk-link']")

    file_links = []
    for element in elements:
        element_link = element.get_attribute('href')
        file_links.append(element_link)

    driver.close()

    return file_links
