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
import sys
import smtplib
import os

# Local Packages
from src.bronco_vehicles import *
from src.bronco_sport_vehicles import *
from src.edge_vehicles import *
from src.escape_vehicles import *
from src.explorer_vehicles import *
from src.f150_vehicles import *
from src.f150_lightening_vehicles import *
from src.mustang_vehicles import *
from src.mustang_mach_e_vehicles import *
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
EDGE_SKIP_FLAG = os.getenv("EDGE_SKIP_FLAG", "").lower()
ESCAPE_SKIP_FLAG = os.getenv("ESCAPE_SKIP_FLAG", "").lower()
EXPLORER_SKIP_FLAG = os.getenv("EXPLORER_SKIP_FLAG", "").lower()
F150_SKIP_FLAG = os.getenv("F150_SKIP_FLAG", "").lower()
F150_LIGHTENING_SKIP_FLAG = os.getenv("F150_LIGHTENING_SKIP_FLAG", "").lower()
MUSTANG_SKIP_FLAG = os.getenv("MUSTANG_SKIP_FLAG", "").lower()
MUSTANG_MACH_E_SKIP_FLAG = os.getenv("MUSTANG_MACH_E_SKIP_FLAG", "").lower()
NAVIGATION_SKIP_FLAG = os.getenv("NAVIGATION_SKIP_FLAG", "").lower()

# Initialize variables for Email
vehicles_list_html = []
all_model_images_df = pd.DataFrame()


# ---------------------------------
# Get Navigation Data
# ---------------------------------

if NAVIGATION_SKIP_FLAG == "false":
    print("Navigation pricing started...")
    func_start_time = start_timer()

    # Capture Prices
    nav_prices_df = create_navigation_prices_df()

    print_elapsed_time(func_start_time, "Navigation pricing completed time")
    print_elapsed_time(start_time, "Elapased Time")
else:
    print("NAVIGATION_SKIP_FLAG is set to 'true'. Skipping NAVIGATION pricing.")

# ---------------------------------
# Get Bronco Data
# ---------------------------------

if BRONCO_SKIP_FLAG == "false":
    print("Bronco pricing started...")
    func_start_time = start_timer()

    # Capture Prices
    bronco_prices_df = create_vehicle_prices_df(
        get_ford_mfg_bronco_prices(), get_ford_dealer_bronco_prices()
    )

    # Capture Hero Images
    bronco_image_df = create_vehicle_image_df(
        get_ford_mfg_bronco_hero_img(),
        get_ford_dealer_bronco_hero_img(),
        "Bronco®",
        BRONCO_MANUFACTURER_IMAGE_URL,
        BRONCO_DEALER_IMAGE_URL,
    )

    # Append Prices to single list
    vehicles_list_html.append(
        ("BRONCO®", bronco_prices_df, BRONCO_MANUFACTURER_URL, BRONCO_DEALER_URL)
    )

    # Append Images to single data frame
    all_model_images_df = pd.concat(
        [all_model_images_df, bronco_image_df], ignore_index=True
    )

    print_elapsed_time(func_start_time, "Bronco pricing completed time")
    print_elapsed_time(start_time, "Elapased Time")
else:
    print("BRONCO_SKIP_FLAG is set to 'true'. Skipping BRONCO pricing.")

# ---------------------------------
# Get Bronco Sport Data
# ---------------------------------

if BRONCO_SPORT_SKIP_FLAG == "false":
    print("Bronco Sport pricing started...")
    func_start_time = start_timer()

    # Capture Prices
    bronco_sport_prices_df = create_vehicle_prices_df(
        get_ford_mfg_bronco_sport_prices(), get_ford_dealer_bronco_sport_prices()
    )

    # Capture Hero Images
    bronco_sport_image_df = create_vehicle_image_df(
        get_ford_mfg_bronco_sport_hero_img(),
        get_ford_dealer_bronco_sport_hero_img(),
        "Bronco® Sport",
        BRONCO_SPORT_MANUFACTURER_IMAGE_URL,
        BRONCO_SPORT_DEALER_IMAGE_URL,
    )

    # Append Prices to single list
    vehicles_list_html.append(
        (
            "BRONCO® SPORT",
            bronco_sport_prices_df,
            BRONCO_SPORT_MANUFACTURER_URL,
            BRONCO_SPORT_DEALER_URL,
        )
    )

    # Append Images to single data frame
    all_model_images_df = pd.concat(
        [all_model_images_df, bronco_sport_image_df], ignore_index=True
    )

    print_elapsed_time(func_start_time, "Bronco Sport pricing completed time")
    print_elapsed_time(start_time, "Elapased Time")
else:
    print("BRONCO_SPORT_SKIP_FLAG is set to 'true'. Skipping BRONCO SPORT pricing.")

# ---------------------------------
# Get Edge Data
# ---------------------------------

