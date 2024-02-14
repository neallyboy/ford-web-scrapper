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

# ---------------------------------
# Get Navigation Data
# ---------------------------------

print("Navigation pricing started.")
func_start_time = start_timer()

nav_prices_df = create_navigation_prices_df()

print_elapsed_time(func_start_time, "Navigation pricing completed time")
print_elapsed_time(start_time, "Elapased Time")

# ---------------------------------
# Get Bronco Data
# ---------------------------------

print("Bronco pricing started.")
func_start_time = start_timer()

bronco_prices_df = create_vehicle_prices_df(
    get_ford_mfg_bronco_prices(), get_ford_dealer_bronco_prices()
)
bronco_image_df = create_vehicle_image_df(
    get_ford_mfg_bronco_hero_img(),
    get_ford_dealer_bronco_hero_img(),
    "Bronco®",
    BRONCO_MANUFACTURER_IMAGE_URL,
    BRONCO_DEALER_URL,
)

print_elapsed_time(func_start_time, "Bronco pricing completed time")
print_elapsed_time(start_time, "Elapased Time")

# ---------------------------------
# Get Bronco Sport Data
# ---------------------------------

print("Bronco Sport pricing started.")
func_start_time = start_timer()

bronco_sport_prices_df = create_vehicle_prices_df(
    get_ford_mfg_bronco_sport_prices(), get_ford_dealer_bronco_sport_prices()
)
bronco_sport_image_df = create_vehicle_image_df(
    get_ford_mfg_bronco_sport_hero_img(),
    get_ford_dealer_bronco_sport_hero_img(),
    "Bronco® Sport",
    BRONCO_SPORT_MANUFACTURER_IMAGE_URL,
    BRONCO_SPORT_DEALER_URL,
)

print_elapsed_time(func_start_time, "Bronco Sport pricing completed time")
print_elapsed_time(start_time, "Elapased Time")

# ---------------------------------
# Get Edge Data
# ---------------------------------

print("Edge pricing started.")
func_start_time = start_timer()

edge_prices_df = create_vehicle_prices_df(
    get_ford_mfg_edge_prices(), get_ford_dealer_edge_prices()
)
edge_image_df = create_vehicle_image_df(
    get_ford_mfg_edge_hero_img(),
    get_ford_dealer_edge_hero_img(),
    "Edge®",
    EDGE_MANUFACTURER_URL,
    EDGE_DEALER_URL,
)

print_elapsed_time(func_start_time, "Edge Sport pricing completed time")
print_elapsed_time(start_time, "Elapased Time")

# ---------------------------------
# Get Escape Data
# ---------------------------------

print("Escape pricing started.")
func_start_time = start_timer()

escape_prices_df = create_vehicle_prices_df(
    get_ford_mfg_escape_prices(), get_ford_dealer_escape_prices()
)
escape_image_df = create_vehicle_image_df(
    get_ford_mfg_escape_hero_img(),
    get_ford_dealer_escape_hero_img(),
    "Escape",
    ESCAPE_MANUFACTURER_URL,
    ESCAPE_DEALER_URL,
)

print_elapsed_time(func_start_time, "Escape Sport pricing completed time")
print_elapsed_time(start_time, "Elapased Time")

# ---------------------------------
# Get F-150 Data
# ---------------------------------

print("F-150 pricing started.")
func_start_time = start_timer()

f150_prices_df = create_vehicle_prices_df(
    get_ford_mfg_f150_prices(), get_ford_dealer_f150_prices()
)
f150_image_df = create_vehicle_image_df(
    get_ford_mfg_f150_hero_img(),
    get_ford_dealer_f150_hero_img(),
    "F-150®",
    F150_MANUFACTURER_URL,
    F150_DEALER_URL,
)

print_elapsed_time(func_start_time, "F-150 Sport pricing completed time")
print_elapsed_time(start_time, "Elapased Time")

# ---------------------------------
# Get F-150 Lightening Data
# ---------------------------------

print("F-150 Lightening pricing started.")
func_start_time = start_timer()

f150_lightening_prices_df = create_vehicle_prices_df(
    get_ford_mfg_f150_lightening_prices(), get_ford_dealer_f150_lightening_prices()
)
f150_lightening_image_df = create_vehicle_image_df(
    get_ford_mfg_f150_lightening_hero_img(),
    get_ford_dealer_f150_lightening_hero_img(),
    "F-150® Lightening®",
    F150_LIGHTENING_MANUFACTURER_URL,
    F150_LIGHTENING_DEALER_URL,
)

print_elapsed_time(func_start_time, "F-150 Lightening Sport pricing completed time")
print_elapsed_time(start_time, "Elapased Time")

# ---------------------------------
# Get Mustang Data
# ---------------------------------

