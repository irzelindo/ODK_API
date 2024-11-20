# Import configparser to get all the variables from the config file
import configparser
import os

print(__name__)

# Get the path to the config file
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "config.ini"))

# Get the path to the data directory
ODK_SERVER_URL = config["ODK"]["ODK_SERVER_URL"]
ODK_USERNAME = config["ODK"]["ODK_USERNAME"]
ODK_PASSWORD = config["ODK"]["ODK_PASSWORD"]
