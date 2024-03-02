# 3rd Party Pacakges
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd

# Built-in Packages
from datetime import datetime
import os
import re
import smtplib
import time
from typing import Callable, Optional, List, Tuple

# Local Packages
from .constants import constants as const

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
    price_func_mfr: Callable[[str], list],
    price_func_dealer: Callable[[str], list],
    mfr_price_url: str,
    dealer_price_url: str,
) -> pd.DataFrame:

    # Get Vehicle Prices
    vehicle_mfr_prices = price_func_mfr(mfr_price_url)
    vehicle_dealer_prices = price_func_dealer(dealer_price_url)

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

    # Create a temporary column with numeric values
    merged_df['temp'] = pd.to_numeric(merged_df['Ford Manufacturer Price'].replace("[\$,]", "", regex=True), errors='coerce')

    # Sort by the temporary column
    merged_df.sort_values(by=['temp'], inplace=True)

    # Drop the temporary column
    merged_df.drop(columns=['temp'], inplace=True)

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
    hero_image_func_mfr: Callable[[str], str],
    hero_image_func_dealer: Callable[[str], str],
    model: str,
    mfr_image_url: str,
    dealer_image_url: str,
) -> pd.DataFrame:

    # Get Vehicle Images
    vehicle_mfr_hero_image = hero_image_func_mfr(mfr_image_url)
    vehicle_dealer_hero_image = hero_image_func_dealer(dealer_image_url)

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


# ------------------------------------------------
# Send Dealer Email
# ------------------------------------------------
def send_dealer_email(sender_email: str, receiver_email: str, password: str, subject: str, vehicles_list_html: List[Tuple[str, pd.DataFrame, str, str]], all_model_images_df: pd.DataFrame, nav_prices_df: pd.DataFrame) -> None:
    
    # Split the string into a list using comma as a separator
    receiver_emails_list = receiver_email.split(",")

    # Create the message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = (
        ",".join(receiver_emails_list)
        if len(receiver_emails_list) > 1
        else receiver_emails_list[0]
    )
    msg["Subject"] = subject

    # Customize HTML content for Gmail email
    html_content = f"""
    <html>
      <head>
        <style>
          table {{
            border-collapse: collapse;
            width: 100%;
          }}
          th, td {{
            text-align: left;
            padding: 8px;
            border: 1px solid #dddddd;
          }}
          th {{
            background-color: #f2f2f2;
          }}
          td.match {{
            background-color: green;
            color: white;
          }}
          td.mismatch {{
            background-color: red;
            color: white;
          }}
        </style>
      </head>
      <body>
        <p>Please review the most recent price and image comparisons between Ford.ca and Fordtodealers.ca. This email serves as an informational audit and requires verification by the recipient prior to any pricing updates.</p>
        <h2>NAVIGATION MENU PRICES</h2>
        Data Sources:
        <ul>
          <li>{const["MAIN_NAVIGATION_MENU_MANUFACTURER_URL"]}</li>
          <li>{const["MAIN_NAVIGATION_MENU_DEALER_URL"]}</li>
        </ul>
        {nav_prices_df.to_html(classes='table', escape=False, index=False, formatters={'Price Comparison': redden})}
    """

    # Loop through each vehicle and add corresponding HTML sections
    for vehicle_name, vehicle_df, manufacturer_url, dealer_url in vehicles_list_html:

        html_content += f"""
        <h2>{vehicle_name} PRICES</h2>
        Data Sources:
        <ul>
          <li>{manufacturer_url}</li>
          <li>{dealer_url}</li>
        </ul>
        {vehicle_df.to_html(classes='table', escape=False, index=False, formatters={'Price Comparison': redden})}
        """

    # Continue with the remaining HTML content
    html_content += f"""
        <br>
        <hr>
        <h2>MODEL HERO IMAGES</h2>
        <p>The comparisons are done based on filename and not the actual image presented.</p>
        {all_model_images_df.to_html(classes='table', escape=False, index=False, formatters={'Image Comparison': redden})}
      </body>
    </html>
    """

    msg.attach(MIMEText(html_content, "html"))

    # Connect to the SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_emails_list, msg.as_string())
        server.quit()


# ------------------------------------------------
# Send Error Email
# ------------------------------------------------
def send_error_email(sender_email: str, receiver_email: str, password: str, subject: str, error_message: str) -> None:
    
    # Split the string into a list using comma as a separator
    receiver_emails_list = receiver_email.split(",")

    # Create the message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = (
        ",".join(receiver_emails_list)
        if len(receiver_emails_list) > 1
        else receiver_emails_list[0]
    )
    msg["Subject"] = subject

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    body = f"An error occurred in the Ford Dealer Comparison application at {timestamp}\n\n{error_message}"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()