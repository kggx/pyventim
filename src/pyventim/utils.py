import pathlib
from typing import Dict, List, Any

import lxml, lxml.html
import json


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


def parse_json_from_component_html(html: str) -> List[Dict[str, Any]]:
    """This function returns all json entries on a component html string

    Args:
        html (str): HTML to look for json data

    Returns:
        Dict: Returns a list of dictionaries containing the json
    """
    return [
        json.loads(x.text)
        for x in lxml.html.fromstring(html).findall(
            ".//script[@type='application/ld+json']"
        )
    ]


def parse_has_next_page_from_component_html(html: str) -> bool:
    """This function returns if the returned page has a next page.

    Args:
        html (str): HTML code to check

    Returns:
        bool: Returns True if the page has a proceeding page.
    """
    return (
        len(lxml.html.fromstring(html).findall(".//button[@data-qa='next-page']")) == 0
    )


# <button
# class="btn btn-lg btn-square theme-interaction-border theme-interaction-bg standard-gray-border disabled"
# title="N&auml;chste Seite"
# data-qa="next-page"
# disabled
# >
# <i class="icon icon-arrow-right">
# <span class="sr-only">Nächste Seite</span>
# </i>
# </button>