print("Mustang pricing started.")
func_start_time = start_timer()

mustang_prices_df = create_vehicle_prices_df(
    get_ford_mfg_mustang_prices(), get_ford_dealer_mustang_prices()
)
mustang_image_df = create_vehicle_image_df(
    get_ford_mfg_mustang_hero_img(),
    get_ford_dealer_mustang_hero_img(),
    "Mustang®",
    MUSTANG_MANUFACTURER_URL,
    MUSTANG_DEALER_URL,
)

print_elapsed_time(func_start_time, "Mustang pricing completed time")
print_elapsed_time(start_time, "Elapased Time")

# ---------------------------------
# Get Mustang Mach-E Data
# ---------------------------------

print("Mustang Mach-E pricing started.")
func_start_time = start_timer()

mustang_mach_e_prices_df = create_vehicle_prices_df(
    get_ford_mfg_mustang_mach_e_prices(), get_ford_dealer_mustang_mach_e_prices()
)
mustang_mach_e_image_df = create_vehicle_image_df(
    get_ford_mfg_mustang_mach_e_hero_img(),
    get_ford_dealer_mustang_mach_e_hero_img(),
    "Mustang MACH-E®",
    MUSTANG_MACH_E_MANUFACTURER_URL,
    MUSTANG_MACH_E_DEALER_URL,
)

print_elapsed_time(func_start_time, "Mustang Mach-E pricing completed time")
print_elapsed_time(start_time, "Elapased Time")

# --------------------------------------------------#
# Concatenate the Image data frames
# - Merge all the Images to a single data frame
# --------------------------------------------------#
all_model_images_df = pd.concat(
    [
        bronco_image_df,
        bronco_sport_image_df,
        edge_image_df,
        escape_image_df,
        f150_image_df,
        f150_lightening_image_df,
        mustang_image_df,
        mustang_mach_e_image_df,
    ],
    ignore_index=True,
)

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
    <h2>BRONCO® PRICES</h2>
    Data Sources:
    <ul>
      <li>{BRONCO_MANUFACTURER_URL}</li>
      <li>{BRONCO_DEALER_URL}</li>
    </ul>
    {bronco_prices_df.to_html(classes='table', escape=False, index=False, formatters={'Price Comparison': redden})}
    <h2>BRONCO® SPORT PRICES</h2>
    Data Sources:
    <ul>
      <li>{BRONCO_SPORT_MANUFACTURER_URL}</li>
      <li>{BRONCO_SPORT_DEALER_URL}</li>
    </ul>
    {bronco_sport_prices_df.to_html(classes='table', escape=False, index=False, formatters={'Price Comparison': redden})}
    <h2>EDGE® PRICES</h2>
    Data Sources:
    <ul>
      <li>{EDGE_MANUFACTURER_URL}</li>
      <li>{EDGE_DEALER_URL}</li>
    </ul>
    {edge_prices_df.to_html(classes='table', escape=False, index=False, formatters={'Price Comparison': redden})}
    <h2>ESCAPE PRICES</h2>
    Data Sources:
    <ul>
      <li>{ESCAPE_MANUFACTURER_URL}</li>
      <li>{ESCAPE_DEALER_URL}</li>
    </ul>
    {escape_prices_df.to_html(classes='table', escape=False, index=False, formatters={'Price Comparison': redden})}
    <h2>F-150® PRICES</h2>
    Data Sources:
    <ul>
      <li>{F150_MANUFACTURER_URL}</li>
      <li>{F150_DEALER_URL}</li>
    </ul>
    {f150_prices_df.to_html(classes='table', escape=False, index=False, formatters={'Price Comparison': redden})}
    <h2>F-150® LIGHTENING® PRICES</h2>
    Data Sources:
    <ul>
      <li>{F150_LIGHTENING_MANUFACTURER_URL}</li>
      <li>{F150_LIGHTENING_DEALER_URL}</li>
    </ul>
    {f150_lightening_prices_df.to_html(classes='table', escape=False, index=False, formatters={'Price Comparison': redden})}
    <h2>MUSTANG® PRICES</h2>
    Data Sources:
    <ul>
      <li>{MUSTANG_MANUFACTURER_URL}</li>
      <li>{MUSTANG_DEALER_URL}</li>
    </ul>
    {mustang_prices_df.to_html(classes='table', escape=False, index=False, formatters={'Price Comparison': redden})}
    <h2>MUSTANG MACH-E® PRICES</h2>
    Data Sources:
    <ul>
      <li>{MUSTANG_MACH_E_MANUFACTURER_URL}</li>
      <li>{MUSTANG_MACH_E_DEALER_URL}</li>
    </ul>
    {mustang_mach_e_prices_df.to_html(classes='table', escape=False, index=False, formatters={'Price Comparison': redden})}
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
