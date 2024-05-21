"""Common utility functions for pyventim"""

import json
import pathlib
from typing import Dict, List, Any

import lxml
import lxml.html


def parse_city_name_from_link(city_url: str) -> str:
    """This function returns the city name given a link like:
    "https://www.eventim.de/city/hamburg-7/venue/stage-theater-im-hafen-hamburg-3880"

    Args:
        city_url (str): Link to parse

    Returns:
        str: The city name from the url.
    """
    return pathlib.Path(city_url).parts[3].split("-")[0]


def parse_city_id_from_link(city_url: str) -> int:
    """This function returns the city id given a link like:
    "https://www.eventim.de/city/hamburg-7/venue/stage-theater-im-hafen-hamburg-3880"

    Args:
        city_url (str): Link to parse

    Returns:
        int: The city id from the url.
    """
    return int(pathlib.Path(city_url).parts[3].split("-")[1])


def parse_list_from_component_html(html: str) -> List[Dict[str, Any]]:
    """This function returns all json entries on a component html string

    Args:
        html (str): HTML to look for json data

    Returns:
        Dict: Returns a list of dictionaries containing the data
    """
    return [
        json.loads(x.text)
        for x in lxml.html.fromstring(html).findall(
            ".//script[@type='application/ld+json']"
        )
    ]


def parse_calendar_from_component_html(html: str) -> Dict[str, Any]:
    """This function returns the calendar widget data entries of a component html string

    Args:
        html (str): HTML to look for json data

    Returns:
        Dict: Returns a dict with the calendar widget data
    """
    return json.loads(
        lxml.html.fromstring(html)
        .xpath(
            ".//script[@type='application/configuration' and contains(text(),'calendar_content')]"
        )[0]
        .text
    )


def parse_has_next_page_from_component_html(html: str) -> bool:
    """Returns if the page has a proceeding page

    Args:
        html (str): HTML to parse

    Returns:
        bool: Returns true if followed by another page.
    """
    matches = lxml.html.fromstring(html).xpath(
        ".//li[contains(@class,'pagination-pages-small') and contains(text(),' von ')]"
    )
    for match in matches:
        current, total = match.text.split(" von ")
        return current < total

    return False


def parse_seatmap_configuration_from_event_html(html: str):
    matches = lxml.html.fromstring(html).xpath(
        ".//script[@type='application/configuration' and contains(text(),'seatmapOptions')]"
    )
    if len(matches) > 0:
        return json.loads(matches[0].text)

    else:
        return None
