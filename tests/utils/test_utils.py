# pylint: skip-file
from typing import List, Dict

# Module to test
import pyventim.utils
import pyventim.adapters


def test_parse_city_name_from_link():
    url = "https://www.eventim.de/city/hamburg-7/venue/stage-theater-im-hafen-hamburg-3880"
    assert pyventim.utils.parse_city_name_from_link(city_url=url) == "hamburg"


def test_parse_city_id_from_link():
    url = "https://www.eventim.de/city/hamburg-7/venue/stage-theater-im-hafen-hamburg-3880"
    assert pyventim.utils.parse_city_id_from_link(city_url=url) == 7


def test_parse_list_from_component_html():
    adapter = pyventim.adapters.HtmlAdapter()
    result = adapter.get(
        endpoint="component",
        params={
            "doc": "component",
            "esid": 473431,
            "fun": "eventselectionbox",
            "pnum": 1,
        },
    )
    attractions = pyventim.utils.parse_list_from_component_html(result.html_data)
    assert isinstance(attractions, List)
    for attraction in attractions:
        assert isinstance(attraction, Dict)


def test_parse_calendar_from_component_html():
    adapter = pyventim.adapters.HtmlAdapter()
    result = adapter.get(
        endpoint="component",
        params={
            "doc": "component",
            "esid": 473431,
            "fun": "eventselectionbox",
            "pnum": 1,
        },
    )
    calendar_config = pyventim.utils.parse_calendar_from_component_html(
        result.html_data
    )
    assert isinstance(calendar_config, Dict)

    calendar_content = calendar_config["calendar_content"]
    assert isinstance(calendar_content, Dict)

    attractions = calendar_content["result"]
    assert isinstance(attractions, List)

    for attraction in attractions:
        assert isinstance(attraction, Dict)


def test_parse_has_next_page_from_component_html():
    adapter = pyventim.adapters.HtmlAdapter()
    result = adapter.get(
        endpoint="component",
        params={
            "doc": "component",
            "esid": 473431,
            "fun": "eventselectionbox",
            "pnum": 1,
        },
    )
    assert isinstance(
        pyventim.utils.parse_has_next_page_from_component_html(result.html_data), bool
    )

    pass
