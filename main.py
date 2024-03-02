# 3rd Party Pacakges
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import pandas as pd
from pandas.io.formats.style import Styler

# Built-in Packages
import datetime
import logging
import time
from typing import Callable
import sys
import os

# Local Packages
from src.bronco_vehicles import *
from src.bronco_sport_vehicles import *
from src.chassis_cab_vehicles import *
from src.utilities.constants import constants as const
from src.e_series_cutaway_vehicles import *
from src.e_series_stripped_chassis_vehicles import *
from src.e_transit_vehicles import *
from src.edge_vehicles import *
from src.escape_vehicles import *
from src.explorer_vehicles import *
from src.expedition_vehicles import *
from src.f_series_stripped_chassis_vehicles import *
from src.f150_vehicles import *
from src.f150_commercial_vehicles import *
from src.f150_lightening_vehicles import *
from src.f650_f750_vehicles import *
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
# BRONCO_SKIP_FLAG = os.getenv("BRONCO_SKIP_FLAG", "").lower()
# BRONCO_SPORT_SKIP_FLAG = os.getenv("BRONCO_SPORT_SKIP_FLAG", "").lower()
# CHASSIS_CAB_SKIP_FLAG = os.getenv("CHASSIS_CAB_SKIP_FLAG", "").lower()
# E_SERIES_CUTAWAY_SKIP_FLAG = os.getenv("E_SERIES_CUTAWAY_SKIP_FLAG", "").lower()
# E_SERIES_STRIPPED_CHASSIS_SKIP_FLAG = os.getenv("E_SERIES_STRIPPED_CHASSIS_SKIP_FLAG", "").lower()
# E_TRANSIT_SKIP_FLAG = os.getenv("E_TRANSIT_SKIP_FLAG", "").lower()
# EDGE_SKIP_FLAG = os.getenv("EDGE_SKIP_FLAG", "").lower()
# ESCAPE_SKIP_FLAG = os.getenv("ESCAPE_SKIP_FLAG", "").lower()
# EXPLORER_SKIP_FLAG = os.getenv("EXPLORER_SKIP_FLAG", "").lower()
# EXPEDITION_SKIP_FLAG = os.getenv("EXPEDITION_SKIP_FLAG", "").lower()
# F_SERIES_STRIPPED_CHASSIS_SKIP_FLAG = os.getenv("F_SERIES_STRIPPED_CHASSIS_SKIP_FLAG", "").lower()
# F150_SKIP_FLAG = os.getenv("F150_SKIP_FLAG", "").lower()
# F150_COMMERCIAL_SKIP_FLAG = os.getenv("F150_COMMERCIAL_SKIP_FLAG", "").lower()
# F150_LIGHTENING_SKIP_FLAG = os.getenv("F150_LIGHTENING_SKIP_FLAG", "").lower()
# F650_F750_SKIP_FLAG = os.getenv("F650_F750_SKIP_FLAG", "").lower()
# MAVERICK_SKIP_FLAG = os.getenv("MAVERICK_SKIP_FLAG", "").lower()
# MUSTANG_SKIP_FLAG = os.getenv("MUSTANG_SKIP_FLAG", "").lower()
# MUSTANG_MACH_E_SKIP_FLAG = os.getenv("MUSTANG_MACH_E_SKIP_FLAG", "").lower()
# NAVIGATION_SKIP_FLAG = os.getenv("NAVIGATION_SKIP_FLAG", "").lower()
# RANGER_SKIP_FLAG = os.getenv("RANGER_SKIP_FLAG", "").lower()
# SUPER_DUTY_SKIP_FLAG = os.getenv("SUPER_DUTY_SKIP_FLAG", "").lower()
# SUPER_DUTY_COMMERCIAL_SKIP_FLAG = os.getenv("SUPER_DUTY_COMMERCIAL_SKIP_FLAG", "").lower()
# TRANSIT_SKIP_FLAG = os.getenv("TRANSIT_SKIP_FLAG", "").lower()
# TRANSIT_CC_CA_SKIP_FLAG = os.getenv("TRANSIT_CC_CA_SKIP_FLAG", "").lower()
# TRANSIT_COMMERCIAL_SKIP_FLAG = os.getenv("TRANSIT_COMMERCIAL_SKIP_FLAG", "").lower()
# TRANSIT_CONNECT_SKIP_FLAG = os.getenv("TRANSIT_CONNECT_SKIP_FLAG", "").lower()
# TRANSIT_CONNECT_COMMERCIAL_SKIP_FLAG = os.getenv("TRANSIT_CONNECT_COMMERCIAL_SKIP_FLAG", "").lower()

