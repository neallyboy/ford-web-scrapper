# 3rd Party Pacakges
from dotenv import load_dotenv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Built-in Packages
import os
import time

# Load environment variables from the .env file
load_dotenv(override=True)

github_token = os.getenv("GITHUB_TOKEN")


# ----------------------------------------------------------------------
# Driver setup based on environment variable
# ----------------------------------------------------------------------
def setup_driver():
    driver_type = os.getenv("BROWSER_DRIVER_TYPE", "firefox").lower()

    if driver_type == "chrome":
        return setup_chrome_driver()
    elif driver_type == "firefox":
        return setup_firefox_driver()
    elif driver_type == "edge":
        return setup_edge_driver()
    else:
        raise ValueError(
            "Invalid DRIVER_TYPE in the .env file. Use 'chrome' or 'firefox'."
        )


# ----------------------------------------------------------------------
# Chrome driver setup
# ----------------------------------------------------------------------
def setup_chrome_driver():
    chrome_service = ChromeService(ChromeDriverManager().install())
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("detach", False)
    headless_mode = os.getenv("CHROME_HEADLESS_MODE", "False").lower() == "true"
    if headless_mode:
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return driver


# ----------------------------------------------------------------------
# Edge driver setup
# ----------------------------------------------------------------------
def setup_edge_driver():
    edge_service = EdgeService(EdgeChromiumDriverManager().install())
    edge_options = EdgeOptions()
    edge_options.add_experimental_option("detach", False)
    headless_mode = os.getenv("EDGE_HEADLESS_MODE", "False").lower() == "true"
    if headless_mode:
        edge_options.add_argument("--headless")
    driver = webdriver.Edge(service=edge_service, options=edge_options)
    return driver


# ----------------------------------------------------------------------
# Firefox driver setup
# ----------------------------------------------------------------------
def setup_firefox_driver():
    os.environ["GH_TOKEN"] = github_token
    firefox_service = FirefoxService(GeckoDriverManager().install())
    firefox_options = FirefoxOptions()
    firefox_options.add_argument(
        "--disable-gpu"
    )  # Add any additional options if needed
    headless_mode = os.getenv("FIREFOX_HEADLESS_MODE", "False").lower() == "true"
    if headless_mode:
        firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
    return driver


# ----------------------------------------------------------------------
# Start Timer
# ----------------------------------------------------------------------
def start_timer():
    return time.time()


# ----------------------------------------------------------------------
# Return Elasped Time
# ----------------------------------------------------------------------
def print_elapsed_time(start_time):
    elapsed_time_seconds = time.time() - start_time
    hours, remainder = divmod(elapsed_time_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(
        f"Elapsed Time: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"
    )


# ----------------------------------------------------------------------
# Change the colour background to Red if found the word Mismatch.
# ----------------------------------------------------------------------
def redden(x):
    if x == "Mismatch":
        return f'<span style="background-color: red; color: white; padding: 2px 5px; border-radius: 3px;">{x}</span>'
    return str(x)


# ------------------------------------------
# Create Model-Prices data frame
# ------------------------------------------
def create_vehicle_prices_df(price_func_mfr, price_func_dealer):

    # Get Vehicle Prices
    vehicle_mfr_prices = price_func_mfr
    vehicle_dealer_prices = price_func_dealer

    # Convert datasets to DataFrames
    vehicle_mfr_prices_df = pd.DataFrame(
        vehicle_mfr_prices, columns=["Car Model", "Ford Manufacturer Price"]
    )
    vehicle_dealer_prices_df = pd.DataFrame(
        vehicle_dealer_prices, columns=["Car Model", "Ford Dealer Price"]
    )

    # Merge datasets on 'Car Model'
    merged_df = pd.merge(
        vehicle_mfr_prices_df,
        vehicle_dealer_prices_df,
        on="Car Model",
        how="outer",
        suffixes=("_ford_mfr_vehicles", "_ford_dealer_vehicles"),
    )

    # Sort by Manufacturer Price
    merged_df.sort_values(by=["Ford Manufacturer Price"], inplace=True)

    # Set the index to 'Car Model'
    merged_df.set_index("Car Model", inplace=True)

    # Replace NaN values with $0
    merged_df.fillna("$0", inplace=True)

    # Reset the index to avoid multi-level index rendering issues
    merged_df.reset_index(inplace=True)

    # Add a column for price difference
    merged_df["Price Difference"] = pd.to_numeric(
        merged_df["Ford Manufacturer Price"].replace("[\$,]", "", regex=True),
        errors="coerce",
    ) - pd.to_numeric(
        merged_df["Ford Dealer Price"].replace("[\$,]", "", regex=True), errors="coerce"
    )

    # Format the "Price Difference" column as currency with negative sign before the dollar amount and no decimals
    merged_df["Price Difference"] = merged_df["Price Difference"].apply(
        lambda x: "${:,.0f}".format(x).replace("$-", "-$") if pd.notnull(x) else x
    )

    # Replace NaN values with - in Price Difference
    merged_df["Price Difference"] = merged_df["Price Difference"].fillna("-")

    # Add a column for price comparison
    merged_df["Price Comparison"] = "Match"
    merged_df.loc[
        merged_df["Ford Manufacturer Price"] != merged_df["Ford Dealer Price"],
        "Price Comparison",
    ] = "Mismatch"

    return merged_df


# ------------------------------------------
# Create Model-Image data frame
# ------------------------------------------
def create_vehicle_image_df(
    hero_image_func_mfr, hero_image_func_dealer, model, mfr_image_url, dealer_image_url
):

    # Get Vehicle Images
    vehicle_mfr_hero_image = hero_image_func_mfr
    vehicle_dealer_hero_image = hero_image_func_dealer

    # Embed hyperlinks in the image URLs

    # Convert datasets to DataFrames
    hero_image_df = pd.DataFrame(
        {
            "Model Hero Image": [model],
            "Ford Manufacturer Image URL": [mfr_image_url],
            "Ford Manufacturer Image Filename": [vehicle_mfr_hero_image],
            "Ford Dealer Image URL": [dealer_image_url],
            "Ford Dealer Image Filename": [vehicle_dealer_hero_image],
        }
    )

    # Add a column for price comparison
    hero_image_df["Image Comparison"] = "Match"
    hero_image_df.loc[
        hero_image_df["Ford Manufacturer Image Filename"]
        != hero_image_df["Ford Dealer Image Filename"],
        "Image Comparison",
    ] = "Mismatch"

    return hero_image_df
