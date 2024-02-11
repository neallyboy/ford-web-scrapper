import pandas as pd


class Vehicle:
    def __init__(self, model, price, category=None, hero_image=None):
        self.model = model.text.strip() if model else "Unknown"
        self.price = self.clean_price(price)
        self.category = category.text.strip() if category else "Unknown"
        self.hero_image = hero_image.text.strip() if hero_image else "Unknown"

    def __str__(self):
        return f"Category: {self.category}, Model: {self.model}, Price: {self.price}, Hero Image: {self.hero_image}"

    def clean_price(self, price):
        try:
            # Strip non-numeric characters and convert to numeric
            cleaned_price = pd.to_numeric(
                price.replace("[\$,]", "", regex=True), errors="coerce"
            )

            return cleaned_price
        except ValueError:
            return None  # or any default value indicating an invalid price

    def convert_price_to_currency(self, decimal_places=0):
        try:
            if pd.notnull(self.price):
                # Assuming the price is in dollars and cents format
                price_in_cents = int(float(self.price) * (10**decimal_places))
                dollars, cents = divmod(price_in_cents, 10**decimal_places)

                if decimal_places == 0:
                    return f"${dollars:,}"
                else:
                    return f"${dollars:,}.{cents:0{decimal_places}d}"
            else:
                return "Invalid Price Format"
        except ValueError:
            return "Invalid Price Format"


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


# ------------------------------------------
# Get prices from ford.ca
# ------------------------------------------
def get_ford_mfg_mustang_prices():

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

    # Mustangs URL
    url = MUSTANG_MANUFACTURER_URL
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    mustang_prices = []

    try:
        # Get all the buttons to scroll through the Mustang models
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

            # Extract Mustang models and prices using Selenium
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
                mustang_prices.append((model_name, price_value))

        # Remove possible duplicates
        mustang_prices = list(set(mustang_prices))

    except Exception as e:
        mustang_prices = [("Ford.ca Error", e)]

    finally:
        # Close the browser
        driver.quit()

    return mustang_prices
