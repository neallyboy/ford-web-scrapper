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
- Docker Desktop (optional) to create a docker image and container

## ChromeDriver Setup

NOTE: The `webdriver_manager` package is part of this application and installs the browser driver on-demand which means downloading the drivers not neccessary.

1. **Download ChromeDriver:**
   Download the appropriate version of ChromeDriver for your Chrome browser version. You can download it from [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/).

2. **Set ChromeDriver Path:**
   Create a `.env` file in the project's root directory and add the following line:
   - Replace `/path/to/chromedriver.exe` with the actual path to your downloaded `chromedriver.exe`.

## Installation

1. **Clone the Repository:**

```
git clone https://github.com/firealan/fordtodealer_compare.git
cd fordtodealer_compare
```

2. **Install Python Modules:**

```
pip install -r requirements.txt
```

3. **Create .env and update the given values file:**

Create the .env file in the root folder. Ensure the following environment variables are set in your .env file:

```
# Selenium configuration
# BROWSER_DRIVER_TYPE options are: chrome, firefox, edge
BROWSER_DRIVER_TYPE=firefox
HEADLESS_MODE=false
GITHUB_TOKEN=github_pac_token

# Email configuration
EMAIL_SENDER=your-email@gmail.com
EMAIL_RECIEVER=recipient-email@gmail.com
EMAIL_PASSWORD=your-gmail-password

# URL Configuration
NAVIGATION_SKIP_FLAG=false
NAVIGATION_MODEL_LIST=BRONCO SPORT,EDGE,ESCAPE,F-150,MUSTANG
MAIN_NAVIGATION_MENU_MANUFACTURER_URL=https://www.ford.ca
MAIN_NAVIGATION_MENU_DEALER_URL=https://fordtodealers.ca

BRONCO_SKIP_FLAG=false
BRONCO_MANUFACTURER_URL=https://www.ford.ca/suvs/bronco/models/?gnav=vhpnav-specs
BRONCO_MANUFACTURER_IMAGE_URL=https://www.ford.ca/suvs/bronco/?gnav=header-suvs-vhp
BRONCO_DEALER_URL=https://fordtodealers.ca/ford-bronco/
BRONCO_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-bronco/

BRONCO_SPORT_SKIP_FLAG=false
BRONCO_SPORT_MANUFACTURER_URL=https://www.ford.ca/suvs/bronco-sport/models/?gnav=vhpnav-specs
BRONCO_SPORT_MANUFACTURER_IMAGE_URL=https://www.ford.ca/suvs/bronco-sport/?gnav=vhpnav-overiew
BRONCO_SPORT_DEALER_URL=https://fordtodealers.ca/ford-bronco-sport/
BRONCO_SPORT_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-bronco-sport/

CHASSIS_CAB_SKIP_FLAG=false
CHASSIS_CAB_MANUFACTURER_URL=https://www.ford.ca/commercial-trucks/chassis-cab/?gnav=header-commercial-vhp
CHASSIS_CAB_MANUFACTURER_IMAGE_URL=https://www.ford.ca/commercial-trucks/chassis-cab/?gnav=header-commercial-vhp
CHASSIS_CAB_DEALER_URL=https://fordtodealers.ca/ford-chassis-cab/
CHASSIS_CAB_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-chassis-cab/

E_TRANSIT_SKIP_FLAG=false
E_TRANSIT_MANUFACTURER_URL=https://www.ford.ca/commercial-trucks/e-transit/?gnav=header-trucks-vhp
E_TRANSIT_MANUFACTURER_IMAGE_URL=https://www.ford.ca/commercial-trucks/e-transit/?gnav=header-trucks-vhp
E_TRANSIT_DEALER_URL=https://fordtodealers.ca/ford-e-transit/
E_TRANSIT_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-e-transit/

E_SERIES_CUTAWAY_SKIP_FLAG=false
E_SERIES_CUTAWAY_MANUFACTURER_URL=https://www.ford.ca/commercial-trucks/e-series-cutaway/?gnav=header-commercial-vhp
E_SERIES_CUTAWAY_MANUFACTURER_IMAGE_URL=https://www.ford.ca/commercial-trucks/e-series-cutaway/?gnav=header-commercial-vhp
E_SERIES_CUTAWAY_DEALER_URL=https://fordtodealers.ca/ford-e-series-cutaway/
E_SERIES_CUTAWAY_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-e-series-cutaway/

E_SERIES_STRIPPED_CHASSIS_SKIP_FLAG=false
E_SERIES_STRIPPED_CHASSIS_MANUFACTURER_URL=https://www.ford.ca/commercial-trucks/e-series-stripped-chassis/models/?gnav=vhpnav-specs
E_SERIES_STRIPPED_CHASSIS_MANUFACTURER_IMAGE_URL=https://www.ford.ca/commercial-trucks/e-series-stripped-chassis/?gnav=header-commercial-vhp
E_SERIES_STRIPPED_CHASSIS_DEALER_URL=https://fordtodealers.ca/ford-e-series-stripped-chasis/
E_SERIES_STRIPPED_CHASSIS_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-e-series-stripped-chasis/

EDGE_SKIP_FLAG=false
EDGE_MANUFACTURER_URL=https://www.ford.ca/suvs-crossovers/edge/?gnav=header-suvs-vhp
EDGE_MANUFACTURER_IMAGE_URL=https://www.ford.ca/suvs-crossovers/edge/?gnav=header-suvs-vhp
EDGE_DEALER_URL=https://fordtodealers.ca/ford-edge/
EDGE_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-edge/

ESCAPE_SKIP_FLAG=false
ESCAPE_MANUFACTURER_URL=https://www.ford.ca/suvs-crossovers/escape/?gnav=header-suvs-vhp
ESCAPE_MANUFACTURER_IMAGE_URL=https://www.ford.ca/suvs-crossovers/escape/?gnav=header-suvs-vhp
ESCAPE_DEALER_URL=https://fordtodealers.ca/ford-escape/
ESCAPE_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-escape/

EXPEDITION_SKIP_FLAG=false
EXPEDITION_MANUFACTURER_URL=https://www.ford.ca/suvs/expedition/?gnav=header-suvs-vhp
EXPEDITION_MANUFACTURER_IMAGE_URL=https://www.ford.ca/suvs/expedition/?gnav=header-suvs-vhp
EXPEDITION_DEALER_URL=https://fordtodealers.ca/ford-expedition/
EXPEDITION_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-expedition/

EXPLORER_SKIP_FLAG=false
EXPLORER_MANUFACTURER_URL=https://www.ford.ca/suvs/explorer/?gnav=header-suvs-vhp
EXPLORER_MANUFACTURER_IMAGE_URL=https://www.ford.ca/suvs/explorer/?gnav=header-suvs-vhp
EXPLORER_DEALER_URL=https://fordtodealers.ca/ford-explorer/
EXPLORER_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-explorer/

F_SERIES_STRIPPED_CHASSIS_SKIP_FLAG=false
F_SERIES_STRIPPED_CHASSIS_MANUFACTURER_URL=https://www.ford.ca/commercial-trucks/f-series-stripped-chassis/models/?gnav=vhpnav-specs
F_SERIES_STRIPPED_CHASSIS_MANUFACTURER_IMAGE_URL=https://www.ford.ca/commercial-trucks/f-series-stripped-chassis/?gnav=header-commercial-vhp
F_SERIES_STRIPPED_CHASSIS_DEALER_URL=https://fordtodealers.ca/ford-f-series-stripped-chasis/
F_SERIES_STRIPPED_CHASSIS_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-f-series-stripped-chasis/

F150_SKIP_FLAG=false
F150_MANUFACTURER_URL=https://www.ford.ca/trucks/f150/?gnav=header-trucks-vhp
F150_MANUFACTURER_IMAGE_URL=https://www.ford.ca/trucks/f150/?gnav=header-trucks-vhp
F150_DEALER_URL=https://fordtodealers.ca/ford-f-150/
F150_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-f-150/

F150_COMMERCIAL_SKIP_FLAG=false
F150_COMMERCIAL_MANUFACTURER_URL=https://www.ford.ca/commercial-trucks/f150/?gnav=header-commercial-vhp
F150_COMMERCIAL_MANUFACTURER_IMAGE_URL=https://www.ford.ca/commercial-trucks/f150/?gnav=header-commercial-vhp
F150_COMMERCIAL_DEALER_URL=https://fordtodealers.ca/ford-f-150-commercial/
F150_COMMERCIAL_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-f-150-commercial/

F150_LIGHTENING_SKIP_FLAG=false
F150_LIGHTENING_MANUFACTURER_URL=https://www.ford.ca/trucks/f150/f150-lightning/?gnav=header-trucks-vhp
F150_LIGHTENING_MANUFACTURER_IMAGE_URL=https://www.ford.ca/trucks/f150/f150-lightning/?gnav=header-trucks-vhp
F150_LIGHTENING_DEALER_URL=https://fordtodealers.ca/ford-f150-lightning/
F150_LIGHTENING_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-f150-lightning/

F650_F750_SKIP_FLAG=false
F650_F750_MANUFACTURER_URL=https://www.ford.ca/commercial-trucks/f650-f750/?gnav=header-commercial-vhp
F650_F750_MANUFACTURER_IMAGE_URL=https://www.ford.ca/commercial-trucks/f650-f750/?gnav=header-commercial-vhp
F650_F750_DEALER_URL=https://fordtodealers.ca/ford-f-650-f-750/
F650_F750_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-f-650-f-750/

MAVERICK_SKIP_FLAG=false
MAVERICK_MANUFACTURER_URL=https://www.ford.ca/trucks/maverick/?gnav=header-trucks-vhp
MAVERICK_MANUFACTURER_IMAGE_URL=https://www.ford.ca/trucks/maverick/?gnav=header-trucks-vhp
MAVERICK_DEALER_URL=https://fordtodealers.ca/ford-maverick/
MAVERICK_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-maverick/

MUSTANG_SKIP_FLAG=false
MUSTANG_MANUFACTURER_URL=https://www.ford.ca/cars/mustang/?gnav=header-suvs-vhp
MUSTANG_MANUFACTURER_IMAGE_URL=https://www.ford.ca/cars/mustang/?gnav=header-suvs-vhp
MUSTANG_DEALER_URL=https://fordtodealers.ca/ford-mustang/
MUSTANG_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-mustang/

MUSTANG_MACH_E_SKIP_FLAG=false
MUSTANG_MACH_E_MANUFACTURER_URL=https://www.ford.ca/suvs/mach-e/?gnav=vhpnav-overiew
MUSTANG_MACH_E_MANUFACTURER_IMAGE_URL=https://www.ford.ca/suvs/mach-e/?gnav=vhpnav-overiew
MUSTANG_MACH_E_DEALER_URL=https://fordtodealers.ca/ford-mustang-mach-e/
MUSTANG_MACH_E_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-mustang-mach-e/

RANGER_SKIP_FLAG=false
RANGER_MANUFACTURER_URL=https://www.ford.ca/trucks/ranger/?gnav=header-trucks-vhp
RANGER_MANUFACTURER_IMAGE_URL=https://www.ford.ca/trucks/ranger/?gnav=header-trucks-vhp
RANGER_DEALER_URL=https://fordtodealers.ca/ford-ranger/
RANGER_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-ranger/

SUPER_DUTY_SKIP_FLAG=false
SUPER_DUTY_MANUFACTURER_URL=https://www.ford.ca/trucks/super-duty/?gnav=header-trucks-vhp
SUPER_DUTY_MANUFACTURER_IMAGE_URL=https://www.ford.ca/trucks/super-duty/?gnav=header-trucks-vhp
SUPER_DUTY_DEALER_URL=https://fordtodealers.ca/ford-super-duty-commercial/
SUPER_DUTY_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-super-duty-commercial/

SUPER_DUTY_COMMERCIAL_SKIP_FLAG=false
SUPER_DUTY_COMMERCIAL_MANUFACTURER_URL=https://www.ford.ca/commercial-trucks/super-duty/?gnav=header-commercial-vhp
SUPER_DUTY_COMMERCIAL_MANUFACTURER_IMAGE_URL=https://www.ford.ca/commercial-trucks/super-duty/?gnav=header-commercial-vhp
SUPER_DUTY_COMMERCIAL_DEALER_URL=https://fordtodealers.ca/ford-super-duty-commercial/
SUPER_DUTY_COMMERCIAL_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-super-duty-commercial/

TRANSIT_SKIP_FLAG=false
TRANSIT_MANUFACTURER_URL=https://www.ford.ca/trucks/transit-passenger-van-wagon/?gnav=header-trucks-vhp
TRANSIT_MANUFACTURER_IMAGE_URL=https://www.ford.ca/trucks/transit-passenger-van-wagon/?gnav=header-trucks-vhp
TRANSIT_DEALER_URL=https://fordtodealers.ca/ford-transit/
TRANSIT_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-transit/

TRANSIT_CC_CA_SKIP_FLAG=false
TRANSIT_CC_CA_MANUFACTURER_URL=https://www.ford.ca/commercial-trucks/transit-chassis/?gnav=header-commercial-vhp
TRANSIT_CC_CA_MANUFACTURER_IMAGE_URL=https://www.ford.ca/commercial-trucks/transit-chassis/?gnav=header-commercial-vhp
TRANSIT_CC_CA_DEALER_URL=https://fordtodealers.ca/ford-transit-cc-ca/
TRANSIT_CC_CA_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-transit-cc-ca/

TRANSIT_COMMERCIAL_SKIP_FLAG=false
TRANSIT_COMMERCIAL_MANUFACTURER_URL=https://www.ford.ca/commercial-trucks/transit-cargo-van/?gnav=header-commercial-vhp
TRANSIT_COMMERCIAL_MANUFACTURER_IMAGE_URL=https://www.ford.ca/commercial-trucks/transit-cargo-van/?gnav=header-commercial-vhp
TRANSIT_COMMERCIAL_DEALER_URL=https://fordtodealers.ca/ford-transit-commercial/
TRANSIT_COMMERCIAL_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-transit-commercial/

TRANSIT_CONNECT_SKIP_FLAG=false
TRANSIT_CONNECT_MANUFACTURER_URL=https://www.ford.ca/trucks/transit-connect-passenger-van-wagon/?gnav=header-trucks-vhp
TRANSIT_CONNECT_MANUFACTURER_IMAGE_URL=https://www.ford.ca/trucks/transit-connect-passenger-van-wagon/?gnav=header-trucks-vhp
TRANSIT_CONNECT_DEALER_URL=https://fordtodealers.ca/ford-transit-connect/
TRANSIT_CONNECT_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-transit-connect/

TRANSIT_CONNECT_COMMERCIAL_SKIP_FLAG=false
TRANSIT_CONNECT_COMMERCIAL_MANUFACTURER_URL=https://www.ford.ca/commercial-trucks/transit-connect-cargo-van/?gnav=header-commercial-vhp
TRANSIT_CONNECT_COMMERCIAL_MANUFACTURER_IMAGE_URL=https://www.ford.ca/commercial-trucks/transit-connect-cargo-van/?gnav=header-commercial-vhp
TRANSIT_CONNECT_COMMERCIAL_DEALER_URL=https://fordtodealers.ca/ford-transit-connect/
TRANSIT_CONNECT_COMMERCIAL_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-transit-connect/
```