if EDGE_SKIP_FLAG == "false":
    print("Edge pricing started...")
    func_start_time = start_timer()

    # Capture Prices
    edge_prices_df = create_vehicle_prices_df(
        get_ford_mfg_edge_prices(), get_ford_dealer_edge_prices()
    )

    # Capture Hero Images
    edge_image_df = create_vehicle_image_df(
        get_ford_mfg_edge_hero_img(),
        get_ford_dealer_edge_hero_img(),
        "Edge®",
        EDGE_MANUFACTURER_IMAGE_URL,
        EDGE_DEALER_IMAGE_URL,
    )

    # Append Prices to single list
    vehicles_list_html.append(
        (
            "EDGE®",
            edge_prices_df,
            EDGE_MANUFACTURER_URL,
            EDGE_DEALER_URL,
        )
    )

    # Append Images to single data frame
    all_model_images_df = pd.concat(
        [all_model_images_df, edge_image_df], ignore_index=True
    )

    print_elapsed_time(func_start_time, "Edge Sport pricing completed time")
    print_elapsed_time(start_time, "Elapased Time")
else:
    print("EDGE_SKIP_FLAG is set to 'true'. Skipping Edge pricing.")

# ---------------------------------
# Get Escape Data
# ---------------------------------

if ESCAPE_SKIP_FLAG == "false":
    print("Escape pricing started...")
    func_start_time = start_timer()

    # Capture Prices
    escape_prices_df = create_vehicle_prices_df(
        get_ford_mfg_escape_prices(), get_ford_dealer_escape_prices()
    )

    # Capture Hero Images
    escape_image_df = create_vehicle_image_df(
        get_ford_mfg_escape_hero_img(),
        get_ford_dealer_escape_hero_img(),
        "Escape",
        ESCAPE_MANUFACTURER_IMAGE_URL,
        ESCAPE_DEALER_IMAGE_URL,
    )

    # Append Prices to single list
    vehicles_list_html.append(
        (
            "ESCAPE",
            escape_prices_df,
            ESCAPE_MANUFACTURER_URL,
            ESCAPE_DEALER_URL,
        )
    )

    # Append Images to single data frame
    all_model_images_df = pd.concat(
        [all_model_images_df, escape_image_df], ignore_index=True
    )

    print_elapsed_time(func_start_time, "Escape Sport pricing completed time")
    print_elapsed_time(start_time, "Elapased Time")
else:
    print("ESCAPE_SKIP_FLAG is set to 'true'. Skipping Escape pricing.")

# ---------------------------------
# Get Explorer Data
# ---------------------------------

if EXPLORER_SKIP_FLAG == "false":
    print("Explorer pricing started...")
    func_start_time = start_timer()

    # Capture Prices
    explorer_prices_df = create_vehicle_prices_df(
        get_ford_mfg_explorer_prices(), get_ford_dealer_explorer_prices()
    )

    # Capture Hero Images
    explorer_image_df = create_vehicle_image_df(
        get_ford_mfg_explorer_hero_img(),
        get_ford_dealer_explorer_hero_img(),
        "Explorer®",
        EXPLORER_MANUFACTURER_IMAGE_URL,
        EXPLORER_DEALER_IMAGE_URL,
    )

    # Append Prices to single list
    vehicles_list_html.append(
        (
            "EXPLORER",
            explorer_prices_df,
            EXPLORER_MANUFACTURER_URL,
            EXPLORER_DEALER_URL,
        )
    )

    # Append Images to single data frame
    all_model_images_df = pd.concat(
        [all_model_images_df, explorer_image_df], ignore_index=True
    )

    print_elapsed_time(func_start_time, "Explorer pricing completed time")
    print_elapsed_time(start_time, "Elapased Time")
else:
    print("EXPLORER_SKIP_FLAG is set to 'true'. Skipping Explorer pricing.")

# ---------------------------------
# Get F-150 Data
# ---------------------------------

if F150_SKIP_FLAG == "false":
    print("F-150 pricing started...")
    func_start_time = start_timer()

    # Capture Prices
    f150_prices_df = create_vehicle_prices_df(
        get_ford_mfg_f150_prices(), get_ford_dealer_f150_prices()
    )

    # Capture Hero Images
    f150_image_df = create_vehicle_image_df(
        get_ford_mfg_f150_hero_img(),
        get_ford_dealer_f150_hero_img(),
        "F-150®",
        F150_MANUFACTURER_IMAGE_URL,
        F150_DEALER_IMAGE_URL,
    )

    # Append Prices to single list
    vehicles_list_html.append(
        (
            "F-150®",
            f150_prices_df,
            F150_MANUFACTURER_URL,
            F150_DEALER_URL,
        )
    )

    # Append Images to single data frame
    all_model_images_df = pd.concat(
        [all_model_images_df, f150_image_df], ignore_index=True
    )

    print_elapsed_time(func_start_time, "F-150 Sport pricing completed time")
    print_elapsed_time(start_time, "Elapased Time")
