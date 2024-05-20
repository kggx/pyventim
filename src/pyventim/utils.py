import pathlib

# import lxml
# import json


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


# def get_attraction_music_events_from_html(html: str):
#     """This function returns all json entries on a html string

#     Args:
#         html (str): HTML to look for json data

#     Returns:
#         Dict: Returns a list of dictionaries containing the json
#     """
#     html_obj: lxml.ETree = lxml.html.fromstring(html)
#     return [
#         json.loads(x.text)
#         for x in html_obj.findall(".//script[@type='application/ld+json']")
#     ]
