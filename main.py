# 3rd Party Pacakges
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import matplotlib.pyplot as plt
import pandas as pd
from pandas.io.formats.style import Styler

# Built-in Packages
import datetime
import time
from typing import Callable
import sys
import smtplib
import os

# Local Packages
from src.bronco_vehicles import *
from src.bronco_sport_vehicles import *
from src.e_series_cutaway_vehicles import *
from src.e_transit_vehicles import *
from src.edge_vehicles import *
from src.escape_vehicles import *
from src.explorer_vehicles import *
from src.expedition_vehicles import *
from src.f150_vehicles import *
from src.f150_commercial_vehicles import *
from src.f150_lightening_vehicles import *
from src.maverick_vehicles import *
from src.mustang_vehicles import *
from src.mustang_mach_e_vehicles import *
from src.ranger_vehicles import *
from src.super_duty_vehicles import *
from src.super_duty_commercial_vehicles import *
from src.transit_vehicles import *
from src.transit_cc_ca_vehicles import *
from src.transit_commercial_vehicles import *
from src.transit_connect_vehicles import *
from src.transit_connect_commercial_vehicles import *
from src.navigation_menu import *
from src.utilities.utilities import *

# Load environment variables from the .env file
load_dotenv(override=True)

# Record the start time
start_time = start_timer()

# Get email configuration from environment variables
EMAIL_RECIEVER = os.getenv("EMAIL_RECIEVER")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Get skip flags from environment variables
BRONCO_SKIP_FLAG = os.getenv("BRONCO_SKIP_FLAG", "").lower()
BRONCO_SPORT_SKIP_FLAG = os.getenv("BRONCO_SPORT_SKIP_FLAG", "").lower()
E_SERIES_CUTAWAY_SKIP_FLAG = os.getenv("E_SERIES_CUTAWAY_SKIP_FLAG", "").lower()
E_TRANSIT_SKIP_FLAG = os.getenv("E_TRANSIT_SKIP_FLAG", "").lower()
EDGE_SKIP_FLAG = os.getenv("EDGE_SKIP_FLAG", "").lower()
ESCAPE_SKIP_FLAG = os.getenv("ESCAPE_SKIP_FLAG", "").lower()
EXPLORER_SKIP_FLAG = os.getenv("EXPLORER_SKIP_FLAG", "").lower()
EXPEDITION_SKIP_FLAG = os.getenv("EXPEDITION_SKIP_FLAG", "").lower()
F150_SKIP_FLAG = os.getenv("F150_SKIP_FLAG", "").lower()
F150_COMMERCIAL_SKIP_FLAG = os.getenv("F150_SKIP_FLAG", "").lower()
F150_LIGHTENING_SKIP_FLAG = os.getenv("F150_LIGHTENING_SKIP_FLAG", "").lower()
MAVERICK_SKIP_FLAG = os.getenv("MAVERICK_SKIP_FLAG", "").lower()
MUSTANG_SKIP_FLAG = os.getenv("MUSTANG_SKIP_FLAG", "").lower()
MUSTANG_MACH_E_SKIP_FLAG = os.getenv("MUSTANG_MACH_E_SKIP_FLAG", "").lower()
NAVIGATION_SKIP_FLAG = os.getenv("NAVIGATION_SKIP_FLAG", "").lower()
RANGER_SKIP_FLAG = os.getenv("RANGER_SKIP_FLAG", "").lower()
SUPER_DUTY_SKIP_FLAG = os.getenv("SUPER_DUTY_SKIP_FLAG", "").lower()
SUPER_DUTY_COMMERCIAL_SKIP_FLAG = os.getenv("SUPER_DUTY_COMMERCIAL_SKIP_FLAG", "").lower()
TRANSIT_SKIP_FLAG = os.getenv("TRANSIT_SKIP_FLAG", "").lower()
TRANSIT_CC_CA_SKIP_FLAG = os.getenv("TRANSIT_CC_CA_SKIP_FLAG", "").lower()
TRANSIT_COMMERCIAL_SKIP_FLAG = os.getenv("TRANSIT_COMMERCIAL_SKIP_FLAG", "").lower()
TRANSIT_CONNECT_SKIP_FLAG = os.getenv("TRANSIT_CONNECT_SKIP_FLAG", "").lower()
TRANSIT_CONNECT_COMMERCIAL_SKIP_FLAG = os.getenv("TRANSIT_CONNECT_COMMERCIAL_SKIP_FLAG", "").lower()

