# Data Scraping Ford Vehicles

## Overview

This project scrapes Ford vehicle prices and hero images from Ford's official website and a dealer website, compares the prices, and sends an email notification.

## Prerequisites

Before running the script, ensure you have the following:

- Python 3.x installed
- Chrome browser installed
- ChromeDriver downloaded and configured (see instructions below)
- Required Python modules installed (install using `pip install -r requirements.txt`)
- A Gmail account for sending email notifications

## ChromeDriver Setup

1. **Download ChromeDriver:**
   Download the appropriate version of ChromeDriver for your Chrome browser version. You can download it from [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/).

2. **Set ChromeDriver Path:**
   Create a `.env` file in the project's root directory and add the following line:
   - Replace `/path/to/chromedriver.exe` with the actual path to your downloaded `chromedriver.exe`.

## Installation

1. **Clone the Repository:**

```
git clone https://github.com/your-username/my-project.git
cd my-project


pip install -r requirements.txt
```

2. **Install Python Modules:**

```
pip install -r requirements.txt
```

## Run the Script

```
python main.py
```

The script will scrape Ford vehicle models, prices, and hero immages, compare them, generate an HTML email, and send it to the specified email address.

## Environment Variables

Ensure the following environment variables are set in your .env file:

```
# Selenium configuration
CHROME_DRIVER_PATH=/path/to/chromedriver.exe
CHROME_HEADLESS_MODE=false

# Email configuration
EMAIL_SENDER=your-email@gmail.com
EMAIL_RECIEVER=recipient-email@gmail.com
EMAIL_PASSWORD=your-gmail-password

# URL Configuration
MAIN_MANUFACTURER_URL=https://www.ford.ca
MAIN_DEALER_URL=https://fordtodealers.ca

BRONCO_SPORT_MANUFACTURER_URL=https://www.ford.ca/suvs/bronco-sport/models/?gnav=vhpnav-specs
BRONCO_SPORT_MANUFACTURER_IMAGE_URL=https://www.ford.ca/suvs/bronco-sport/?gnav=vhpnav-overiew
BRONCO_SPORT_DEALER_URL=https://fordtodealers.ca/ford-bronco-sport/

BRONCO_MANUFACTURER_URL=https://www.ford.ca/suvs/bronco/models/?gnav=vhpnav-specs
BRONCO_MANUFACTURER_IMAGE_URL=https://www.ford.ca/suvs/bronco/?gnav=header-suvs-vhp
BRONCO_DEALER_URL=https://fordtodealers.ca/ford-bronco/

EDGE_MANUFACTURER_URL=https://www.ford.ca/suvs-crossovers/edge/?gnav=header-suvs-vhp
EDGE_DEALER_URL=https://fordtodealers.ca/ford-edge/

ESCAPE_MANUFACTURER_URL=https://www.ford.ca/suvs-crossovers/escape/?gnav=header-suvs-vhp
ESCAPE_DEALER_URL=https://fordtodealers.ca/ford-escape/

F150_MANUFACTURER_URL=https://www.ford.ca/trucks/f150/?gnav=header-trucks-vhp
F150_DEALER_URL=https://fordtodealers.ca/ford-f-150/

F150_LIGHTENING_MANUFACTURER_URL=https://www.ford.ca/trucks/f150/f150-lightning/?gnav=header-trucks-vhp
F150_LIGHTENING_DEALER_URL=https://fordtodealers.ca/ford-f150-lightning/

MUSTANG_MANUFACTURER_URL=https://www.ford.ca/cars/mustang/?gnav=header-suvs-vhp
MUSTANG_DEALER_URL=https://fordtodealers.ca/ford-mustang/

MUSTANG_MACH_E_MANUFACTURER_URL=https://www.ford.ca/suvs/mach-e/?gnav=vhpnav-overiew
MUSTANG_MACH_E_DEALER_URL=https://fordtodealers.ca/ford-mustang-mach-e/
```

Note the gmail password needs to be setup as an App Password. You will need to go to the account settings to set this up.

## Contributing

Feel free to contribute to this project by opening issues or pull requests.
