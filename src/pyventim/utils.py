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


def parse_has_seatmap_from_event_html(html: str) -> bool:
    """This function checks if the html has a seatmap data compoenent

    Args:
        html (str): HTML to check

    Returns:
        bool: True if the html has a seatmapOptions string
    """
    return (
        len(
            lxml.html.fromstring(html).xpath(
                ".//script[@type='application/configuration' and contains(text(),'seatmapOptions')]"
            )
        )
        > 0
    )


def parse_seatmap_configuration_from_event_html(html: str) -> Dict:
    """This function parses the seatmap configuration from an event page.

    Args:
        html (str): HTML to parse

    Returns:
        Dict: Returns the extracted json data.
    """
    return json.loads(
        lxml.html.fromstring(html)
        .xpath(
            ".//script[@type='application/configuration' and contains(text(),'seatmapOptions')]"
        )[0]
        .text
    )


def parse_seathamp_data_from_api(seatmap_data: Dict) -> Dict:
    # pylint: disable=line-too-long
    """This function parses the eventim seatmap data in a more readable format

    Args:
        seatmap_data (Dict): Raw seatmap data returned by a eventim event page.

    Returns:
        Dict: Seat map data in a readable format. Seatmap meta and seats in the format "Block -> Row -> Seat"
    """
    blocks = []
    for block in seatmap_data["blocks"]:
        rows = []
        for row in block["rows"]:
            seats = []
            for seat in row[1]:
                seats.append(
                    dict(
                        seat_code=seat[0],
                        seat_price_category_index=seat[1],
                        seat_coordinate_x=seat[2],
                        seat_coordinate_y=seat[3],
                    )
                )
                # End of seat

            rows.append(dict(row_code=row[0], row_seats=seats))
            # End of row

        blocks.append(
            dict(
                block_id=block["blockId"],
                block_name=block["name"],
                block_description=block["blockDescription"],
                block_rows=rows,
            )
        )
        # End of block

    # Parse pricing categories
    price_categories = [
        dict(
            price_category_id=x[0], price_category_name=x[1], price_category_color=x[2]
        )
        for x in seatmap_data["pcs"]
    ]

    # Return the final seatmap
    seatmap = dict(
        seatmap_key=seatmap_data["key"],
        seatmap_timestamp=seatmap_data["availabilityTimestamp"],
        seatmap_individual_seats=seatmap_data["individualSeats"],
        seatmap_dimension_x=seatmap_data["dimension"][0],
        seatmap_dimension_y=seatmap_data["dimension"][1],
        seatmap_seat_size=seatmap_data["seatSize"],
        blocks=blocks,
        price_categories=price_categories,
    )

    return seatmap


def parse_seatmap_url_params_from_seatmap_information(options: dict) -> Dict:
    """This function builds a private signed api url from the obtained seatmap information.

    Args:
        options (dict): Options to be processed

    Returns:
        Dict: Dictionary containing key, value pairs for the request
    """
    params = {
        param.split("=")[0]: param.split("=")[1]
        for param in options["additionalRequestParams"][1:].split("&")
    }
    # Add additional parmeter to the params
    params["cType"] = options["cType"]
    params["evId"] = options["evId"]
    params["cId"] = options["cId"]
    params["fun"] = "json"

    return params