# Initialize variables for Email
vehicles_list_html = []
all_model_images_df = pd.DataFrame()


# Process Vehicle data
def get_vehicle_data(
    vehicle_name: str,
    skip_flag: str,
    mfg_prices_func: Callable,
    dealer_prices_func: Callable,
    mfg_image_func: Callable,
    dealer_image_func: Callable,
    mfg_price_url: str,
    dealer_price_url: str,
    mfg_image_url: str,
    dealer_image_url: str,
) -> None:
    global all_model_images_df

    if skip_flag == "false":
        print(f"{vehicle_name} pricing scraping started...")

        func_start_time = start_timer()

        # Capture Prices
        vehicle_prices_df = create_vehicle_prices_df(
            mfg_prices_func, dealer_prices_func, mfg_price_url, dealer_price_url
        )

        print(f"{vehicle_name} pricing scraping completed.")
        print(f"{vehicle_name} image scraping started...")

        # Capture Hero Images
        vehicle_image_df = create_vehicle_image_df(
            mfg_image_func,
            dealer_image_func,
            vehicle_name,
            mfg_image_url,
            dealer_image_url,
        )

        print(f"{vehicle_name} image scraping completed.")

        # Append Prices to single list
        vehicles_list_html.append(
            (vehicle_name, vehicle_prices_df, mfg_image_url, dealer_image_url)
        )

        # Append Images to single data frame
        all_model_images_df = pd.concat(
            [all_model_images_df, vehicle_image_df], ignore_index=True
        )

        print_elapsed_time(
            func_start_time, f"{vehicle_name} pricing and image scraping completed time"
        )
        print_elapsed_time(start_time, "Elapased Time")
        print("")
    else:
        print(
            f"{vehicle_name} SKIP FLAG is set to 'true'. Skipping {vehicle_name} pricing."
        )
        print("")


