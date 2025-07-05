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

def login_and_generate_session(connector):
    """
    Logs in to Angel One and generates a session.

    Args:
        connector: An instance of the SmartConnect class.

    Returns:
        dict: The user's profile data if login is successful.
        None: If login fails or an exception occurs.
    """
    load_dotenv()
    client_id = os.getenv("ANGEL_CLIENT_ID")
    password = os.getenv("ANGEL_PASSWORD")
    totp = os.getenv("ANGEL_TOTP")

    try:
        data = connector.generateSession(client_id, password, totp)
        if data['status'] and data['data']:
            return data['data']
        else:
            print(f"Error during session generation: {data['message']}")
            return None
    except Exception as e:
        print(f"Exception during login: {e}")
        return None
