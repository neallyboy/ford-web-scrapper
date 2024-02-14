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
# BROWSER_DRIVER_TYPE options are: chrome, firefox, edge
BROWSER_DRIVER_TYPE=firefox
CHROME_HEADLESS_MODE=false
EDGE_HEADLESS_MODE=false
FIREFOX_HEADLESS_MODE=true
GITHUB_TOKEN=github_pac_token

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
BRONCO_SPORT_IMAGE_URL=https://fordtodealers.ca/ford-bronco-sport/

BRONCO_MANUFACTURER_URL=https://www.ford.ca/suvs/bronco/models/?gnav=vhpnav-specs
BRONCO_MANUFACTURER_IMAGE_URL=https://www.ford.ca/suvs/bronco/?gnav=header-suvs-vhp
BRONCO_DEALER_URL=https://fordtodealers.ca/ford-bronco/
BRONCO_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-bronco/

EDGE_MANUFACTURER_URL=https://www.ford.ca/suvs-crossovers/edge/?gnav=header-suvs-vhp
EDGE_MANUFACTURER_IMAGE_URL=https://www.ford.ca/suvs-crossovers/edge/?gnav=header-suvs-vhp
EDGE_DEALER_URL=https://fordtodealers.ca/ford-edge/
EDGE_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-edge/

ESCAPE_MANUFACTURER_URL=https://www.ford.ca/suvs-crossovers/escape/?gnav=header-suvs-vhp
ESCAPE_MANUFACTURER_IMAGE_URL=https://www.ford.ca/suvs-crossovers/escape/?gnav=header-suvs-vhp
ESCAPE_DEALER_URL=https://fordtodealers.ca/ford-escape/
ESCAPE_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-escape/

F150_MANUFACTURER_URL=https://www.ford.ca/trucks/f150/?gnav=header-trucks-vhp
F150_MANUFACTURER_IMAGE_URL=https://www.ford.ca/trucks/f150/?gnav=header-trucks-vhp
F150_DEALER_URL=https://fordtodealers.ca/ford-f-150/
F150_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-f-150/

F150_LIGHTENING_MANUFACTURER_URL=https://www.ford.ca/trucks/f150/f150-lightning/?gnav=header-trucks-vhp
F150_LIGHTENING_MANUFACTURER_IMAGE_URL=https://www.ford.ca/trucks/f150/f150-lightning/?gnav=header-trucks-vhp
F150_LIGHTENING_DEALER_URL=https://fordtodealers.ca/ford-f150-lightning/
F150_LIGHTENING_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-f150-lightning/

MUSTANG_MANUFACTURER_URL=https://www.ford.ca/cars/mustang/?gnav=header-suvs-vhp
MUSTANG_MANUFACTURER_IMAGE_URL=https://www.ford.ca/cars/mustang/?gnav=header-suvs-vhp
MUSTANG_DEALER_URL=https://fordtodealers.ca/ford-mustang/
MUSTANG_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-mustang/

MUSTANG_MACH_E_MANUFACTURER_URL=https://www.ford.ca/suvs/mach-e/?gnav=vhpnav-overiew
MUSTANG_MACH_E_MANUFACTURER_IMAGE_URL=https://www.ford.ca/suvs/mach-e/?gnav=vhpnav-overiew
MUSTANG_MACH_E_DEALER_URL=https://fordtodealers.ca/ford-mustang-mach-e/
MUSTANG_MACH_E_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-mustang-mach-e/
```

- EMAIL_PASSWORD = This application uses Google gmail to send the email notifcation. In order to send an email, a App Password needs to be created by the gmail account sending the email. It is a 16 character string that needs to be set here.
- GITHUB_TOKEN = If using the Firefox headless mode, you need to create a Github PAC Token in order to by pass the Github API rate limit. Authitcated users get 5000 calls per hour versus 60 calls per hour for unathunticated users.

## Contributing

Feel free to contribute to this project by opening issues or pull requests.