### Selenium configuration

- BROWSER_DRIVER_TYPE = Set this value to the browser you would like to use. Currently the supported browsers are `chrome`, `edge`, and `firefox`. These browsers need to be installed on the host machine that this application runs on.

- HEADLESS_MODE = The value is either `true` (enable headless browsing) or `false` (disable headless browsing).

- GITHUB_TOKEN = The webdriver_manager downloads some webdrivers from their official GitHub repositories but GitHub has rate limitations in place. An unauthenticated user gets 60 requests per hours. Create a PAC token in Github, and place the value here as authenticated users rate limit is 5000 requests per hour. Follow the insturctions in the [Github link](https://docs.github.com/en/enterprise-server@3.9/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) to create PAC token.

### Email configuration

- EMAIL_SENDER = This is the email you are sending the email notification from i.e. youremail@gmail.com. This is also used as the login credentials for Gmail.

- EMAIL_RECIEVER = These are the emails you would like to send emails to. It is a comma delimited string format that can contain a single email `recipient-email@gmail.com` or multiple `recipient1-email@gmail.com,recipient2-email@gmail.com`.

- EMAIL_PASSWORD = This application uses Google gmail to send the email notifcation. In order to send an email, a App Password needs to be created by the gmail account sending the email. It is a 16 character string that needs to be set here. Follow the instruction in the [Google link](https://knowledge.workspace.google.com/kb/how-to-create-app-passwords-000009237) to create an app password.

### URL configuration

The URL's listed here are for the individual vehicle page that contains the vehicle trim prices and hero image. There might be some cases where the pricing is a different url than the hero image thus allowing you to specify where either will be.

The pattern is:

```
<vehicle_model>_SKIP_FLAG=<boolean>
<vehicle_model>_MANUFACTURER_URL=<url>
<vehicle_model>_MANUFACTURER_IMAGE_URL=<url>
<vehicle_model>_DEALER_URL=<url>
<vehicle_model>_DEALER_IMAGE_URL=<url>
```

Example for Bronco Sport vehicle:

```
BRONCO_SPORT_SKIP_FLAG=false
BRONCO_SPORT_MANUFACTURER_URL=https://www.ford.ca/suvs/bronco-sport/models/?gnav=vhpnav-specs
BRONCO_SPORT_MANUFACTURER_IMAGE_URL=https://www.ford.ca/suvs/bronco-sport/?gnav=vhpnav-overiew
BRONCO_SPORT_DEALER_URL=https://fordtodealers.ca/ford-bronco-sport/
BRONCO_SPORT_DEALER_IMAGE_URL=https://fordtodealers.ca/ford-bronco-sport/
```

4. **Create Python .venv for the project:**

In VS Code, it is a good idea to create a python virtual environemnt so all the project dependencies are contained within for a cleaner development space.

To create a virtual environment for the project please follow the instructions in the [Visual Studio link](https://code.visualstudio.com/docs/python/environments) - creating environments.

## Docker - Optional Step

This project contains a Docker file to be able to create a Docker image and container to run independent of host computer requirements. In otherwords, the container will hold **ALL** dependencies required for the python application to run.

1. **Install Docker Desktop:**

Install Docker desktop on the host machine. It can be [found here](https://www.docker.com/products/docker-desktop/).

2. **Build Docker Image**

In your terminal run the following:

```
docker build -t ford_data_scraping .
```

## Run the Script

```
python main.py
```

This will run the script locally, and will scrape Ford vehicle models, prices, and hero immages, compare them, generate an HTML email, and send it to the specified email address.

## Adding a new vehicle

Need to add new lines in the .env file

```
<vehicle_model>_SKIP_FLAG=<boolean>
<vehicle_model>_MANUFACTURER_URL=<url>
<vehicle_model>_MANUFACTURER_IMAGE_URL=<url>
<vehicle_model>_DEALER_URL=<url>
<vehicle_model>_DEALER_IMAGE_URL=<url>
```

Then the logic to pick out the web elements that hold the vehicle model name, price, and hero image will need to be created as a new file in the `src` folder.

It will be easier to copy an existing file, like mustang_vehicles.py, and rename it to the new vehicle and adjusting the XPATH that target the specific information that is needed.

## Contributing

Feel free to contribute to this project by opening issues or pull requests.
