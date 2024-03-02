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
# Selenium configuration - Webdriver for Firefox via Github
GITHUB_TOKEN=github_pac_token

# Email configuration
EMAIL_ERROR_RECIEVER=admin@email.com
EMAIL_SENDER=your-email@gmail.com
EMAIL_RECIEVER=recipient-email@gmail.com
EMAIL_PASSWORD=your-gmail-password
```

### Selenium configuration

- GITHUB_TOKEN = The webdriver_manager downloads some webdrivers from their official GitHub repositories but GitHub has rate limitations in place. An unauthenticated user gets 60 requests per hours. Create a PAC token in Github, and place the value here as authenticated users rate limit is 5000 requests per hour. Follow the insturctions in the [Github link](https://docs.github.com/en/enterprise-server@3.9/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) to create PAC token.

### Email configuration

- EMAIL_ERROR_RECIEVER = These are the emails you would like to send emails to for application failures. It is a comma delimited string format that can contain a single email `recipient-email@gmail.com` or multiple `recipient1-email@gmail.com,recipient2-email@gmail.com`.

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

### constants.py - Vehicle URL's

The `constants.py` file holds the URL's, Web Driver configs, and skip flags that enable selecting specific vehicle data to be web scrapped.

- BROWSER_DRIVER_TYPE = Set this value to the browser you would like to use. Currently the supported browsers are `chrome`, `edge`, and `firefox`. These browsers need to be installed on the host machine that this application runs on.

- HEADLESS_MODE = The value is either `true` (enable headless browsing) or `false` (disable headless browsing).

- SKIP_FLAG = The value is either `true` (disables web scrapping) or `false` (enables web scrapping).

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

Add new lines in the constants.py file

```
<vehicle_model>_SKIP_FLAG=<boolean>
<vehicle_model>_MANUFACTURER_URL=<url>
<vehicle_model>_MANUFACTURER_IMAGE_URL=<url>
<vehicle_model>_DEALER_URL=<url>
<vehicle_model>_DEALER_IMAGE_URL=<url>
```

Then add the new vehicle in the following project structure:

```
my_project/
|-- src/
|   |-- __init__.py
|   |-- mustang_vehicles.py
|   |-- <new_vehicles>.py
|   |-- utilities/
|       |-- __init__.py
|       |-- constants.py
```

Then add the logic to pick out the web elements that hold the vehicle model name, price, and hero image within the `<new_vehicles>.py` file.

It will be easier to copy an existing file, like `mustang_vehicles.py`, and rename it to the `<new_vehicles>.py` and adjusting the XPATH that target the specific information that is needed.

## Windows Scheduler - Schedule Docker Container Run

To schedule the docker container to run locally in a Windows machine, do the following:

1. Open Task Scheduler. You can do this by searching for "Task Scheduler" in the Start menu.

2. In the Task Scheduler, click on "Create Basic Task...".

3. Enter a name and a description for the task and click "Next".

4. Choose "Daily", "Weekly", "Monthly", or "One time", depending on how often you want the task to run, and click "Next".

5. Set the start time and date for the task and click "Next".

6. Choose "Start a program" and click "Next".

7. In the "Program/script" field, enter the path to your Docker Compose executable. This is typically "C:\Program Files\Docker\Docker\resources\bin\docker-compose.exe".

8. In the "Add arguments (optional)" field, enter the command you want to run. For example, to start a Docker Compose service, you might enter "up -d".

9. In the "Start in (optional)" field, enter the path to the directory that contains your Docker Compose file.

10. Click "Next" and then "Finish".

## Contributing

Feel free to contribute to this project by opening issues or pull requests.
