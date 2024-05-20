# pylint: skip-file
import pytest

# Module to test
from pyventim import utils


def test_parse_city_name_from_link():
    url = "https://www.eventim.de/city/hamburg-7/venue/stage-theater-im-hafen-hamburg-3880"
    expected_name = "hamburg"
    returned_name = utils.parse_city_name_from_link(city_url=url)


def test_parse_city_id_from_link():
    url = "https://www.eventim.de/city/hamburg-7/venue/stage-theater-im-hafen-hamburg-3880"
    expected_name = 1
    returned_name = utils.parse_city_id_from_link(city_url=url)
