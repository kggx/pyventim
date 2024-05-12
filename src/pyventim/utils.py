import requests
import pathlib
from typing import Dict, Any


def parse_city_name_from_link(city_url: str) -> str:
    """Given a link like "https://www.eventim.de/city/hamburg-7/venue/stage-theater-im-hafen-hamburg-3880": This function will return the city name.

    Args:
        city_url (str): Link to parse

    Returns:
        str: The city name from the url.
    """
    return pathlib.Path(city_url).parts[3].split("-")[0]


def parse_city_id_from_link(city_url: str) -> int:
    """Given a link like "https://www.eventim.de/city/hamburg-7/venue/stage-theater-im-hafen-hamburg-3880": This function returns the city id.

    Args:
        city_url (str): Link to parse

    Returns:
        int: The city id from the url.
    """
    return pathlib.Path(city_url).parts[3].split("-")[1]
