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
MAIN_MANUFACTURER_URL = os.getenv("MAIN_MANUFACTURER_URL")
MAIN_DEALER_URL = os.getenv("MAIN_DEALER_URL")

# ------------------------------------------
# Get prices from ford.ca
# ------------------------------------------
def get_ford_mfg_nav_prices():
    
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

    # Main URL
    url = MAIN_MANUFACTURER_URL
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    vehicle_prices = []

    try:
      # Click on Vehicles button in the main navigation bar
      all_vehicles_button = driver.find_element(By.XPATH,"(//li[@class='main-nav-item no-float-md flyout-item-wrap']/button)")
      all_vehicles_button.click()

      # Get all the Sub menu buttons
      sub_menu_buttons = driver.find_elements(By.XPATH,"(//button[contains(@class,'bri-nav__list-link segment-anchor-trigger fgx-btn')]//span[@class='link-text'])")

      if not sub_menu_buttons:
          raise Exception("Vehicle sub menu navigation not found. Page structure may have changed.")

      # Click through each sub menu to load model and price
      for sub_menu_button in sub_menu_buttons:
        sub_menu_button_name = sub_menu_button.text.strip()
        if sub_menu_button_name == '':
          continue
        sub_menu_button.click()
        
        # Wait for data to load
        time.sleep(2)

        # Get the vehicle names and prices
        sub_menu_all_vehicles_names = driver.find_elements(By.XPATH,"(//div[@class='vehicle-segment-layout fgx-brand-global-container-pad segment-menu-item-container open']//a[@class='veh-item-inline'])")
        sub_menu_all_vehicles_prices = driver.find_elements(By.XPATH,"(//div[@class='vehicle-segment-layout fgx-brand-global-container-pad segment-menu-item-container open']//span[contains(@data-pricing-template,'price')])")
        
        # For element, get the name and price
        for vehicle, price in zip(sub_menu_all_vehicles_names,sub_menu_all_vehicles_prices):
          vehicle_name = vehicle.text.strip()
          vehicle_price = price.text.strip()
          if vehicle_name == '' or vehicle_price == '':           # Ignore half captured data
            continue  
          vehicle_prices.append((sub_menu_button_name,vehicle_name,vehicle_price))
    
      # Remove possible duplicates
      #vehicle_prices = list(set(vehicle_prices))

    except Exception as e:
        vehicle_prices = [('Ford.ca Error', e)]

    finally:
      # Close the browser
      driver.quit()

    return vehicle_prices


# ------------------------------------------
# Get prices from fordtodealers.ca
# ------------------------------------------
def get_ford_dealer_nav_prices():
    
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

    # Main URL
    url = MAIN_DEALER_URL
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    vehicle_prices = []

    try:
      # Click on Vehicles button in the main navigation bar
      all_vehicles_button = driver.find_element(By.XPATH,"(//li[@class='main-nav-item no-float-md flyout-item-wrap']/button)")
      all_vehicles_button.click()

      # Get all the Sub menu buttons
      sub_menu_buttons = driver.find_elements(By.XPATH,"(//button[contains(@class,'bri-nav__list-link segment-anchor-trigger fgx-btn')]//span[@class='link-text'])")

      if not sub_menu_buttons:
          raise Exception("Vehicle sub menu navigation not found. Page structure may have changed.")

      # Click through each sub menu to load model and price
      for sub_menu_button in sub_menu_buttons:
        sub_menu_button_name = sub_menu_button.text.strip()
        if sub_menu_button_name == '':
          continue
        sub_menu_button.click()
        
        # Wait for data to load
        time.sleep(2)

        # Get the vehicle names and prices
        sub_menu_all_vehicles_names = driver.find_elements(By.XPATH,"(//div[@class='vehicle-segment-layout fgx-brand-global-container-pad segment-menu-item-container open']//a[@class='veh-item-inline'])")
        sub_menu_all_vehicles_prices = driver.find_elements(By.XPATH,"(//div[@class='vehicle-segment-layout fgx-brand-global-container-pad segment-menu-item-container open']//span[contains(@data-pricing-template,'price')])")
        
        # For element, get the name and price
        for vehicle, price in zip(sub_menu_all_vehicles_names,sub_menu_all_vehicles_prices):
          vehicle_name = vehicle.text.strip()
          vehicle_price = price.text.strip()
          if vehicle_name == '' or vehicle_price == '':           # Ignore half captured data
            continue  
          vehicle_prices.append((sub_menu_button_name,vehicle_name,vehicle_price))
    
      # Remove possible duplicates
      #vehicle_prices = list(set(vehicle_prices))

    except Exception as e:
        vehicle_prices = [('Ford.ca Error', e)]

    finally:
      # Close the browser
      driver.quit()

    return vehicle_prices


