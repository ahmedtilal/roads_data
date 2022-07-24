import os
import xml.etree.ElementTree as ET
import pandas as pd
import requests


def get_df_from_xml_url(url: str) -> pd.DataFrame:
    """
    Fetches the xml data from the url endpoint and returns it in a Pandas DataFrame format.

    Args:
        url (str): Endpoint url.

    Returns:
        DataFrame: Dataframe containing the fetched data.
    """    
    response = requests.get(url)
    tree = ET.ElementTree(ET.fromstring(response.content))
    root = tree.getroot()
    root = root[0][0]

    data_list = []

    for child in root:
        data_list.append(child.attrib)

    df = pd.DataFrame.from_records(data_list)
    return df


def save_xml_to_file_from_url(url: str, file_path: str = None) -> None:
    """
    Retrieves the xml string from the url endpoint and saves it in the passed file path or to xml_files_from_endpoint_directory if no path is passed to the function.

    The saved file is named the same as the last string in the endpoint (usually the file name).

    Args:
        url (str): The url that points to the file.
        file_path (str, optional): Optional argument if the file is desired to be saved in another directory. Defaults to None.
    """
    pwd = os.path.abspath(os.path.join(os.pardir))
    saving_dir = os.path.join(pwd, "xml_files_from_endpoint")
    file_name = url.split("/")[-1]
    response = requests.get(url)
    if file_path is None:
        file_path = os.path.join(saving_dir, file_name)
    with open(file_path, "wb") as file:
        file.write(response.content)