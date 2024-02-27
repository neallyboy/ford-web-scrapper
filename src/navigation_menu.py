# 3rd Party Pacakges
from dotenv import load_dotenv
import pandas as pd
from selenium.webdriver.common.by import By

# Built-in Packages
import time
from typing import List, Tuple
import os
import re
import sys

# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(script_dir))
sys.path.append(os.path.join(os.path.dirname(script_dir), "src"))

# Local Packages
from utilities.utilities import parse_img_filename
from classes.web_driver_singleton import WebDriverSingleton

# Load environment variables from the .env file
load_dotenv(override=True)

# Get email configuration from environment variables
MAIN_NAVIGATION_MENU_MANUFACTURER_URL = os.getenv(
    "MAIN_NAVIGATION_MENU_MANUFACTURER_URL"
)
MAIN_NAVIGATION_MENU_DEALER_URL = os.getenv("MAIN_NAVIGATION_MENU_DEALER_URL")
NAVIGATION_MODEL_LIST = os.getenv("NAVIGATION_MODEL_LIST", "")


# ------------------------------------------
# Get prices from ford.ca
# ------------------------------------------
def get_ford_mfg_nav_prices(url: str) -> List[Tuple[str, str]]:

    # Set up the Web driver
    driver = WebDriverSingleton.get_driver()

    # Main URL
    driver.get(url)
    time.sleep(3)  # Allow time for the page to load

    # Troubleshooting - Get browser console logs
    # logs = driver.get_log("browser")
    # for log in logs:
    #    print(log)

    # Troubleshooting - Save screenshot
    # driver.save_screenshot("screenshot.png")

    # Troubleshooting - Save page html source
    # with open("page_source.html", "w", encoding="utf-8") as file:
    #    file.write(driver.page_source)

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
        vehicle_prices_sorted = list(dict.fromkeys(vehicle_prices).keys())
        vehicle_prices = vehicle_prices_sorted

    except Exception as e:
        vehicle_prices = [("Ford.ca Error", str(e))]

    return vehicle_prices


# ------------------------------------------
# Get prices from fordtodealers.ca
# ------------------------------------------
def get_ford_dealer_nav_prices(url: str) -> List[Tuple[str, str, str]]:

    # Set up the Web driver
    driver = WebDriverSingleton.get_driver()

    # Main URL
    driver.get(url)
    time.sleep(3)  # Allow time for the page to load

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
        vehicle_prices_sorted = list(dict.fromkeys(vehicle_prices).keys())
        vehicle_prices = vehicle_prices_sorted

    except Exception as e:
        vehicle_prices = [("Fordtodealers.ca Error", str(e))]

    return vehicle_prices


# ------------------------------------------
# Create Model Prices data frame
# ------------------------------------------
def create_navigation_prices_df(mfr_url: str, dealer_url: str) -> pd.DataFrame:

    # Get Vehicle Data
    ford_mfr_nav_prices = get_ford_mfg_nav_prices(mfr_url)
    ford_dealer_nav_prices = get_ford_dealer_nav_prices(dealer_url)

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

    # Add a column for price difference
    merged_df["Price Difference"] = pd.to_numeric(
        merged_df["Ford Manufacturer Price"].replace("[\\$,]", "", regex=True),
        errors="coerce",
    ) - pd.to_numeric(
        merged_df["Ford Dealer Price"].replace("[\\$,]", "", regex=True),
        errors="coerce",
    )

    # Format the "Price Difference" column as currency with negative sign before the dollar amount and no decimals
    merged_df["Price Difference"] = merged_df["Price Difference"].apply(
        lambda x: "${:,.0f}".format(x).replace("$-", "-$") if pd.notnull(x) else x
    )

    # Add a column for price comparison
    merged_df["Price Comparison"] = "Match"
    merged_df.loc[
        merged_df["Ford Manufacturer Price"] != merged_df["Ford Dealer Price"],
        "Price Comparison",
    ] = "Mismatch"

    # Filter Navigation List if needed - Reducing the list
    if NAVIGATION_MODEL_LIST is not None and NAVIGATION_MODEL_LIST.strip() != "":
        car_models = [model.strip() for model in NAVIGATION_MODEL_LIST.split(",")]
        merged_df = merged_df[merged_df["Car Model"].isin(car_models)]

    return merged_df


# Test Functions
if __name__ == "__main__":
    print(get_ford_mfg_nav_prices(MAIN_NAVIGATION_MENU_MANUFACTURER_URL))
    print(get_ford_dealer_nav_prices(MAIN_NAVIGATION_MENU_DEALER_URL))
    print(
        create_navigation_prices_df(
            MAIN_NAVIGATION_MENU_MANUFACTURER_URL, MAIN_NAVIGATION_MENU_DEALER_URL
        )
    )

    driver = WebDriverSingleton.get_driver()
    driver.quit()