else:
    print("F150_SKIP_FLAG is set to 'true'. Skipping F150 pricing.")

# ---------------------------------
# Get F-150 Lightening Data
# ---------------------------------

if F150_LIGHTENING_SKIP_FLAG == "false":
    print("F-150 Lightening pricing started...")
    func_start_time = start_timer()

    # Capture Prices
    f150_lightening_prices_df = create_vehicle_prices_df(
        get_ford_mfg_f150_lightening_prices(), get_ford_dealer_f150_lightening_prices()
    )

    # Capture Hero Images
    f150_lightening_image_df = create_vehicle_image_df(
        get_ford_mfg_f150_lightening_hero_img(),
        get_ford_dealer_f150_lightening_hero_img(),
        "F-150® Lightening®",
        F150_LIGHTENING_MANUFACTURER_IMAGE_URL,
        F150_LIGHTENING_DEALER_IMAGE_URL,
    )

    # Append Prices to single list
    vehicles_list_html.append(
        (
            "F-150® LIGHTENING®",
            f150_lightening_prices_df,
            F150_LIGHTENING_MANUFACTURER_URL,
            F150_LIGHTENING_DEALER_URL,
        )
    )

    # Append Images to single data frame
    all_model_images_df = pd.concat(
        [all_model_images_df, f150_lightening_image_df], ignore_index=True
    )

    print_elapsed_time(func_start_time, "F-150 Lightening Sport pricing completed time")
    print_elapsed_time(start_time, "Elapased Time")
else:
    print(
        "F150_LIGHTENING_SKIP_FLAG is set to 'true'. Skipping F150 Lightening pricing."
    )

# ---------------------------------
# Get Mustang Data
# ---------------------------------

if MUSTANG_SKIP_FLAG == "false":
    print("Mustang pricing started...")
    func_start_time = start_timer()

    # Capture Prices
    mustang_prices_df = create_vehicle_prices_df(
        get_ford_mfg_mustang_prices(), get_ford_dealer_mustang_prices()
    )

    # Capture Hero Images
    mustang_image_df = create_vehicle_image_df(
        get_ford_mfg_mustang_hero_img(),
        get_ford_dealer_mustang_hero_img(),
        "Mustang®",
        MUSTANG_MANUFACTURER_IMAGE_URL,
        MUSTANG_DEALER_IMAGE_URL,
    )

    # Append Prices to single list
    vehicles_list_html.append(
        (
            "MUSTANG®",
            mustang_prices_df,
            MUSTANG_MANUFACTURER_URL,
            MUSTANG_DEALER_URL,
        )
    )

    # Append Images to single data frame
    all_model_images_df = pd.concat(
        [all_model_images_df, mustang_image_df], ignore_index=True
    )

    print_elapsed_time(func_start_time, "Mustang pricing completed time")
    print_elapsed_time(start_time, "Elapased Time")
else:
    print("MUSTANG_SKIP_FLAG is set to 'true'. Skipping Mustang pricing.")

# ---------------------------------
# Get Mustang Mach-E Data
# ---------------------------------
if MUSTANG_MACH_E_SKIP_FLAG == "false":
    print("Mustang Mach-E pricing started...")
    func_start_time = start_timer()

    # Capture Prices
    mustang_mach_e_prices_df = create_vehicle_prices_df(
        get_ford_mfg_mustang_mach_e_prices(), get_ford_dealer_mustang_mach_e_prices()
    )

    # Capture Hero Images
    mustang_mach_e_image_df = create_vehicle_image_df(
        get_ford_mfg_mustang_mach_e_hero_img(),
        get_ford_dealer_mustang_mach_e_hero_img(),
        "Mustang MACH-E®",
        MUSTANG_MACH_E_MANUFACTURER_URL,
        MUSTANG_MACH_E_DEALER_URL,
    )

    # Append Prices to single list
    vehicles_list_html.append(
        (
            "MUSTANG MACH-E®",
            mustang_mach_e_prices_df,
            MUSTANG_MACH_E_MANUFACTURER_IMAGE_URL,
            MUSTANG_MACH_E_DEALER_IMAGE_URL,
        )
    )

    # Append Images to single data frame
    all_model_images_df = pd.concat(
        [all_model_images_df, mustang_mach_e_image_df], ignore_index=True
    )

    print_elapsed_time(func_start_time, "Mustang Mach-E pricing completed time")
    print_elapsed_time(start_time, "Elapased Time")
else:
    print("MUSTANG_MACH_E_SKIP_FLAG is set to 'true'. Skipping Mustang Mach-E pricing.")


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
    <p>Please review the latest price and image comparisons between Ford.ca and Fordtodealers.ca. This email is meant to be an informational audit and still needs to be verified by the recieving party before updating any pricing</p>
    <h2>NAVIGATION MENU PRICES</h2>
    Data Sources:
    <ul>
      <li>{MAIN_MANUFACTURER_URL}</li>
      <li>{MAIN_DEALER_URL}</li>
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
