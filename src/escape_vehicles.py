# 3rd Party Pacakges
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Built-in Packages
import time
import os

# Load environment variables from the .env file
load_dotenv()

# Get email configuration from environment variables
CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")

def get_ford_mfg_escape_prices():
    # Set up the Chrome driver
    chrome_service = ChromeService(executable_path=CHROME_DRIVER_PATH)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", False)  
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    url = "https://www.ford.ca/suvs-crossovers/escape/?gnav=header-suvs-vhp"
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    escape_prices = []

    # Extract Mustang models and prices
    model_elements = driver.find_elements(By.XPATH, "//*[@class='bri-txt generic-title-one ff-b']")
    price_elements = driver.find_elements(By.XPATH, '//*[@class="bri-txt body-one ff-b"]') 
    
    for model, price in zip(model_elements, price_elements):
        model_name = model.text.strip()
        price_value = price.text.strip()
        if model_name == '' or price_value == '':
          continue  
        escape_prices.append((model_name, price_value))  

    # Close the browser
    driver.quit()

    return escape_prices


def get_ford_dealer_escape_prices():
    # Set up the Chrome driver
    chrome_service = ChromeService(executable_path=CHROME_DRIVER_PATH)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", False)  
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    url = "https://fordtodealers.ca/ford-escape/"
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    escape_prices = []

    li_s = driver.find_elements(By.XPATH,"(//ul[@class='wpb_tabs_nav ui-tabs-nav clearfix'])/li")
    print(li_s)

    # Extract Mustang models and prices
    #model_elements = driver.find_elements(By.XPATH, "//*[@class='bri-txt generic-title-one ff-b']")
    #price_elements = driver.find_elements(By.XPATH, '//*[@class="bri-txt body-one ff-b"]') 
    
    #for model, price in zip(model_elements, price_elements):
    #    model_name = model.text.strip()
    #    price_value = price.text.strip()
    #    if model_name == '' or price_value == '':
    #      continue  
    #    escape_prices.append((model_name, price_value))  

    # Close the browser
    driver.quit()

    return escape_prices

# Test Functions
#print(get_ford_mfg_escape_prices())
#print(get_ford_dealer_escape_prices())