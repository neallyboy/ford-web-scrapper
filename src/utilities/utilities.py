# 3rd Party Pacakges
from dotenv import load_dotenv
import pandas as pd

# Built-in Packages
import os
import re
import time
from typing import Callable, Optional

# Load environment variables from the .env file
load_dotenv(override=True)


# ----------------------------------------------------------------------
# Start Timer
# ----------------------------------------------------------------------
def start_timer() -> float:
    return time.time()


# ----------------------------------------------------------------------
# Return Elasped Time
# ----------------------------------------------------------------------
def print_elapsed_time(start_time: float, process_name: str) -> None:
    elapsed_time_seconds = time.time() - start_time
    hours, remainder = divmod(elapsed_time_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(
        f"{process_name}: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"
    )


# ----------------------------------------------------------------------
# Change the colour background to Red if found the word Mismatch.
# ----------------------------------------------------------------------
def redden(x: str) -> str:
    if x == "Mismatch":
        return f'<span style="background-color: red; color: white; padding: 2px 5px; border-radius: 3px;">{x}</span>'
    return str(x)


# ------------------------------------------
# Create Model-Prices data frame
# ------------------------------------------
def create_vehicle_prices_df(
    price_func_mfr: Callable[[], list], price_func_dealer: Callable[[], list]
) -> pd.DataFrame:

    # Get Vehicle Prices
    vehicle_mfr_prices = price_func_mfr()
    vehicle_dealer_prices = price_func_dealer()

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
    hero_image_func_mfr: Callable[[], str],
    hero_image_func_dealer: Callable[[], str],
    model: str,
    mfr_image_url: str,
    dealer_image_url: str,
) -> pd.DataFrame:

    # Get Vehicle Images
    vehicle_mfr_hero_image = hero_image_func_mfr()
    vehicle_dealer_hero_image = hero_image_func_dealer()

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


# ------------------------------------------------
# Find image filename from img source attributte
# ------------------------------------------------
def parse_img_filename(img_src: str) -> Optional[re.Match]:
    return re.search(r"\/([^\/]+\.(jpe?g|png|mp4|tif|webp))", img_src)
