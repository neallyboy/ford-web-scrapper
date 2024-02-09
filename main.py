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
from src.escape_vehicles import *
from src.f150_vehicles import *
from src.mustang_vehicles import *
from src.navigation_menu import *

# Load environment variables from the .env file
load_dotenv()

# Get email configuration from environment variables
EMAIL_RECIEVER = os.getenv("EMAIL_RECIEVER")
EMAIL_SENDER = os.getenv("EMAIL_RECIEVER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Get Navigation Data
nav_prices_df = create_navigation_prices_df()

# Get Mustang Data
mustang_prices_df = create_mustang_prices_df()
mustang_image_df = create_mustang_image_df()

# Get Escape Data
escape_prices_df = create_escape_prices_df()
escape_image_df = create_escape_image_df()

# Get F-150 Data
f150_image_df = create_f150_image_df()

# --------------------------------------------------#
# Concatenate the Image data frames
# - Merge all the Images to a single data frame
# --------------------------------------------------#
all_model_images_df = pd.concat(
    [mustang_image_df, escape_image_df, f150_image_df], ignore_index=True
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


# Change the colour background to Red if found the word Mismatch.
def redden(x):
    if x == "Mismatch":
        return f'<span style="background-color: red; color: white; padding: 2px 5px; border-radius: 3px;">{x}</span>'
    return str(x)


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
    <h2>MUSTANG PRICES</h2>
    Data Sources:
    <ul>
      <li>{MUSTANG_MANUFACTURER_URL}</li>
      <li>{MUSTANG_DEALER_URL}</li>
    </ul>
    {mustang_prices_df.to_html(classes='table', escape=False, index=False, formatters={'Price Comparison': redden})}
    <h2>ESCAPE PRICES</h2>
    Data Sources:
    <ul>
      <li>{ESCAPE_MANUFACTURER_URL}</li>
      <li>{ESCAPE_DEALER_URL}</li>
    </ul>
    {escape_prices_df.to_html(classes='table', escape=False, index=False, formatters={'Price Comparison': redden})}
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