# ------------------------------------------
# Get prices from fordtodealers.ca
# ------------------------------------------
def get_ford_dealer_mustang_prices():
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

    url = MUSTANG_DEALER_URL
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    mustang_prices = []

    try:
      # Get all the buttons to scroll through the Mustang models
      buttons = driver.find_elements(By.XPATH,"(//div[@class='owl-dots'])[1]/button")   # Stop at the first div instance
      
      if not buttons:
        raise Exception("Scrolling buttons not found. Page structure may have changed.")
    
      # Loop through available carousel buttons
      for i in range(len(buttons)):
      
        # Click the current carousel button
        buttons[i].click()
      
        # Time to load DOM
        time.sleep(1)
      
        # Extract Mustang models and prices
        model_elements = driver.find_elements(By.XPATH, "//*[contains(@class,'modelChecker')]")
        price_elements = driver.find_elements(By.XPATH, "//*[contains(@class,'priceChecker')]")

        # Check if model or price elements are not found
        if not model_elements or not price_elements:
           raise Exception("Model or price elements not found. Page structure may have changed.")

        for model, price in zip(model_elements, price_elements):
            model_name = model.text.strip()
            price_value = price.text.strip()
            if model_name == '' or price_value == '':           # Ignore half captured data
              continue  
            mustang_prices.append((model_name, price_value))

        # Remove possible duplicates
        mustang_prices = list(set(mustang_prices))

    except Exception as e:
      mustang_prices = [('Fordtodealers.ca Error', e)]

    # Close the browser
    driver.quit()

    return mustang_prices


# ------------------------------------------
# Get hero image from ford.ca
# ------------------------------------------
def get_ford_mfg_mustang_hero_img():
    
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


# ------------------------------------------
# Get hero image from fordtodealers.ca
# ------------------------------------------
def get_ford_dealer_mustang_hero_img():
    
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

    # Mustangs URL
    url = MUSTANG_DEALER_URL
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    mustang_image = ''

    try:
      # Find the img tag using a more general XPath
      img_element = driver.find_element(By.XPATH,'//div[@class="row-bg using-image"]')
      img_src = img_element.get_attribute('style')

      # Extract the part of the URL containing ".jpg" or "jpeg" using regular expressions
      match = re.search(r'\/([^\/]+\.jpe?g)', img_src)

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


# ------------------------------------------
# Create Model Prices data frame
# ------------------------------------------
def create_mustang_prices_df():
  
  # Get Mustang Data
  ford_mfr_mustang_prices = get_ford_mfg_mustang_prices()
  ford_dealer_mustangs_prices = get_ford_dealer_mustang_prices()

  # Convert datasets to DataFrames
  mustang_mfr_prices_df = pd.DataFrame(ford_mfr_mustang_prices, columns=['Car Model', 'Ford Manufacturer Price'])
  mustang_dealer_prices_df = pd.DataFrame(ford_dealer_mustangs_prices, columns=['Car Model', 'Ford Dealer Price'])

  # Merge datasets on 'Car Model'
  merged_df = pd.merge(mustang_mfr_prices_df, mustang_dealer_prices_df, on='Car Model', how='outer', suffixes=('_ford_mfr_vehicles', '_ford_dealer_vehicles'))

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
def create_mustang_image_df():
  
  # Get Mustang Data
  ford_mfr_mustang_image = get_ford_mfg_mustang_hero_img()
  ford_dealer_mustang_image = get_ford_dealer_mustang_hero_img()

  # Convert datasets to DataFrames
  hero_image_df = pd.DataFrame({'Model Hero Image': ['Mustang'],'Ford Manufacturer Image': [ford_mfr_mustang_image],'Ford Dealer Image': [ford_dealer_mustang_image]})

  # Add a column for price comparison
  hero_image_df['Image Comparison'] = 'Match'
  hero_image_df.loc[hero_image_df['Ford Manufacturer Image'] != hero_image_df['Ford Dealer Image'], 'Image Comparison'] = 'Mismatch'

  return hero_image_df

# Test Functions
print(get_ford_mfg_nav_prices())
#print(get_ford_dealer_nav_prices())
#print(get_ford_mfg_mustang_hero_img())
#print(get_ford_dealer_mustang_hero_img())
#print(create_mustang_prices_df())