# Initialize variables for Email
sender_email = EMAIL_SENDER
receiver_email = EMAIL_RECIEVER
password = EMAIL_PASSWORD
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

    if skip_flag == False:
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
        print()
    else:
        print(
            f"{vehicle_name} SKIP FLAG is set to 'true'. Skipping {vehicle_name} pricing."
        )
        print()


if __name__ == "__main__":

    try:

        # ---------------------------------
        # Get Navigation Data
        # ---------------------------------

        if const["NAVIGATION_SKIP_FLAG"] == False:
            print("Navigation pricing started...")
            func_start_time = start_timer()

            # Capture Prices
            nav_prices_df = create_navigation_prices_df(
                const["MAIN_NAVIGATION_MENU_MANUFACTURER_URL"], const["MAIN_NAVIGATION_MENU_DEALER_URL"]
            )

            print_elapsed_time(func_start_time, "Navigation pricing completed time")
            print_elapsed_time(start_time, "Elapased Time")
            print("")
        else:
            print("NAVIGATION SKIP FLAG is set to 'true'. Skipping NAVIGATION pricing.")
            print("")

        # ---------------------------------
        # Get vehicle data
        # ---------------------------------

        get_vehicle_data(
            "BRONCO®",
            const["BRONCO_SKIP_FLAG"],
            get_ford_mfg_bronco_prices,
            get_ford_dealer_bronco_prices,
            get_ford_mfg_bronco_hero_img,
            get_ford_dealer_bronco_hero_img,
            const["BRONCO_MANUFACTURER_URL"],
            const["BRONCO_DEALER_URL"],
            const["BRONCO_MANUFACTURER_IMAGE_URL"],
            const["BRONCO_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "BRONCO® SPORT",
            const["BRONCO_SPORT_SKIP_FLAG"],
            get_ford_mfg_bronco_sport_prices,
            get_ford_dealer_bronco_sport_prices,
            get_ford_mfg_bronco_sport_hero_img,
            get_ford_dealer_bronco_sport_hero_img,
            const["BRONCO_SPORT_MANUFACTURER_URL"],
            const["BRONCO_SPORT_DEALER_URL"],
            const["BRONCO_SPORT_MANUFACTURER_IMAGE_URL"],
            const["BRONCO_SPORT_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "CHASSIS CAB",
            const["CHASSIS_CAB_SKIP_FLAG"],
            get_ford_mfg_chassis_cab_prices,
            get_ford_dealer_chassis_cab_prices,
            get_ford_mfg_chassis_cab_hero_img,
            get_ford_dealer_chassis_cab_hero_img,
            const["CHASSIS_CAB_MANUFACTURER_URL"],
            const["CHASSIS_CAB_DEALER_URL"],
            const["CHASSIS_CAB_MANUFACTURER_IMAGE_URL"],
            const["CHASSIS_CAB_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "E-SERIES CUTAWAY",
            const["E_SERIES_CUTAWAY_SKIP_FLAG"],
            get_ford_mfg_e_series_cutaway_prices,
            get_ford_dealer_e_series_cutaway_prices,
            get_ford_mfg_e_series_cutaway_hero_img,
            get_ford_dealer_e_series_cutaway_hero_img,
            const["E_SERIES_CUTAWAY_MANUFACTURER_URL"],
            const["E_SERIES_CUTAWAY_DEALER_URL"],
            const["E_SERIES_CUTAWAY_MANUFACTURER_IMAGE_URL"],
            const["E_SERIES_CUTAWAY_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "E-SERIES STRIPPED CHASSIS",
            const["E_SERIES_STRIPPED_CHASSIS_SKIP_FLAG"],
            get_ford_mfg_e_series_stripped_chassis_prices,
            get_ford_dealer_e_series_stripped_chassis_prices,
            get_ford_mfg_e_series_stripped_chassis_hero_img,
            get_ford_dealer_e_series_stripped_chassis_hero_img,
            const["E_SERIES_STRIPPED_CHASSIS_MANUFACTURER_URL"],
            const["E_SERIES_STRIPPED_CHASSIS_DEALER_URL"],
            const["E_SERIES_STRIPPED_CHASSIS_MANUFACTURER_IMAGE_URL"],
            const["E_SERIES_STRIPPED_CHASSIS_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "E-TRANSIT",
            const["E_TRANSIT_SKIP_FLAG"],
            get_ford_mfg_e_transit_prices,
            get_ford_dealer_e_transit_prices,
            get_ford_mfg_e_transit_hero_img,
            get_ford_dealer_e_transit_hero_img,
            const["E_TRANSIT_MANUFACTURER_URL"],
            const["E_TRANSIT_DEALER_URL"],
            const["E_TRANSIT_MANUFACTURER_IMAGE_URL"],
            const["E_TRANSIT_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "EDGE®",
            const["EDGE_SKIP_FLAG"],
            get_ford_mfg_edge_prices,
            get_ford_dealer_edge_prices,
            get_ford_mfg_edge_hero_img,
            get_ford_dealer_edge_hero_img,
            const["EDGE_MANUFACTURER_URL"],
            const["EDGE_DEALER_URL"],
            const["EDGE_MANUFACTURER_IMAGE_URL"],
            const["EDGE_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "ESCAPE",
            const["ESCAPE_SKIP_FLAG"],
            get_ford_mfg_escape_prices,
            get_ford_dealer_escape_prices,
            get_ford_mfg_escape_hero_img,
            get_ford_dealer_escape_hero_img,
            const["ESCAPE_MANUFACTURER_URL"],
            const["ESCAPE_DEALER_URL"],
            const["ESCAPE_MANUFACTURER_IMAGE_URL"],
            const["ESCAPE_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "EXPLORER®",
            const["EXPLORER_SKIP_FLAG"],
            get_ford_mfg_explorer_prices,
            get_ford_dealer_explorer_prices,
            get_ford_mfg_explorer_hero_img,
            get_ford_dealer_explorer_hero_img,
            const["EXPLORER_MANUFACTURER_URL"],
            const["EXPLORER_DEALER_URL"],
            const["EXPLORER_MANUFACTURER_IMAGE_URL"],
            const["EXPLORER_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "EXPEDITION®",
            const["EXPEDITION_SKIP_FLAG"],
            get_ford_mfg_expedition_prices,
            get_ford_dealer_expedition_prices,
            get_ford_mfg_expedition_hero_img,
            get_ford_dealer_expedition_hero_img,
            const["EXPEDITION_MANUFACTURER_URL"],
            const["EXPEDITION_DEALER_URL"],
            const["EXPEDITION_MANUFACTURER_IMAGE_URL"],
            const["EXPEDITION_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "F-SERIES STRIPPED CHASSIS",
            const["F_SERIES_STRIPPED_CHASSIS_SKIP_FLAG"],
            get_ford_mfg_f_series_stripped_chassis_prices,
            get_ford_dealer_f_series_stripped_chassis_prices,
            get_ford_mfg_f_series_stripped_chassis_hero_img,
            get_ford_dealer_f_series_stripped_chassis_hero_img,
            const["F_SERIES_STRIPPED_CHASSIS_MANUFACTURER_URL"],
            const["F_SERIES_STRIPPED_CHASSIS_DEALER_URL"],
            const["F_SERIES_STRIPPED_CHASSIS_MANUFACTURER_IMAGE_URL"],
            const["F_SERIES_STRIPPED_CHASSIS_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "F-150®",
            const["F150_SKIP_FLAG"],
            get_ford_mfg_f150_prices,
            get_ford_dealer_f150_prices,
            get_ford_mfg_f150_hero_img,
            get_ford_dealer_f150_hero_img,
            const["F150_MANUFACTURER_URL"],
            const["F150_DEALER_URL"],
            const["F150_MANUFACTURER_IMAGE_URL"],
            const["F150_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "F-150® COMMERICAL",
            const["F150_COMMERCIAL_SKIP_FLAG"],
            get_ford_mfg_f150_commercial_prices,
            get_ford_dealer_f150_commercial_prices,
            get_ford_mfg_f150_commercial_hero_img,
            get_ford_dealer_f150_commercial_hero_img,
            const["F150_COMMERCIAL_MANUFACTURER_URL"],
            const["F150_COMMERCIAL_DEALER_URL"],
            const["F150_COMMERCIAL_MANUFACTURER_IMAGE_URL"],
            const["F150_COMMERCIAL_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "F-150® LIGHTENING®",
            const["F150_LIGHTENING_SKIP_FLAG"],
            get_ford_mfg_f150_lightening_prices,
            get_ford_dealer_f150_lightening_prices,
            get_ford_mfg_f150_lightening_hero_img,
            get_ford_dealer_f150_lightening_hero_img,
            const["F150_LIGHTENING_MANUFACTURER_URL"],
            const["F150_LIGHTENING_DEALER_URL"],
            const["F150_LIGHTENING_MANUFACTURER_IMAGE_URL"],
            const["F150_LIGHTENING_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "F-650® F-750®",
            const["F650_F750_SKIP_FLAG"],
            get_ford_mfg_f650_f750_prices,
            get_ford_dealer_f650_f750_prices,
            get_ford_mfg_f650_f750_hero_img,
            get_ford_dealer_f650_f750_hero_img,
            const["F650_F750_MANUFACTURER_URL"],
            const["F650_F750_DEALER_URL"],
            const["F650_F750_MANUFACTURER_IMAGE_URL"],
            const["F650_F750_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "MAVERICK®",
            const["MAVERICK_SKIP_FLAG"],
            get_ford_mfg_maverick_prices,
            get_ford_dealer_maverick_prices,
            get_ford_mfg_maverick_hero_img,
            get_ford_dealer_maverick_hero_img,
            const["MAVERICK_MANUFACTURER_URL"],
            const["MAVERICK_DEALER_URL"],
            const["MAVERICK_MANUFACTURER_IMAGE_URL"],
            const["MAVERICK_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "MUSTANG®",
            const["MUSTANG_SKIP_FLAG"],
            get_ford_mfg_mustang_prices,
            get_ford_dealer_mustang_prices,
            get_ford_mfg_mustang_hero_img,
            get_ford_dealer_mustang_hero_img,
            const["MUSTANG_MANUFACTURER_URL"],
            const["MUSTANG_DEALER_URL"],
            const["MUSTANG_MANUFACTURER_IMAGE_URL"],
            const["MUSTANG_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "MUSTANG MACH-E®",
            const["MUSTANG_MACH_E_SKIP_FLAG"],
            get_ford_mfg_mustang_mach_e_prices,
            get_ford_dealer_mustang_mach_e_prices,
            get_ford_mfg_mustang_mach_e_hero_img,
            get_ford_dealer_mustang_mach_e_hero_img,
            const["MUSTANG_MACH_E_MANUFACTURER_URL"],
            const["MUSTANG_MACH_E_DEALER_URL"],
            const["MUSTANG_MACH_E_MANUFACTURER_IMAGE_URL"],
            const["MUSTANG_MACH_E_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "RANGER®",
            const["RANGER_SKIP_FLAG"],
            get_ford_mfg_ranger_prices,
            get_ford_dealer_ranger_prices,
            get_ford_mfg_ranger_hero_img,
            get_ford_dealer_ranger_hero_img,
            const["RANGER_MANUFACTURER_URL"],
            const["RANGER_DEALER_URL"],
            const["RANGER_MANUFACTURER_IMAGE_URL"],
            const["RANGER_DEALER_IMAGE_URL"],
        )
        
        get_vehicle_data(
            "SUPER DUTY®",
            const["SUPER_DUTY_SKIP_FLAG"],
            get_ford_mfg_super_duty_prices,
            get_ford_dealer_super_duty_prices,
            get_ford_mfg_super_duty_hero_img,
            get_ford_dealer_super_duty_hero_img,
            const["SUPER_DUTY_MANUFACTURER_URL"],
            const["SUPER_DUTY_DEALER_URL"],
            const["SUPER_DUTY_MANUFACTURER_IMAGE_URL"],
            const["SUPER_DUTY_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "SUPER DUTY® COMMERICAL",
            const["SUPER_DUTY_COMMERCIAL_SKIP_FLAG"],
            get_ford_mfg_super_duty_commercial_prices,
            get_ford_dealer_super_duty_commercial_prices,
            get_ford_mfg_super_duty_commercial_hero_img,
            get_ford_dealer_super_duty_commercial_hero_img,
            const["SUPER_DUTY_COMMERCIAL_MANUFACTURER_URL"],
            const["SUPER_DUTY_COMMERCIAL_DEALER_URL"],
            const["SUPER_DUTY_COMMERCIAL_MANUFACTURER_IMAGE_URL"],
            const["SUPER_DUTY_COMMERCIAL_DEALER_IMAGE_URL"],
        )
        
        get_vehicle_data(
            "TRANSIT®",
            const["TRANSIT_SKIP_FLAG"],
            get_ford_mfg_transit_prices,
            get_ford_dealer_transit_prices,
            get_ford_mfg_transit_hero_img,
            get_ford_dealer_transit_hero_img,
            const["TRANSIT_MANUFACTURER_URL"],
            const["TRANSIT_DEALER_URL"],
            const["TRANSIT_MANUFACTURER_IMAGE_URL"],
            const["TRANSIT_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "TRANSIT® CC-CA",
            const["TRANSIT_CC_CA_SKIP_FLAG"],
            get_ford_mfg_transit_cc_ca_prices,
            get_ford_dealer_transit_cc_ca_prices,
            get_ford_mfg_transit_cc_ca_hero_img,
            get_ford_dealer_transit_cc_ca_hero_img,
            const["TRANSIT_CC_CA_MANUFACTURER_URL"],
            const["TRANSIT_CC_CA_DEALER_URL"],
            const["TRANSIT_CC_CA_MANUFACTURER_IMAGE_URL"],
            const["TRANSIT_CC_CA_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "TRANSIT® COMMERCIAL",
            const["TRANSIT_COMMERCIAL_SKIP_FLAG"],
            get_ford_mfg_transit_commercial_prices,
            get_ford_dealer_transit_commercial_prices,
            get_ford_mfg_transit_commercial_hero_img,
            get_ford_dealer_transit_commercial_hero_img,
            const["TRANSIT_COMMERCIAL_MANUFACTURER_URL"],
            const["TRANSIT_COMMERCIAL_DEALER_URL"],
            const["TRANSIT_COMMERCIAL_MANUFACTURER_IMAGE_URL"],
            const["TRANSIT_COMMERCIAL_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "TRANSIT® CONNECT",
            const["TRANSIT_CONNECT_SKIP_FLAG"],
            get_ford_mfg_transit_connect_prices,
            get_ford_dealer_transit_connect_prices,
            get_ford_mfg_transit_connect_hero_img,
            get_ford_dealer_transit_connect_hero_img,
            const["TRANSIT_CONNECT_MANUFACTURER_URL"],
            const["TRANSIT_CONNECT_DEALER_URL"],
            const["TRANSIT_CONNECT_MANUFACTURER_IMAGE_URL"],
            const["TRANSIT_CONNECT_DEALER_IMAGE_URL"],
        )

        get_vehicle_data(
            "TRANSIT® CONNECT COMMERCIAL",
            const["TRANSIT_CONNECT_COMMERCIAL_SKIP_FLAG"],
            get_ford_mfg_transit_connect_commercial_prices,
            get_ford_dealer_transit_connect_commercial_prices,
            get_ford_mfg_transit_connect_commercial_hero_img,
            get_ford_dealer_transit_connect_commercial_hero_img,
            const["TRANSIT_CONNECT_COMMERCIAL_MANUFACTURER_URL"],
            const["TRANSIT_CONNECT_COMMERCIAL_DEALER_URL"],
            const["TRANSIT_CONNECT_COMMERCIAL_MANUFACTURER_IMAGE_URL"],
            const["TRANSIT_CONNECT_COMMERCIAL_DEALER_IMAGE_URL"],
        )

        # Close Webdriver
        driver = WebDriverSingleton.get_driver()
        driver.quit()

        # Email the data
        if const["EMAIL_SKIP_FLAG"] == False:
            send_dealer_email(sender_email, receiver_email, password, "Ford Vehicle Prices and Image Comparison", vehicles_list_html, all_model_images_df, nav_prices_df)
        else:
            print("EMAIL SKIP FLAG is set to 'true'. Email not sent.")
            print()

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

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        filename = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        error_message = f"{exc_type.__name__} at {filename}\nline: {line_number}\n{str(e)}"
        logging.error(error_message)
        send_error_email(sender_email, os.getenv("EMAIL_ERROR_RECIEVER"), password, "FAILED: Ford Vehicle Prices and Image Comparison", error_message)