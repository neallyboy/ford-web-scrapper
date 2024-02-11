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
from src.bronco_sport_vehicles import *
from src.edge_vehicles import *
from src.escape_vehicles import *
from src.f150_vehicles import *
from src.mustang_vehicles import *
from src.navigation_menu import *
from src.utilities.utilities import *

# Load environment variables from the .env file
load_dotenv()

# Record the start time
start_time = time.time()

# Get email configuration from environment variables
EMAIL_RECIEVER = os.getenv("EMAIL_RECIEVER")
EMAIL_SENDER = os.getenv("EMAIL_RECIEVER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Get Navigation Data
nav_prices_df = create_navigation_prices_df()

# Get Bronco Sport Data
bronco_sport_prices_df = create_vehicle_prices_df(
    get_ford_mfg_bronco_sport_prices(), get_ford_dealer_bronco_sport_prices()
)
bronco_sport_image_df = create_vehicle_image_df(
    get_ford_mfg_bronco_sport_hero_img(),
    get_ford_dealer_bronco_sport_hero_img(),
    "Bronco Sport",
)

# Get Edge Data
edge_prices_df = create_vehicle_prices_df(
    get_ford_mfg_edge_prices(), get_ford_dealer_edge_prices()
)
edge_image_df = create_vehicle_image_df(
    get_ford_mfg_edge_hero_img(), get_ford_dealer_edge_hero_img(), "Edge"
)

# Get Escape Data
escape_prices_df = create_vehicle_prices_df(
    get_ford_mfg_escape_prices(), get_ford_dealer_escape_prices()
)
escape_image_df = create_vehicle_image_df(
    get_ford_mfg_escape_hero_img(), get_ford_dealer_escape_hero_img(), "Escape"
)

# Get F-150 Data
f150_prices_df = create_vehicle_prices_df(
    get_ford_mfg_f150_prices(), get_ford_dealer_f150_prices()
)
f150_image_df = create_vehicle_image_df(
    get_ford_mfg_f150_hero_img(), get_ford_dealer_f150_hero_img(), "F-150"
)

# Get Mustang Data
mustang_prices_df = create_vehicle_prices_df(
    get_ford_mfg_mustang_prices(), get_ford_dealer_mustang_prices()
)
mustang_image_df = create_vehicle_image_df(
    get_ford_mfg_mustang_hero_img(), get_ford_dealer_mustang_hero_img(), "Mustang"
)

# --------------------------------------------------#
# Concatenate the Image data frames
# - Merge all the Images to a single data frame
# --------------------------------------------------#
all_model_images_df = pd.concat(
    [
        bronco_sport_image_df,
        edge_image_df,
        escape_image_df,
        f150_image_df,
        mustang_image_df,
    ],
    ignore_index=True,
)

# Email configuration
sender_email = EMAIL_SENDER
receiver_email = EMAIL_RECIEVER
password = EMAIL_PASSWORD

# Create the message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
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
    <p>Please find the latest price and image comparisons between Ford.ca and Fordtodealers.ca</p>
    <h2>NAVIGATION MENU PRICES</h2>
    Data Sources:
    <ul>
      <li>{MAIN_MANUFACTURER_URL}</li>
      <li>{MAIN_DEALER_URL}</li>
    </ul>
    {nav_prices_df.to_html(classes='table', escape=False, index=False, formatters={'Price Comparison': redden})}
    <h2>BRONCO SPORT PRICES</h2>
    Data Sources:
    <ul>
      <li>{BRONCO_SPORT_MANUFACTURER_URL}</li>
      <li>{BRONCO_SPORT_DEALER_URL}</li>
    </ul>
    {bronco_sport_prices_df.to_html(classes='table', escape=False, index=False, formatters={'Price Comparison': redden})}
    <h2>EDGE PRICES</h2>
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
    <h2>F-150 PRICES</h2>
    Data Sources:
    <ul>
      <li>{F150_MANUFACTURER_URL}</li>
      <li>{F150_DEALER_URL}</li>
    </ul>
    {f150_prices_df.to_html(classes='table', escape=False, index=False, formatters={'Price Comparison': redden})}
    <h2>MUSTANG PRICES</h2>
    Data Sources:
    <ul>
      <li>{MUSTANG_MANUFACTURER_URL}</li>
      <li>{MUSTANG_DEALER_URL}</li>
    </ul>
    {mustang_prices_df.to_html(classes='table', escape=False, index=False, formatters={'Price Comparison': redden})}
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
    server.sendmail(sender_email, receiver_email, msg.as_string())

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
