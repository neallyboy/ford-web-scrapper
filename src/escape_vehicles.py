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
ESCAPE_MANUFACTURER_URL = os.getenv("ESCAPE_MANUFACTURER_URL")
ESCAPE_DEALER_URL = os.getenv("ESCAPE_DEALER_URL")


# ------------------------------------------
# Get prices from ford.ca
# ------------------------------------------
def get_ford_mfg_escape_prices():
    # Set up the Chrome driver
    chrome_service = ChromeService(executable_path=CHROME_DRIVER_PATH)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", False)  
    # Check if CHROME_HEADLESS_MODE is set to 'True' in the environment
    headless_mode = os.getenv("CHROME_HEADLESS_MODE", "False").lower() == "true"
    if headless_mode:
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        chrome_options.add_argument("--disable-gpu")  # Necessary for headless mode on some systems
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    url = ESCAPE_MANUFACTURER_URL
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    escape_prices = []

    try:
      # Extract Mustang models and prices
      model_elements = driver.find_elements(By.XPATH, "//*[@class='bri-txt generic-title-one ff-b']")
      price_elements = driver.find_elements(By.XPATH, '//*[@class="bri-txt body-one ff-b"]')

      # Check if model or price elements are not found
      if not model_elements or not price_elements:
         raise Exception("Model or price elements not found. Page structure may have changed.")
    
      for model, price in zip(model_elements, price_elements):
          model_name = model.text.strip()
          price_value = price.text.strip()
          if model_name == '' or price_value == '':
            continue  
          escape_prices.append((model_name, price_value))  

    except Exception as e:
        escape_prices = [('Ford.ca Error', e)]

    finally:
      # Close the browser
      driver.quit()

    return escape_prices


# ------------------------------------------
# Get prices from fordtodealers.ca
# ------------------------------------------
def get_ford_dealer_escape_prices():
    # Set up the Chrome driver
    chrome_service = ChromeService(executable_path=CHROME_DRIVER_PATH)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", False)  
    # Check if CHROME_HEADLESS_MODE is set to 'True' in the environment
    headless_mode = os.getenv("CHROME_HEADLESS_MODE", "False").lower() == "true"
    if headless_mode:
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        chrome_options.add_argument("--disable-gpu")  # Necessary for headless mode on some systems
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    url = ESCAPE_DEALER_URL
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    escape_prices = []

    try:
      # Extract Mustang models and prices
      model_elements = driver.find_elements(By.XPATH, "//span[@class='modelCheckerLi']")
      price_elements = driver.find_elements(By.XPATH, "//span[@class='modelCheckerLi']/label")

      # Check if model or price elements are not found
      if not model_elements or not price_elements:
         raise Exception("Model or price elements not found. Page structure may have changed.")
    
      for model, price in zip(model_elements, price_elements):
          model_name = model.text.strip().split('\n')[0]        # Strip everything after '\n'
          price_value = price.text.strip()
          if model_name == '' or price_value == '':
            continue  
          escape_prices.append((model_name, price_value))

    except Exception as e:
        escape_prices = [('Fordtodealers.ca Error', e)]

    finally:
      # Close the browser
      driver.quit()

    return escape_prices


# ------------------------------------------
# Get hero image from ford.ca
# ------------------------------------------
def get_ford_mfg_escape_hero_img():
    
    # Set up the Chrome driver
    chrome_service = ChromeService(executable_path=CHROME_DRIVER_PATH)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", False)
    # Check if CHROME_HEADLESS_MODE is set to 'True' in the environment
    headless_mode = os.getenv("CHROME_HEADLESS_MODE", "False").lower() == "true"
    if headless_mode:
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        chrome_options.add_argument("--disable-gpu")  # Necessary for headless mode on some systems
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    url = ESCAPE_MANUFACTURER_URL
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    escape_image = ''

    try:
      # Find the img tag using a more general XPath
      img_element = driver.find_element(By.XPATH,'//div[@class="billboard-img"]//picture/img')
      img_src = img_element.get_attribute('src')
      
      # Extract the part of the URL containing ".jpg" using regular expressions
      match = re.search(r'\/([^\/]+\.jpg)', img_src)

      if match:
        # Get the matched group (filename with .jpg)
        escape_image = match.group(1)
      
      else:
        escape_image = 'No jpg found'

    except Exception as e:
      escape_image = e

    # Close the browser
    driver.quit()

    return escape_image


