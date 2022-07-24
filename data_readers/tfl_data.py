import requests, json
import pandas as pd

# This file fetches the data from the Transport for London API(Tfl).
# Found at https://api-portal.tfl.gov.uk/apis.

def get_json_data(url: str) -> list[dict] | bool:
    """
    Fetches the json string from the API endpoint.
    
    Returns False if there is an issue fetching the API and logs the Exception.

    Args:
        url (str): API endpoint url.

    Returns:
        list[dict]: list of dictionaries representing the data fetched from the url.
    """    
    try:
        hdr ={
        # Request headers
        'Cache-Control': 'no-cache',
        }

        response = requests.get(url, headers=hdr)
    except Exception as e:
        print(e)
        return False
    return response.json()

def convert_json_to_df(json: list) -> pd.DataFrame:
    """
    Converts the json records to a Pandas Dataframe.

    Args:
        json (list): records list.

    Returns:
        pd.DataFrame: data in the form of Dataframe.
    """    
    return pd.DataFrame.from_records(json)

def get_df_from_endpoint(url: str) -> pd.DataFrame | bool:
    """
    Gets the data from the API endpoint in the form of Pandas DataFrame or returns False if there is an issue.

    Args:
        url (str): _description_

    Returns:
        pd.DataFrame | bool: _description_
    """    
    json = get_json_data(url)
    if json:
        return convert_json_to_df(json)
    else:
        return False