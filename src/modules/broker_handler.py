import os
from smartapi import SmartConnect
from dotenv import load_dotenv

# This file will contain the generic broker module.
# It will handle the connection to the broker's API.

def initialize_api_connector():
    """
    Initializes the API connector for Angel One.

    Loads the API key from the .env file and creates an instance of SmartConnect.

    Returns:
        SmartConnect: An instance of the SmartConnect class if the API key is found.
        None: If the API key is not found in the .env file.
    """
    load_dotenv()
    api_key = os.getenv("ANGEL_API_KEY")
    if api_key:
        return SmartConnect(api_key=api_key)
    else:
        return None
