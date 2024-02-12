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
EDGE_MANUFACTURER_URL = os.getenv("EDGE_MANUFACTURER_URL")
EDGE_DEALER_URL = os.getenv("EDGE_DEALER_URL")


# ------------------------------------------
# Get prices from ford.ca
# ------------------------------------------
def get_ford_mfg_edge_prices():

    # Set up the Chrome driver
    chrome_service = ChromeService(executable_path=CHROME_DRIVER_PATH)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", False)
    # Check if CHROME_HEADLESS_MODE is set to 'True' in the environment
    headless_mode = os.getenv("CHROME_HEADLESS_MODE", "False").lower() == "true"
    if headless_mode:
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        chrome_options.add_argument(
            "--disable-gpu"
        )  # Necessary for headless mode on some systems
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Vehicle URL
    url = EDGE_MANUFACTURER_URL
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    vehicle_prices = []

    try:
        # Get all the buttons to scroll through the vehicle models
        buttons = driver.find_elements(
            By.XPATH,
            "(//ol[@class='bds-carousel-indicators global-indicators to-fade-in  scrollable'])/li",
        )  # Stop at the first ol instance

        if not buttons:
            raise Exception(
                "Scrolling buttons not found. Page structure may have changed."
            )

        # Loop through available carousel buttons
        for i in range(len(buttons)):

            # Click the current carousel button
            buttons[i].click()

            # Time to load DOM
            time.sleep(1)

            # Extract vehicle models and prices using Selenium
            model_elements = driver.find_elements(
                By.XPATH, "//*[@class='fgx-brand-ds to-fade-in title-three ff-d']"
            )
            price_elements = driver.find_elements(By.XPATH, '//*[@class="price"]')

            # Check if model or price elements are not found
            if not model_elements or not price_elements:
                raise Exception(
                    "Model or price elements not found. Page structure may have changed."
                )

            for model, price in zip(model_elements, price_elements):
                model_name = model.text.strip()
                price_value = price.text.strip()
                if model_name == "" or price_value == "":  # Ignore half captured data
                    continue
                vehicle_prices.append((model_name, price_value))

        # Remove possible duplicates
        vehicle_prices = list(set(vehicle_prices))

    except Exception as e:
        vehicle_prices = [("Ford.ca Error", e)]

    finally:
        # Close the browser
        driver.quit()

    return vehicle_prices


# ------------------------------------------
# Get prices from fordtodealers.ca
# ------------------------------------------
def get_ford_dealer_edge_prices():
    # Set up the Chrome driver
    chrome_service = ChromeService(executable_path=CHROME_DRIVER_PATH)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", False)
    # Check if CHROME_HEADLESS_MODE is set to 'True' in the environment
    headless_mode = os.getenv("CHROME_HEADLESS_MODE", "False").lower() == "true"
    if headless_mode:
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        chrome_options.add_argument(
            "--disable-gpu"
        )  # Necessary for headless mode on some systems
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Vehicle URL
    url = EDGE_DEALER_URL
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    vehicle_prices = []

    try:
        # Get all the buttons to scroll through the vehicle models
        buttons = driver.find_elements(
            By.XPATH, "(//div[@class='owl-dots'])[1]/button"
        )  # Stop at the first div instance

        if not buttons:
            raise Exception(
                "Scrolling buttons not found. Page structure may have changed."
            )

        # Loop through available carousel buttons
        for i in range(len(buttons)):

            # Click the current carousel button
            buttons[i].click()

            # Time to load DOM
            time.sleep(1)

            # Extract vehicle models and prices
            model_elements = driver.find_elements(
                By.XPATH, "//*[contains(@class,'modelChecker')]"
            )
            price_elements = driver.find_elements(
                By.XPATH, "//*[contains(@class,'priceChecker')]"
            )

            # Check if model or price elements are not found
            if not model_elements or not price_elements:
                raise Exception(
                    "Model or price elements not found. Page structure may have changed."
                )

            for model, price in zip(model_elements, price_elements):
                model_name = model.text.strip()
                price_value = price.text.strip()
                if model_name == "" or price_value == "":  # Ignore half captured data
                    continue
                vehicle_prices.append((model_name, price_value))

            # Remove possible duplicates
            vehicle_prices = list(set(vehicle_prices))

    except Exception as e:
        vehicle_prices = [("Fordtodealers.ca Error", e)]

    # Close the browser
    driver.quit()

    return vehicle_prices


# ------------------------------------------
# Get hero image from ford.ca
# ------------------------------------------
def get_ford_mfg_edge_hero_img():

    # Set up the Chrome driver
    chrome_service = ChromeService(executable_path=CHROME_DRIVER_PATH)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", False)
    # Check if CHROME_HEADLESS_MODE is set to 'True' in the environment
    headless_mode = os.getenv("CHROME_HEADLESS_MODE", "False").lower() == "true"
    if headless_mode:
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        chrome_options.add_argument(
            "--disable-gpu"
        )  # Necessary for headless mode on some systems
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Vehicle URL
    url = EDGE_MANUFACTURER_URL
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    vehicle_image = ""

    try:
        # Find the img tag using a more general XPath
        img_element = driver.find_element(
            By.XPATH, '//*[@id="component01"]//picture/img'
        )
        img_src = img_element.get_attribute("src")

        # Extract the part of the URL containing image using regular expressions
        match = re.search(r"\/([^\/]+\.(jpe?g|png|mp4))", img_src)

        if match:
            # Get the matched group (filename with image file extension)
            vehicle_image = match.group(1)

        else:
            vehicle_image = "No jpg, jpeg, or png found"

    except Exception as e:
        vehicle_image = e

    # Close the browser
    driver.quit()

    return vehicle_image


# ------------------------------------------
# Get hero image from fordtodealers.ca
# ------------------------------------------
def get_ford_dealer_edge_hero_img():

    # Set up the Chrome driver
    chrome_service = ChromeService(executable_path=CHROME_DRIVER_PATH)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", False)
    # Check if CHROME_HEADLESS_MODE is set to 'True' in the environment
    headless_mode = os.getenv("CHROME_HEADLESS_MODE", "False").lower() == "true"
    if headless_mode:
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        chrome_options.add_argument(
            "--disable-gpu"
        )  # Necessary for headless mode on some systems
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Vehicle URL
    url = EDGE_DEALER_URL
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    vehicle_image = ""

    try:
        # Find the img tag using a more general XPath
        img_element = driver.find_element(
            By.XPATH,
            '//div[starts-with(@class,"row-bg") and contains(@class,"using-image")]',
        )
        img_src = img_element.get_attribute("style")

        # Extract the part of the URL containing image using regular expressions
        match = re.search(r"\/([^\/]+\.(jpe?g|png|mp4))", img_src)

        if match:
            # Get the matched group (filename with image file extension)
            vehicle_image = match.group(1)

        else:
            vehicle_image = "No jpg, jpeg, or png found"

    except Exception as e:
        vehicle_image = e

    # Close the browser
    driver.quit()

    return vehicle_image


# Test Functions
# print(get_ford_mfg_edge_prices())
# print(get_ford_dealer_edge_prices())
# print(get_ford_mfg_edge_hero_img())
# print(get_ford_dealer_edge_hero_img())
