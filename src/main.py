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
from escape_vehicles import get_ford_mfg_escape_prices, get_ford_dealer_escape_prices
from mustang_vehicles import *

# Load environment variables from the .env file
load_dotenv()

# Get email configuration from environment variables
EMAIL_RECIEVER = os.getenv("EMAIL_RECIEVER")
EMAIL_SENDER = os.getenv("EMAIL_RECIEVER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Get Mustang Data
ford_mfr_mustang_prices = get_ford_mfg_mustang_prices()
ford_dealer_mustangs_prices = get_ford_dealer_mustang_prices()

ford_mfr_mustang_image = get_ford_mfg_mustang_hero_img()
ford_dealer_mustang_image = get_ford_dealer_mustang_hero_img()

# Convert datasets to DataFrames
mustang_mfr_prices_df = pd.DataFrame(ford_mfr_mustang_prices, columns=['Car Model', 'Ford Manufacturer Price'])
mustang_dealer_prices_df = pd.DataFrame(ford_dealer_mustangs_prices, columns=['Car Model', 'Ford Dealer Price'])

hero_image_df = pd.DataFrame({'Model Hero Image': ['Mustang'],'Ford Manufacturer Image': [ford_mfr_mustang_image],'Ford Dealer Image': [ford_dealer_mustang_image]})

# Merge datasets on 'Car Model'
merged_df = pd.merge(mustang_mfr_prices_df, mustang_dealer_prices_df, on='Car Model', how='outer', suffixes=('_ford_mfr_vehicles', '_ford_dealer_vehicles'))

# Sort
merged_df.sort_values(by=['Ford Manufacturer Price'], inplace=True)

# Set the index to 'Car Model'
merged_df.set_index('Car Model', inplace=True)

# Replace NaN values with $0
merged_df.fillna('$0', inplace=True)

# Reset the index to avoid multi-level index rendering issues
merged_df.reset_index(inplace=True)

# Add a column for price comparison
merged_df['Price Comparison'] = 'Match'
merged_df.loc[merged_df['Ford Manufacturer Price'] != merged_df['Ford Dealer Price'], 'Price Comparison'] = 'Mismatch'

hero_image_df['Image Comparison'] = 'Match'
hero_image_df.loc[hero_image_df['Ford Manufacturer Image'] != hero_image_df['Ford Dealer Image'], 'Image Comparison'] = 'Mismatch'

# Email configuration
sender_email = EMAIL_SENDER
receiver_email = EMAIL_RECIEVER
password = EMAIL_PASSWORD

# Create the message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Mustang Prices Update"

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
    <h2>Mustang Prices</h2>
    {merged_df.to_html(classes='table', escape=False, index=False)}
    <h2>Model Hero Images</h2>
    {hero_image_df.to_html(classes='table', escape=False, index=False)}
  </body>
</html>
"""

msg.attach(MIMEText(html_content, 'html'))

# Connect to the SMTP server
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())