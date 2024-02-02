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
from mustang_vehicles import get_ford_mfg_mustang_prices, get_ford_dealer_mustang_prices

# Load environment variables from the .env file
load_dotenv()

# Get email configuration from environment variables
EMAIL_RECIEVER = os.getenv("EMAIL_RECIEVER")
EMAIL_SENDER = os.getenv("EMAIL_RECIEVER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Get Mustang Data
ford_mfr_mustangs = get_ford_mfg_mustang_prices()
ford_dealer_mustangs = get_ford_dealer_mustang_prices()

# Convert datasets to DataFrames
df1 = pd.DataFrame(ford_mfr_mustangs, columns=['Car Model', 'Ford Manufacturer Price'])
df2 = pd.DataFrame(ford_dealer_mustangs, columns=['Car Model', 'Ford Dealer Price'])

# Merge datasets on 'Car Model'
merged_df = pd.merge(df1, df2, on='Car Model', how='outer', suffixes=('_ford_mfr_vehicles', '_ford_dealer_vehicles'))

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

# Function to apply cell coloring based on the price comparison
def highlight_price_difference(val):
    if isinstance(val, pd.Series):
        return [f'background-color: {"red" if "mismatch" in v.lower() else "green" if "match" in v.lower() else ""}; color: white' for v in val]
    else:
        return f'background-color: {"red" if "mismatch" in val.lower() else "green" if "match" in val.lower() else ""}; color: white'

# Apply styling to the DataFrame
styled_df = merged_df.style.apply(highlight_price_difference, subset=pd.IndexSlice[:, ['Price Comparison']])

# print(styled_df.to_html(classes='table', escape=False, index=False, header=False))

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
    {styled_df.to_html(classes='table', escape=False, index=False, header=False)}  <!-- Add index=False, header=False to exclude the index column -->
  </body>
</html>
"""

msg.attach(MIMEText(html_content, 'html'))

# Connect to the SMTP server
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())