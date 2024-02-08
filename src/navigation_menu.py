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
        chrome_options.add_argument(
            "--disable-gpu"
        )  # Necessary for headless mode on some systems
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Main URL
    url = MAIN_MANUFACTURER_URL
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    vehicle_prices = []

    try:
        # Click on Vehicles button in the main navigation bar
        all_vehicles_button = driver.find_element(
            By.XPATH, "//li[@class='main-nav-item no-float-md flyout-item-wrap']/button"
        )
        all_vehicles_button.click()

        # Get all the Sub menu buttons
        sub_menu_buttons = driver.find_elements(
            By.XPATH,
            "//button[contains(@class,'bri-nav__list-link segment-anchor-trigger fgx-btn')]//span[@class='link-text']",
        )

        if not sub_menu_buttons:
            raise Exception(
                "Vehicle sub menu navigation not found. Page structure may have changed."
            )

        # Click through each sub menu to load model and price
        for sub_menu_button in sub_menu_buttons:
            sub_menu_button_name = sub_menu_button.text.strip()
            if sub_menu_button_name == "":
                continue
            sub_menu_button.click()

            # Wait for data to load
            time.sleep(2)

            # Get the vehicle names and prices
            sub_menu_all_vehicles_names = driver.find_elements(
                By.XPATH,
                "//div[@class='vehicle-segment-layout fgx-brand-global-container-pad segment-menu-item-container open']//a[@class='veh-item-inline']",
            )
            sub_menu_all_vehicles_prices = driver.find_elements(
                By.XPATH,
                "//div[@class='vehicle-segment-layout fgx-brand-global-container-pad segment-menu-item-container open']//span[contains(@data-pricing-template,'price')]",
            )

            # For element, get the name and price
            for vehicle, price in zip(
                sub_menu_all_vehicles_names, sub_menu_all_vehicles_prices
            ):
                vehicle_name = vehicle.text.strip()
                vehicle_price = price.text.strip()
                if (
                    vehicle_name == "" or vehicle_price == ""
                ):  # Ignore half captured data
                    continue
                vehicle_prices.append(
                    (sub_menu_button_name, vehicle_name, vehicle_price)
                )

        # Remove possible duplicates
        # vehicle_prices = list(set(vehicle_prices))

    except Exception as e:
        vehicle_prices = [("Ford.ca Error", e)]

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
        chrome_options.add_argument(
            "--disable-gpu"
        )  # Necessary for headless mode on some systems
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Main URL
    url = MAIN_DEALER_URL
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    vehicle_prices = []

    try:
        # Click on Vehicles button in the main navigation bar
        all_vehicles_button = driver.find_element(
            By.XPATH, "//a[@class='mega-menu-link sf-with-ul']"
        )
        all_vehicles_button.click()

        # Get all the Sub menu buttons
        sub_menu_buttons = driver.find_elements(
            By.XPATH,
            "//li[contains(@class,'mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-has-children mega-menu-megamenu mega-menu-item')]//a[@class='mega-menu-link sf-with-ul']",
        )

        if not sub_menu_buttons:
            raise Exception(
                "Vehicle sub menu navigation not found. Page structure may have changed."
            )

        # Click through each sub menu to load model and price
        for sub_menu_button in sub_menu_buttons:
            sub_menu_button_name = sub_menu_button.text.strip()
            if sub_menu_button_name == "":
                continue
            sub_menu_button.click()

            # Wait for data to load
            time.sleep(2)

            # Get the vehicle names and prices
            sub_menu_all_vehicles_names = driver.find_elements(
                By.XPATH,
                "//li[starts-with(@class, 'mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-has-children mega-menu-megamenu mega-menu-item') and contains(@class,'mega-toggle-on')]//li[contains(@class,'mega-menu-column') and not(contains(@class, 'hide'))]//p[@class='vehicle-top']//span[contains(@class,'vehicle-name')]/a[1]",
            )
            sub_menu_all_vehicles_prices = driver.find_elements(
                By.XPATH,
                "//li[starts-with(@class, 'mega-menu-item mega-menu-item-type-custom mega-menu-item-object-custom mega-menu-item-has-children mega-menu-megamenu mega-menu-item') and contains(@class,'mega-toggle-on')]//li[contains(@class,'mega-menu-column') and not(contains(@class, 'hide'))]//p[@class='vehicle-bottom']//span[@class='vprice']/span[1]",
            )

            # For element, get the name and price
            for vehicle, price in zip(
                sub_menu_all_vehicles_names, sub_menu_all_vehicles_prices
            ):
                vehicle_name = vehicle.text.strip()
                vehicle_price = price.text.strip()
                if (
                    vehicle_name == "" or vehicle_price == ""
                ):  # Ignore half captured data
                    continue
                vehicle_prices.append(
                    (sub_menu_button_name, vehicle_name, vehicle_price)
                )

        # Remove possible duplicates
        # vehicle_prices = list(set(vehicle_prices)

    except Exception as e:
        vehicle_prices = [("Fordtodealers.ca Error", e)]

    finally:
        # Close the browser
        driver.quit()

    return vehicle_prices


# ------------------------------------------
# Create Model Prices data frame
# ------------------------------------------
def create_navigation_prices_df():

    # Get Mustang Data
    ford_mfr_nav_prices = get_ford_mfg_nav_prices()
    ford_dealer_nav_prices = get_ford_dealer_nav_prices()

    # Convert datasets to DataFrames
    nav_mfr_prices_df = pd.DataFrame(
        ford_mfr_nav_prices,
        columns=["Category", "Car Model", "Ford Manufacturer Price"],
    )
    nav_dealer_prices_df = pd.DataFrame(
        ford_dealer_nav_prices, columns=["Category", "Car Model", "Ford Dealer Price"]
    )

    # String Manipulation for matching - Change ford.ca text to upper
    nav_mfr_prices_df["Car Model"] = nav_mfr_prices_df["Car Model"].str.upper()

    # String Manipulation for matching - Remove ™ and ® from ford.ca
    nav_mfr_prices_df["Car Model"] = nav_mfr_prices_df["Car Model"].replace(
        {"™": "", "®": ""}, regex=True
    )

    # String Manipulation for matching - Remove ™ and ® from fordtodealers.ca
    nav_dealer_prices_df["Car Model"] = nav_dealer_prices_df["Car Model"].replace(
        {"™": "", "®": ""}, regex=True
    )

    # Merge datasets on 'Car Model'
    merged_df = pd.merge(
        nav_mfr_prices_df,
        nav_dealer_prices_df,
        on=["Category", "Car Model"],
        how="outer",
        suffixes=("_ford_mfr_vehicles", "_ford_dealer_vehicles"),
    )

    # Replace NaN values with $0
    merged_df.fillna("$0", inplace=True)

    # Add a column for price comparison
    merged_df["Price Comparison"] = "Match"
    merged_df.loc[
        merged_df["Ford Manufacturer Price"] != merged_df["Ford Dealer Price"],
        "Price Comparison",
    ] = "Mismatch"

    return merged_df


# Test Functions
# print(get_ford_mfg_nav_prices())
# print(get_ford_dealer_nav_prices())
# print(create_navigation_prices_df())
# print(get_ford_mfg_mustang_hero_img())
# print(get_ford_dealer_mustang_hero_img())
# print(create_mustang_prices_df())
