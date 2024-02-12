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
        chrome_options.add_argument(
            "--disable-gpu"
        )  # Necessary for headless mode on some systems
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Vehicle URL
    url = ESCAPE_MANUFACTURER_URL
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    vehicle_prices = []

    try:
        # Extract vehicle models and prices
        model_elements = driver.find_elements(
            By.XPATH, "//*[@class='bri-txt generic-title-one ff-b']"
        )
        price_elements = driver.find_elements(
            By.XPATH, '//*[@class="bri-txt body-one ff-b"]'
        )

        # Check if model or price elements are not found
        if not model_elements or not price_elements:
            raise Exception(
                "Model or price elements not found. Page structure may have changed."
            )

        for model, price in zip(model_elements, price_elements):
            model_name = model.text.strip()
            price_value = price.text.strip()
            if model_name == "" or price_value == "":
                continue
            vehicle_prices.append((model_name, price_value))

    except Exception as e:
        vehicle_prices = [("Ford.ca Error", e)]

    finally:
        # Close the browser
        driver.quit()

    return vehicle_prices


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
        chrome_options.add_argument(
            "--disable-gpu"
        )  # Necessary for headless mode on some systems
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Vehicle URL
    url = ESCAPE_DEALER_URL
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    vehicle_prices = []

    try:
        # Extract vehicle models and prices
        model_elements = driver.find_elements(
            By.XPATH, "//span[@class='modelCheckerLi']"
        )
        price_elements = driver.find_elements(
            By.XPATH, "//span[@class='modelCheckerLi']/label"
        )

        # Check if model or price elements are not found
        if not model_elements or not price_elements:
            raise Exception(
                "Model or price elements not found. Page structure may have changed."
            )

        for model, price in zip(model_elements, price_elements):
            model_name = model.text.strip().split("\n")[
                0
            ]  # Strip everything after '\n'
            price_value = price.text.strip()
            if model_name == "" or price_value == "":
                continue
            vehicle_prices.append((model_name, price_value))

    except Exception as e:
        vehicle_prices = [("Fordtodealers.ca Error", e)]

    finally:
        # Close the browser
        driver.quit()

    return vehicle_prices


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
        chrome_options.add_argument(
            "--disable-gpu"
        )  # Necessary for headless mode on some systems
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Vehicle URL
    url = ESCAPE_MANUFACTURER_URL
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    vehicle_image = ""

    try:
        # Find the img tag using a more general XPath
        img_element = driver.find_element(
            By.XPATH, '//div[@class="billboard-img"]//picture/img'
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
def get_ford_dealer_escape_hero_img():

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
    url = ESCAPE_DEALER_URL
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
# print(get_ford_mfg_escape_prices())
# print(get_ford_dealer_escape_prices())
# print(get_ford_mfg_escape_hero_img())
# print(get_ford_dealer_escape_hero_img())