if __name__ == "__main__":

    # ---------------------------------
    # Get Navigation Data
    # ---------------------------------

    if NAVIGATION_SKIP_FLAG == "false":
        print("Navigation pricing started...")
        func_start_time = start_timer()

        # Capture Prices
        nav_prices_df = create_navigation_prices_df(
            MAIN_NAVIGATION_MENU_MANUFACTURER_URL, MAIN_NAVIGATION_MENU_DEALER_URL
        )

        print_elapsed_time(func_start_time, "Navigation pricing completed time")
        print_elapsed_time(start_time, "Elapased Time")
        print("")
    else:
        print("NAVIGATION_SKIP_FLAG is set to 'true'. Skipping NAVIGATION pricing.")
        print("")

    # ---------------------------------
    # Get vehicle data
    # ---------------------------------

    get_vehicle_data(
        "BRONCO®",
        BRONCO_SKIP_FLAG,
        get_ford_mfg_bronco_prices,
        get_ford_dealer_bronco_prices,
        get_ford_mfg_bronco_hero_img,
        get_ford_dealer_bronco_hero_img,
        BRONCO_MANUFACTURER_URL,
        BRONCO_DEALER_URL,
        BRONCO_MANUFACTURER_IMAGE_URL,
        BRONCO_DEALER_IMAGE_URL,
    )

    get_vehicle_data(
        "BRONCO® SPORT",
        BRONCO_SPORT_SKIP_FLAG,
        get_ford_mfg_bronco_sport_prices,
        get_ford_dealer_bronco_sport_prices,
        get_ford_mfg_bronco_sport_hero_img,
        get_ford_dealer_bronco_sport_hero_img,
        BRONCO_SPORT_MANUFACTURER_URL,
        BRONCO_SPORT_DEALER_URL,
        BRONCO_SPORT_MANUFACTURER_IMAGE_URL,
        BRONCO_SPORT_DEALER_IMAGE_URL,
    )

    get_vehicle_data(
        "E-SERIES CUTAWAY",
        E_SERIES_CUTAWAY_SKIP_FLAG,
        get_ford_mfg_e_series_cutaway_prices,
        get_ford_dealer_e_series_cutaway_prices,
        get_ford_mfg_e_series_cutaway_hero_img,
        get_ford_dealer_e_series_cutaway_hero_img,
        E_SERIES_CUTAWAY_MANUFACTURER_URL,
        E_SERIES_CUTAWAY_DEALER_URL,
        E_SERIES_CUTAWAY_MANUFACTURER_IMAGE_URL,
        E_SERIES_CUTAWAY_DEALER_IMAGE_URL,
    )

    get_vehicle_data(
        "E-TRANSIT",
        E_TRANSIT_SKIP_FLAG,
        get_ford_mfg_e_transit_prices,
        get_ford_dealer_e_transit_prices,
        get_ford_mfg_e_transit_hero_img,
        get_ford_dealer_e_transit_hero_img,
        E_TRANSIT_MANUFACTURER_URL,
        E_TRANSIT_DEALER_URL,
        E_TRANSIT_MANUFACTURER_IMAGE_URL,
        E_TRANSIT_DEALER_IMAGE_URL,
    )

    get_vehicle_data(
        "EDGE®",
        EDGE_SKIP_FLAG,
        get_ford_mfg_edge_prices,
        get_ford_dealer_edge_prices,
        get_ford_mfg_edge_hero_img,
        get_ford_dealer_edge_hero_img,
        EDGE_MANUFACTURER_URL,
        EDGE_DEALER_URL,
        EDGE_MANUFACTURER_IMAGE_URL,
        EDGE_DEALER_IMAGE_URL,
    )

    get_vehicle_data(
        "ESCAPE",
        ESCAPE_SKIP_FLAG,
        get_ford_mfg_escape_prices,
        get_ford_dealer_escape_prices,
        get_ford_mfg_escape_hero_img,
        get_ford_dealer_escape_hero_img,
        ESCAPE_MANUFACTURER_URL,
        ESCAPE_DEALER_URL,
        ESCAPE_MANUFACTURER_IMAGE_URL,
        ESCAPE_DEALER_IMAGE_URL,
    )

    get_vehicle_data(
        "EXPLORER®",
        EXPLORER_SKIP_FLAG,
        get_ford_mfg_explorer_prices,
        get_ford_dealer_explorer_prices,
        get_ford_mfg_explorer_hero_img,
        get_ford_dealer_explorer_hero_img,
        EXPLORER_MANUFACTURER_URL,
        EXPLORER_DEALER_URL,
        EXPLORER_MANUFACTURER_IMAGE_URL,
        EXPLORER_DEALER_IMAGE_URL,
    )

    get_vehicle_data(
        "EXPEDITION®",
        EXPEDITION_SKIP_FLAG,
        get_ford_mfg_expedition_prices,
        get_ford_dealer_expedition_prices,
        get_ford_mfg_expedition_hero_img,
        get_ford_dealer_expedition_hero_img,
        EXPEDITION_MANUFACTURER_URL,
        EXPEDITION_DEALER_URL,
        EXPEDITION_MANUFACTURER_IMAGE_URL,
        EXPEDITION_DEALER_IMAGE_URL,
    )

    get_vehicle_data(
        "F-150®",
        F150_SKIP_FLAG,
        get_ford_mfg_f150_prices,
        get_ford_dealer_f150_prices,
        get_ford_mfg_f150_hero_img,
        get_ford_dealer_f150_hero_img,
        F150_MANUFACTURER_URL,
        F150_DEALER_URL,
        F150_MANUFACTURER_IMAGE_URL,
        F150_DEALER_IMAGE_URL,
    )

    get_vehicle_data(
        "F-150® COMMERICAL",
        F150_COMMERCIAL_SKIP_FLAG,
        get_ford_mfg_f150_commercial_prices,
        get_ford_dealer_f150_commercial_prices,
        get_ford_mfg_f150_commercial_hero_img,
        get_ford_dealer_f150_commercial_hero_img,
        F150_COMMERCIAL_MANUFACTURER_URL,
        F150_COMMERCIAL_DEALER_URL,
        F150_COMMERCIAL_MANUFACTURER_IMAGE_URL,
        F150_COMMERCIAL_DEALER_IMAGE_URL,
    )

    get_vehicle_data(
        "F-150® LIGHTENING®",
        F150_LIGHTENING_SKIP_FLAG,
        get_ford_mfg_f150_lightening_prices,
        get_ford_dealer_f150_lightening_prices,
        get_ford_mfg_f150_lightening_hero_img,
        get_ford_dealer_f150_lightening_hero_img,
        F150_LIGHTENING_MANUFACTURER_URL,
        F150_LIGHTENING_DEALER_URL,
        F150_LIGHTENING_MANUFACTURER_IMAGE_URL,
        F150_LIGHTENING_DEALER_IMAGE_URL,
    )

    get_vehicle_data(
        "MAVERICK®",
        MAVERICK_SKIP_FLAG,
        get_ford_mfg_maverick_prices,
        get_ford_dealer_maverick_prices,
        get_ford_mfg_maverick_hero_img,
        get_ford_dealer_maverick_hero_img,
        MAVERICK_MANUFACTURER_URL,
        MAVERICK_DEALER_URL,
        MAVERICK_MANUFACTURER_IMAGE_URL,
        MAVERICK_DEALER_IMAGE_URL,
    )

    get_vehicle_data(
        "MUSTANG®",
        MUSTANG_SKIP_FLAG,
        get_ford_mfg_mustang_prices,
        get_ford_dealer_mustang_prices,
        get_ford_mfg_mustang_hero_img,
        get_ford_dealer_mustang_hero_img,
        MUSTANG_MANUFACTURER_URL,
        MUSTANG_DEALER_URL,
        MUSTANG_MANUFACTURER_IMAGE_URL,
        MUSTANG_DEALER_IMAGE_URL,
    )

    get_vehicle_data(
        "MUSTANG MACH-E®",
        MUSTANG_MACH_E_SKIP_FLAG,
        get_ford_mfg_mustang_mach_e_prices,
        get_ford_dealer_mustang_mach_e_prices,
        get_ford_mfg_mustang_mach_e_hero_img,
        get_ford_dealer_mustang_mach_e_hero_img,
        MUSTANG_MACH_E_MANUFACTURER_URL,
        MUSTANG_MACH_E_DEALER_URL,
        MUSTANG_MACH_E_MANUFACTURER_IMAGE_URL,
        MUSTANG_MACH_E_DEALER_IMAGE_URL,
    )

    get_vehicle_data(
        "RANGER®",
        RANGER_SKIP_FLAG,
        get_ford_mfg_ranger_prices,
        get_ford_dealer_ranger_prices,
        get_ford_mfg_ranger_hero_img,
        get_ford_dealer_ranger_hero_img,
        RANGER_MANUFACTURER_URL,
        RANGER_DEALER_URL,
        RANGER_MANUFACTURER_IMAGE_URL,
        RANGER_DEALER_IMAGE_URL,
    )
    
    get_vehicle_data(
        "SUPER DUTY®",
        SUPER_DUTY_SKIP_FLAG,
        get_ford_mfg_super_duty_prices,
        get_ford_dealer_super_duty_prices,
        get_ford_mfg_super_duty_hero_img,
        get_ford_dealer_super_duty_hero_img,
        SUPER_DUTY_MANUFACTURER_URL,
        SUPER_DUTY_DEALER_URL,
        SUPER_DUTY_MANUFACTURER_IMAGE_URL,
        SUPER_DUTY_DEALER_IMAGE_URL,
    )

    get_vehicle_data(
        "SUPER DUTY® COMMERICAL",
        SUPER_DUTY_COMMERCIAL_SKIP_FLAG,
        get_ford_mfg_super_duty_commercial_prices,
        get_ford_dealer_super_duty_commercial_prices,
        get_ford_mfg_super_duty_commercial_hero_img,
        get_ford_dealer_super_duty_commercial_hero_img,
        SUPER_DUTY_COMMERCIAL_MANUFACTURER_URL,
        SUPER_DUTY_COMMERCIAL_DEALER_URL,
        SUPER_DUTY_COMMERCIAL_MANUFACTURER_IMAGE_URL,
        SUPER_DUTY_COMMERCIAL_DEALER_IMAGE_URL,
    )
    
    get_vehicle_data(
        "TRANSIT®",
        TRANSIT_SKIP_FLAG,
        get_ford_mfg_transit_prices,
        get_ford_dealer_transit_prices,
        get_ford_mfg_transit_hero_img,
        get_ford_dealer_transit_hero_img,
        TRANSIT_MANUFACTURER_URL,
        TRANSIT_DEALER_URL,
        TRANSIT_MANUFACTURER_IMAGE_URL,
        TRANSIT_DEALER_IMAGE_URL,
    )

    get_vehicle_data(
        "TRANSIT® CC-CA",
        TRANSIT_CC_CA_SKIP_FLAG,
        get_ford_mfg_transit_cc_ca_prices,
        get_ford_dealer_transit_cc_ca_prices,
        get_ford_mfg_transit_cc_ca_hero_img,
        get_ford_dealer_transit_cc_ca_hero_img,
        TRANSIT_CC_CA_MANUFACTURER_URL,
        TRANSIT_CC_CA_DEALER_URL,
        TRANSIT_CC_CA_MANUFACTURER_IMAGE_URL,
        TRANSIT_CC_CA_DEALER_IMAGE_URL,
    )

    get_vehicle_data(
        "TRANSIT® COMMERCIAL",
        TRANSIT_COMMERCIAL_SKIP_FLAG,
        get_ford_mfg_transit_commercial_prices,
        get_ford_dealer_transit_commercial_prices,
        get_ford_mfg_transit_commercial_hero_img,
        get_ford_dealer_transit_commercial_hero_img,
        TRANSIT_COMMERCIAL_MANUFACTURER_URL,
        TRANSIT_COMMERCIAL_DEALER_URL,
        TRANSIT_COMMERCIAL_MANUFACTURER_IMAGE_URL,
        TRANSIT_COMMERCIAL_DEALER_IMAGE_URL,
    )

    get_vehicle_data(
        "TRANSIT® CONNECT",
        TRANSIT_CONNECT_SKIP_FLAG,
        get_ford_mfg_transit_connect_prices,
        get_ford_dealer_transit_connect_prices,
        get_ford_mfg_transit_connect_hero_img,
        get_ford_dealer_transit_connect_hero_img,
        TRANSIT_CONNECT_MANUFACTURER_URL,
        TRANSIT_CONNECT_DEALER_URL,
        TRANSIT_CONNECT_MANUFACTURER_IMAGE_URL,
        TRANSIT_CONNECT_DEALER_IMAGE_URL,
    )

    get_vehicle_data(
        "TRANSIT® CONNECT COMMERCIAL",
        TRANSIT_CONNECT_COMMERCIAL_SKIP_FLAG,
        get_ford_mfg_transit_connect_commercial_prices,
        get_ford_dealer_transit_connect_commercial_prices,
        get_ford_mfg_transit_connect_commercial_hero_img,
        get_ford_dealer_transit_connect_commercial_hero_img,
        TRANSIT_CONNECT_COMMERCIAL_MANUFACTURER_URL,
        TRANSIT_CONNECT_COMMERCIAL_DEALER_URL,
        TRANSIT_CONNECT_COMMERCIAL_MANUFACTURER_IMAGE_URL,
        TRANSIT_CONNECT_COMMERCIAL_DEALER_IMAGE_URL,
    )

    # Close Webdriver
    driver = WebDriverSingleton.get_driver()
    driver.quit()

    # Email configuration
    sender_email = EMAIL_SENDER
    receiver_email = EMAIL_RECIEVER
    password = EMAIL_PASSWORD

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
    msg["Subject"] = "Ford Vehicle Prices and Image Comparison"

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
          <li>{MAIN_NAVIGATION_MENU_MANUFACTURER_URL}</li>
          <li>{MAIN_NAVIGATION_MENU_DEALER_URL}</li>
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

    # Record the end time
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time_seconds = end_time - start_time

    # Convert elapsed time to hours, minutes, and seconds
    hours, remainder = divmod(elapsed_time_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Print the elapsed time
    print(
        f"Script execution time: {int(hours)} hours, {int(minutes)} minutes, {seconds:.2f} seconds"
    )
