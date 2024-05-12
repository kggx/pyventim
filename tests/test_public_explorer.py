# pylint: skip-file

import pytest
import datetime
from typing import Dict, List, Any

# Module to test
from pyventim.public import EventimExploration

# Setup
SEARCH_TERM = "The"
CATEGORIES = ["Musical & Show|Musical"]
CITY_IDS = [7]  # Hamburg
SORT = "DateAsc"
INSTOCK = False

NOW = datetime.datetime.now()
CURRENT_TIME = datetime.time(NOW.hour, NOW.minute, NOW.second)
TODAY = datetime.date.today()
NEXT_WEEK = TODAY + datetime.timedelta(days=7)


########################################
### Query parameter validation tests ###
########################################
def test_validate_required_parameters():
    explorer: EventimExploration = EventimExploration()
    with pytest.raises(
        ValueError,
        match="Must have search_term, categories or city_ids in the query parameters!",
    ):
        explorer.validate_required_parameters()

    assert (
        explorer.validate_required_parameters(search_term="Sample search term...")
        is True
    )


def test_validate_page_parameter():  # pylint: disable=C0116
    explorer: EventimExploration = EventimExploration()
    with pytest.raises(
        ValueError,
        match="page must be a positive integer!",
    ):
        explorer.validate_page_parameter("2")
        explorer.validate_page_parameter(-1)

    assert explorer.validate_page_parameter(1)
    assert explorer.validate_page_parameter(10)


def test_validate_sort_parameter():
    explorer: EventimExploration = EventimExploration()
    with pytest.raises(
        ValueError,
        match="sort must match: DateAsc, DateDesc, NameAsc, NameDesc, Rating, Recommendation",
    ):
        explorer.validate_sort_parameter("This is not a valid sort value.")

    assert explorer.validate_sort_parameter("DateAsc")
    assert explorer.validate_sort_parameter("DateDesc")
    assert explorer.validate_sort_parameter("NameAsc")
    assert explorer.validate_sort_parameter("NameDesc")
    assert explorer.validate_sort_parameter("Rating")
    assert explorer.validate_sort_parameter("Recommendation")


def test_validate_search_term_parameter():  # pylint: disable=C0116
    explorer: EventimExploration = EventimExploration()
    with pytest.raises(
        ValueError,
        match="search_term must have atleast two characters!",
    ):
        explorer.validate_search_term_parameter("2")

    assert explorer.validate_search_term_parameter(SEARCH_TERM)


def test_validate_categories_parameter():
    explorer: EventimExploration = EventimExploration()
    with pytest.raises(ValueError, match="categories must be a list of strings!"):
        explorer.validate_categories_parameter("This is not category value.")
        explorer.validate_categories_parameter(["This is valid", False])

    assert explorer.validate_categories_parameter(CATEGORIES)


def test_validate_city_ids_parameter():
    explorer: EventimExploration = EventimExploration()
    with pytest.raises(ValueError, match="city_ids must be a list of integers!"):
        explorer.validate_city_ids_parameter("This is not category value.")
        explorer.validate_city_ids_parameter(["This is not valid valid", 123])

    assert explorer.validate_city_ids_parameter(CITY_IDS)


def test_validate_date_from_parameter():
    explorer: EventimExploration = EventimExploration()
    with pytest.raises(ValueError, match="date_from must be of type datetime.date!"):
        explorer.validate_date_from_parameter("This is not a valid value.")

    assert explorer.validate_date_from_parameter(TODAY)


def test_validate_date_to_parameter():
    explorer: EventimExploration = EventimExploration()
    with pytest.raises(ValueError, match="date_to must be of type datetime.date!"):
        explorer.validate_date_to_parameter("This is not a valid value.")

    assert explorer.validate_date_to_parameter(TODAY)


def test_validate_time_from_parameter():
    explorer: EventimExploration = EventimExploration()
    with pytest.raises(ValueError, match="time_from must be of type datetime.time!"):
        explorer.validate_time_from_parameter("This is not a valid value.")

    assert explorer.validate_time_from_parameter(CURRENT_TIME)


def test_validate_time_to_parameter():
    explorer: EventimExploration = EventimExploration()
    with pytest.raises(ValueError, match="time_to must be of type datetime.time!"):
        explorer.validate_time_to_parameter("This is not a valid value.")

    assert explorer.validate_time_to_parameter(CURRENT_TIME)


def test_validate_in_stock_parameter():
    explorer: EventimExploration = EventimExploration()
    with pytest.raises(ValueError, match="in_stock must be of type bool!"):
        explorer.validate_in_stock_parameter("This is not a valid value.")

    assert explorer.validate_in_stock_parameter(INSTOCK)


######################################
### Query builder validation tests ###
######################################
def test_build_query_parameters():
    explorer: EventimExploration = EventimExploration()
    inputs = {
        "search_term": SEARCH_TERM,
        "date_from": TODAY,
        "date_to": NEXT_WEEK,
        "categories": CATEGORIES,
        "in_stock": None,
        "not_defined_key": "sample_value",
    }

    params: Dict[str, Any] = explorer.build_query_parameters(**inputs)
    assert isinstance(params, Dict)

    # Check if expected keys are present
    for key in params.keys():
        assert key in [
            "search_term",
            "date_from",
            "date_to",
            "categories",
            "not_defined_key",
        ]

    # Check if a not defined key is in the dictionary
    assert params["not_defined_key"] == "sample_value"

    # Check if empty value is not in the param
    assert "in_stock" not in params.keys()
