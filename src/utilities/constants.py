constants = {
    # BROWSER_DRIVER_TYPE options are: chrome, firefox, edge
    "BROWSER_DRIVER_TYPE":"firefox",
    "HEADLESS_MODE":True,
    "TIME_SLEEP":3,

    # Email configuration
    "EMAIL_SKIP_FLAG":True,

    # URL Configuration
    "NAVIGATION_SKIP_FLAG":False,
    # "NAVIGATION_MODEL_LIST":["BRONCO SPORT","EDGE,ESCAPE","F-150","F-150 LIGHTNING","MUSTANG","MUSTANG MACH-E"],
    "NAVIGATION_MODEL_LIST":["BRONCO SPORT","EDGE","ESCAPE","F-150","MUSTANG"],
    # "NAVIGATION_MODEL_LIST":[],
    "MAIN_NAVIGATION_MENU_MANUFACTURER_URL":"https://www.ford.ca",
    "MAIN_NAVIGATION_MENU_DEALER_URL":"https://fordtodealers.ca",

    # Vehicle Configuration
    "BRONCO_SKIP_FLAG":True,
    "BRONCO_MANUFACTURER_URL":"https://www.ford.ca/suvs/bronco/models/?gnav=vhpnav-specs",
    "BRONCO_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/suvs/bronco/?gnav=header-suvs-vhp",
    "BRONCO_DEALER_URL":"https://fordtodealers.ca/ford-bronco/",
    "BRONCO_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-bronco/",

    "BRONCO_SPORT_SKIP_FLAG":False,
    "BRONCO_SPORT_MANUFACTURER_URL":"https://www.ford.ca/suvs/bronco-sport/models/?gnav=vhpnav-specs",
    "BRONCO_SPORT_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/suvs/bronco-sport/?gnav=vhpnav-overiew",
    "BRONCO_SPORT_DEALER_URL":"https://fordtodealers.ca/ford-bronco-sport/",
    "BRONCO_SPORT_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-bronco-sport/",

    "CHASSIS_CAB_SKIP_FLAG":True,
    "CHASSIS_CAB_MANUFACTURER_URL":"https://www.ford.ca/commercial-trucks/chassis-cab/?gnav=header-commercial-vhp",
    "CHASSIS_CAB_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/commercial-trucks/chassis-cab/?gnav=header-commercial-vhp",
    "CHASSIS_CAB_DEALER_URL":"https://fordtodealers.ca/ford-chassis-cab/",
    "CHASSIS_CAB_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-chassis-cab/",

    "E_TRANSIT_SKIP_FLAG":True,
    "E_TRANSIT_MANUFACTURER_URL":"https://www.ford.ca/commercial-trucks/e-transit/?gnav=header-trucks-vhp",
    "E_TRANSIT_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/commercial-trucks/e-transit/?gnav=header-trucks-vhp",
    "E_TRANSIT_DEALER_URL":"https://fordtodealers.ca/ford-e-transit/",
    "E_TRANSIT_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-e-transit/",

    "E_SERIES_CUTAWAY_SKIP_FLAG":True,
    "E_SERIES_CUTAWAY_MANUFACTURER_URL":"https://www.ford.ca/commercial-trucks/e-series-cutaway/?gnav=header-commercial-vhp",
    "E_SERIES_CUTAWAY_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/commercial-trucks/e-series-cutaway/?gnav=header-commercial-vhp",
    "E_SERIES_CUTAWAY_DEALER_URL":"https://fordtodealers.ca/ford-e-series-cutaway/",
    "E_SERIES_CUTAWAY_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-e-series-cutaway/",

    "E_SERIES_STRIPPED_CHASSIS_SKIP_FLAG":True,
    "E_SERIES_STRIPPED_CHASSIS_MANUFACTURER_URL":"https://www.ford.ca/commercial-trucks/e-series-stripped-chassis/models/?gnav=vhpnav-specs",
    "E_SERIES_STRIPPED_CHASSIS_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/commercial-trucks/e-series-stripped-chassis/?gnav=header-commercial-vhp",
    "E_SERIES_STRIPPED_CHASSIS_DEALER_URL":"https://fordtodealers.ca/ford-e-series-stripped-chasis/",
    "E_SERIES_STRIPPED_CHASSIS_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-e-series-stripped-chasis/",

    "EDGE_SKIP_FLAG":False,
    "EDGE_MANUFACTURER_URL":"https://www.ford.ca/suvs-crossovers/edge/?gnav=header-suvs-vhp",
    "EDGE_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/suvs-crossovers/edge/?gnav=header-suvs-vhp",
    "EDGE_DEALER_URL":"https://fordtodealers.ca/ford-edge/",
    "EDGE_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-edge/",

    "ESCAPE_SKIP_FLAG":False,
    "ESCAPE_MANUFACTURER_URL":"https://www.ford.ca/suvs-crossovers/escape/?gnav=header-suvs-vhp",
    "ESCAPE_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/suvs-crossovers/escape/?gnav=header-suvs-vhp",
    "ESCAPE_DEALER_URL":"https://fordtodealers.ca/ford-escape/",
    "ESCAPE_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-escape/",

    "EXPEDITION_SKIP_FLAG":True,
    "EXPEDITION_MANUFACTURER_URL":"https://www.ford.ca/suvs/expedition/?gnav=header-suvs-vhp",
    "EXPEDITION_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/suvs/expedition/?gnav=header-suvs-vhp",
    "EXPEDITION_DEALER_URL":"https://fordtodealers.ca/ford-expedition/",
    "EXPEDITION_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-expedition/",

    "EXPLORER_SKIP_FLAG":True,
    "EXPLORER_MANUFACTURER_URL":"https://www.ford.ca/suvs/explorer/?gnav=header-suvs-vhp",
    "EXPLORER_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/suvs/explorer/?gnav=header-suvs-vhp",
    "EXPLORER_DEALER_URL":"https://fordtodealers.ca/ford-explorer/",
    "EXPLORER_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-explorer/",

    "F_SERIES_STRIPPED_CHASSIS_SKIP_FLAG":True,
    "F_SERIES_STRIPPED_CHASSIS_MANUFACTURER_URL":"https://www.ford.ca/commercial-trucks/f-series-stripped-chassis/models/?gnav=vhpnav-specs",
    "F_SERIES_STRIPPED_CHASSIS_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/commercial-trucks/f-series-stripped-chassis/?gnav=header-commercial-vhp",
    "F_SERIES_STRIPPED_CHASSIS_DEALER_URL":"https://fordtodealers.ca/ford-f-series-stripped-chasis/",
    "F_SERIES_STRIPPED_CHASSIS_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-f-series-stripped-chasis/",

    "F150_SKIP_FLAG":False,
    "F150_MANUFACTURER_URL":"https://www.ford.ca/trucks/f150/?gnav=header-trucks-vhp",
    "F150_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/trucks/f150/?gnav=header-trucks-vhp",
    "F150_DEALER_URL":"https://fordtodealers.ca/ford-f-150/",
    "F150_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-f-150/",

    "F150_COMMERCIAL_SKIP_FLAG":True,
    "F150_COMMERCIAL_MANUFACTURER_URL":"https://www.ford.ca/commercial-trucks/f150/?gnav=header-commercial-vhp",
    "F150_COMMERCIAL_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/commercial-trucks/f150/?gnav=header-commercial-vhp",
    "F150_COMMERCIAL_DEALER_URL":"https://fordtodealers.ca/ford-f-150-commercial/",
    "F150_COMMERCIAL_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-f-150-commercial/",

    "F150_LIGHTENING_SKIP_FLAG":True,
    "F150_LIGHTENING_MANUFACTURER_URL":"https://www.ford.ca/trucks/f150/f150-lightning/?gnav=header-trucks-vhp",
    "F150_LIGHTENING_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/trucks/f150/f150-lightning/?gnav=header-trucks-vhp",
    "F150_LIGHTENING_DEALER_URL":"https://fordtodealers.ca/ford-f150-lightning/",
    "F150_LIGHTENING_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-f150-lightning/",

    "F650_F750_SKIP_FLAG":True,
    "F650_F750_MANUFACTURER_URL":"https://www.ford.ca/commercial-trucks/f650-f750/?gnav=header-commercial-vhp",
    "F650_F750_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/commercial-trucks/f650-f750/?gnav=header-commercial-vhp",
    "F650_F750_DEALER_URL":"https://fordtodealers.ca/ford-f-650-f-750/",
    "F650_F750_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-f-650-f-750/",

    "MAVERICK_SKIP_FLAG":True,
    "MAVERICK_MANUFACTURER_URL":"https://www.ford.ca/trucks/maverick/?gnav=header-trucks-vhp",
    "MAVERICK_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/trucks/maverick/?gnav=header-trucks-vhp",
    "MAVERICK_DEALER_URL":"https://fordtodealers.ca/ford-maverick/",
    "MAVERICK_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-maverick/",

    "MUSTANG_SKIP_FLAG":False,
    "MUSTANG_MANUFACTURER_URL":"https://www.ford.ca/cars/mustang/?gnav=header-suvs-vhp",
    "MUSTANG_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/cars/mustang/?gnav=header-suvs-vhp",
    "MUSTANG_DEALER_URL":"https://fordtodealers.ca/ford-mustang/",
    "MUSTANG_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-mustang/",

    "MUSTANG_MACH_E_SKIP_FLAG":True,
    "MUSTANG_MACH_E_MANUFACTURER_URL":"https://www.ford.ca/suvs/mach-e/?gnav=vhpnav-overiew",
    "MUSTANG_MACH_E_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/suvs/mach-e/?gnav=vhpnav-overiew",
    "MUSTANG_MACH_E_DEALER_URL":"https://fordtodealers.ca/ford-mustang-mach-e/",
    "MUSTANG_MACH_E_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-mustang-mach-e/",

    "RANGER_SKIP_FLAG":True,
    "RANGER_MANUFACTURER_URL":"https://www.ford.ca/trucks/ranger/?gnav=header-trucks-vhp",
    "RANGER_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/trucks/ranger/?gnav=header-trucks-vhp",
    "RANGER_DEALER_URL":"https://fordtodealers.ca/ford-ranger/",
    "RANGER_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-ranger/",

    "SUPER_DUTY_SKIP_FLAG":True,
    "SUPER_DUTY_MANUFACTURER_URL":"https://www.ford.ca/trucks/super-duty/?gnav=header-trucks-vhp",
    "SUPER_DUTY_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/trucks/super-duty/?gnav=header-trucks-vhp",
    "SUPER_DUTY_DEALER_URL":"https://fordtodealers.ca/ford-super-duty-commercial/",
    "SUPER_DUTY_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-super-duty-commercial/",

    "SUPER_DUTY_COMMERCIAL_SKIP_FLAG":True,
    "SUPER_DUTY_COMMERCIAL_MANUFACTURER_URL":"https://www.ford.ca/commercial-trucks/super-duty/?gnav=header-commercial-vhp",
    "SUPER_DUTY_COMMERCIAL_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/commercial-trucks/super-duty/?gnav=header-commercial-vhp",
    "SUPER_DUTY_COMMERCIAL_DEALER_URL":"https://fordtodealers.ca/ford-super-duty-commercial/",
    "SUPER_DUTY_COMMERCIAL_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-super-duty-commercial/",

    "TRANSIT_SKIP_FLAG":True,
    "TRANSIT_MANUFACTURER_URL":"https://www.ford.ca/trucks/transit-passenger-van-wagon/?gnav=header-trucks-vhp",
    "TRANSIT_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/trucks/transit-passenger-van-wagon/?gnav=header-trucks-vhp",
    "TRANSIT_DEALER_URL":"https://fordtodealers.ca/ford-transit/",
    "TRANSIT_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-transit/",

    "TRANSIT_CC_CA_SKIP_FLAG":True,
    "TRANSIT_CC_CA_MANUFACTURER_URL":"https://www.ford.ca/commercial-trucks/transit-chassis/?gnav=header-commercial-vhp",
    "TRANSIT_CC_CA_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/commercial-trucks/transit-chassis/?gnav=header-commercial-vhp",
    "TRANSIT_CC_CA_DEALER_URL":"https://fordtodealers.ca/ford-transit-cc-ca/",
    "TRANSIT_CC_CA_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-transit-cc-ca/",

    "TRANSIT_COMMERCIAL_SKIP_FLAG":True,
    "TRANSIT_COMMERCIAL_MANUFACTURER_URL":"https://www.ford.ca/commercial-trucks/transit-cargo-van/?gnav=header-commercial-vhp",
    "TRANSIT_COMMERCIAL_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/commercial-trucks/transit-cargo-van/?gnav=header-commercial-vhp",
    "TRANSIT_COMMERCIAL_DEALER_URL":"https://fordtodealers.ca/ford-transit-commercial/",
    "TRANSIT_COMMERCIAL_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-transit-commercial/",

    "TRANSIT_CONNECT_SKIP_FLAG":True,
    "TRANSIT_CONNECT_MANUFACTURER_URL":"https://www.ford.ca/trucks/transit-connect-passenger-van-wagon/?gnav=header-trucks-vhp",
    "TRANSIT_CONNECT_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/trucks/transit-connect-passenger-van-wagon/?gnav=header-trucks-vhp",
    "TRANSIT_CONNECT_DEALER_URL":"https://fordtodealers.ca/ford-transit-connect/",
    "TRANSIT_CONNECT_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-transit-connect/",

    "TRANSIT_CONNECT_COMMERCIAL_SKIP_FLAG":True,
    "TRANSIT_CONNECT_COMMERCIAL_MANUFACTURER_URL":"https://www.ford.ca/commercial-trucks/transit-connect-cargo-van/?gnav=header-commercial-vhp",
    "TRANSIT_CONNECT_COMMERCIAL_MANUFACTURER_IMAGE_URL":"https://www.ford.ca/commercial-trucks/transit-connect-cargo-van/?gnav=header-commercial-vhp",
    "TRANSIT_CONNECT_COMMERCIAL_DEALER_URL":"https://fordtodealers.ca/ford-transit-connect/",
    "TRANSIT_CONNECT_COMMERCIAL_DEALER_IMAGE_URL":"https://fordtodealers.ca/ford-transit-connect/",
}