# ------------------------------------------
# Get hero image from fordtodealers.ca
# ------------------------------------------
def get_ford_dealer_escape_hero_img():
    
    # Set up the Chrome driver
    chrome_service = ChromeService(executable_path=CHROME_DRIVER_PATH)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", False)
    # Check if CHROME_HEADLESS_MODE is set to 'True' in the environment
    headless_mode = os.getenv("CHROME_HEADLESS_MODE", "False").lower() == "true"
    if headless_mode:
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        chrome_options.add_argument("--disable-gpu")  # Necessary for headless mode on some systems
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    url = ESCAPE_DEALER_URL
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    escpae_image = ''

    try:
      # Find the img tag using a more general XPath
      img_element = driver.find_element(By.XPATH,'//div[@class="row-bg using-image"]')
      img_src = img_element.get_attribute('style')

      # Extract the part of the URL containing ".jpg" or "jpeg" using regular expressions
      match = re.search(r'\/([^\/]+\.jpe?g)', img_src)

      if match:
        # Get the matched group (filename with .jpg)
        escpae_image = match.group(1)
      
      else:
        escpae_image = 'No jpg found'

    except Exception as e:
      escpae_image = e

    # Close the browser
    driver.quit()

    return escpae_image


# ------------------------------------------
# Create Model Prices data frame
# ------------------------------------------
def create_escape_prices_df():
  
  # Get Mustang Data
  ford_mfr_escape_prices = get_ford_mfg_escape_prices()
  ford_dealer_escape_prices = get_ford_dealer_escape_prices()

  # Convert datasets to DataFrames
  escape_mfr_prices_df = pd.DataFrame(ford_mfr_escape_prices, columns=['Car Model', 'Ford Manufacturer Price'])
  escape_dealer_prices_df = pd.DataFrame(ford_dealer_escape_prices, columns=['Car Model', 'Ford Dealer Price'])

  # Merge datasets on 'Car Model'
  merged_df = pd.merge(escape_mfr_prices_df, escape_dealer_prices_df, on='Car Model', how='outer', suffixes=('_ford_mfr_vehicles', '_ford_dealer_vehicles'))

  # Sort
  merged_df.sort_values(by=['Ford Manufacturer Price'], inplace=True)

  # Set the index to 'Car Model'
  merged_df.set_index('Car Model', inplace=True)

  # Replace NaN values with $0
  merged_df.fillna('$0', inplace=True)

  # Reset the index to avoid multi-level index rendering issues
  merged_df.reset_index(inplace=True)

  # Add a column for price comparison
  merged_df['Price Comparison'] = 'Match'
  merged_df.loc[merged_df['Ford Manufacturer Price'] != merged_df['Ford Dealer Price'], 'Price Comparison'] = 'Mismatch'

  return merged_df


# ------------------------------------------
# Create Model Image data frame
# ------------------------------------------
def create_escape_image_df():
  
  # Get Escape Data
  ford_mfr_escape_image = get_ford_mfg_escape_hero_img()
  ford_dealer_escape_image = get_ford_dealer_escape_hero_img()

  # Convert datasets to DataFrames
  hero_image_df = pd.DataFrame({'Model Hero Image': ['Escape'],'Ford Manufacturer Image': [ford_mfr_escape_image],'Ford Dealer Image': [ford_dealer_escape_image]})

  # Add a column for price comparison
  hero_image_df['Image Comparison'] = 'Match'
  hero_image_df.loc[hero_image_df['Ford Manufacturer Image'] != hero_image_df['Ford Dealer Image'], 'Image Comparison'] = 'Mismatch'

  return hero_image_df

# Test Functions
#print(get_ford_mfg_escape_prices())
#print(get_ford_dealer_escape_prices())
#print(create_escape_prices_df())
#print(get_ford_mfg_escape_hero_img())
#print(get_ford_dealer_escape_hero_img())
#print(create_escape_image_df())