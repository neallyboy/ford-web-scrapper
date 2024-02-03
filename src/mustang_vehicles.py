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
import re

# Load environment variables from the .env file
load_dotenv()

# Get email configuration from environment variables
CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
MUSTANG_MANUFACTURER_URL = os.getenv("MUSTANG_MANUFACTURER_URL")
MUSTANG_DEALER_URL = os.getenv("MUSTANG_DEALER_URL")

# Get prices from ford.ca
def get_ford_mfg_mustang_prices():
    
    # Set up the Chrome driver
    chrome_service = ChromeService(executable_path=CHROME_DRIVER_PATH)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", False)
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Mustangs URL
    url = MUSTANG_MANUFACTURER_URL
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    mustang_prices = []

    # Get all the buttons to scroll through the Mustang models
    buttons = driver.find_elements(By.XPATH,"(//ol[@class='bds-carousel-indicators global-indicators to-fade-in  scrollable'])/li")   # Stop at the first ol instance
    
    # Loop through available carousel buttons
    for i in range(len(buttons)):
      
      # Click the current carousel button
      buttons[i].click()

      # Time to load DOM
      time.sleep(1)  

      # Extract Mustang models and prices using Selenium
      model_elements = driver.find_elements(By.XPATH, "//*[@class='fgx-brand-ds to-fade-in title-three ff-d']")
      price_elements = driver.find_elements(By.XPATH, '//*[@class="price"]')
    
      for model, price in zip(model_elements, price_elements):
          model_name = model.text.strip()
          price_value = price.text.strip()
          if model_name == '' or price_value == '':
            continue  
          mustang_prices.append((model_name, price_value))

    # Remove possible duplicates
    mustang_prices = list(set(mustang_prices))

    # Close the browser
    driver.quit()

    return mustang_prices


# Get prices from fordtodealers.ca
def get_ford_dealer_mustang_prices():
    # Set up the Chrome driver
    chrome_service = ChromeService(executable_path=CHROME_DRIVER_PATH)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", False)  
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    url = MUSTANG_DEALER_URL
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    mustang_prices = []

    # Get all the buttons to scroll through the Mustang models
    buttons = driver.find_elements(By.XPATH,"(//div[@class='owl-dots'])[1]/button")   # Stop at the first div instance
    
    # Loop through available carousel buttons
    for i in range(len(buttons)):
      
      # Click the current carousel button
      buttons[i].click()
      
      # Time to load DOM
      time.sleep(1)
      
      try:
        # Extract Mustang models and prices
        model_elements = driver.find_elements(By.XPATH, "//*[contains(@class,'modelChecker')]")
        price_elements = driver.find_elements(By.XPATH, "//*[contains(@class,'priceChecker')]")      

        for model, price in zip(model_elements, price_elements):
            model_name = model.text.strip()
            price_value = price.text.strip()
            if model_name == '' or price_value == '':
              continue  
            mustang_prices.append((model_name, price_value))

        # Remove possible duplicates
        mustang_prices = list(set(mustang_prices))

      except Exception as e:
        mustang_image

    # Close the browser
    driver.quit()

    return mustang_prices

# Get hero image from ford.ca
def get_ford_mfg_mustang_hero_img():
    
    # Set up the Chrome driver
    chrome_service = ChromeService(executable_path=CHROME_DRIVER_PATH)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", False)
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Mustangs URL
    url = MUSTANG_MANUFACTURER_URL
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    mustang_image = ''

    try:
      # Find the img tag using a more general XPath
      img_element = driver.find_element(By.XPATH,'//*[@id="component01"]//picture/img')
      img_src = img_element.get_attribute('src')
      
      # Extract the part of the URL containing ".jpg" using regular expressions
      match = re.search(r'\/([^\/]+\.jpg)', img_src)

      if match:
        # Get the matched group (filename with .jpg)
        mustang_image = match.group(1)
      
      else:
        mustang_image = 'No jpg found'

    except Exception as e:
      mustang_image = e

    # Close the browser
    driver.quit()

    return mustang_image

# Get hero image from ford.ca
def get_ford_dealer_mustang_hero_img():
    
    # Set up the Chrome driver
    chrome_service = ChromeService(executable_path=CHROME_DRIVER_PATH)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", False)
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Mustangs URL
    url = MUSTANG_DEALER_URL
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    mustang_image = ''

    try:
      # Find the img tag using a more general XPath
      img_element = driver.find_element(By.XPATH,'//div[@class="row-bg using-image"]')
      img_src = img_element.get_attribute('style')

      # Extract the part of the URL containing ".jpg" using regular expressions
      match = re.search(r'\/([^\/]+\.jpg)', img_src)

      if match:
        # Get the matched group (filename with .jpg)
        mustang_image = match.group(1)
      
      else:
        mustang_image = 'No jpg found'

    except Exception as e:
      mustang_image = e

    # Close the browser
    driver.quit()

    return mustang_image

# Test Functions
#print(get_ford_mfg_mustang_prices())
#print(get_ford_dealer_mustang_prices())
#print(get_ford_mfg_mustang_hero_img())
#print(get_ford_dealer_mustang_hero_img())