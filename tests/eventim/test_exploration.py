"""Module to test the highlevel eventim.Eventim exploration methods"""

from typing import Dict, Iterator

import pytest
import pydantic
from pyventim import Eventim  # pylint: disable=E0401


EVENTIM = Eventim()
# We are testing against a long running german musical prone NOT to change with a known theater
LOCATION = "Stage Theater im Hafen Hamburg"
ATTRACTION = "Disneys DER KÖNIG DER LÖWEN"
SORT = "DateAsc"


def test_attractions_success():
    """Tests the attractions on a fixed attraction"""
    # Check the overall result to be a iterator
    result = EVENTIM.explore_attractions(ATTRACTION)
    assert isinstance(result, Iterator)

    # Item check
    first_item = next(result)
    assert isinstance(first_item, Dict)
    assert sorted(list(first_item.keys())) == sorted(
        [
            "attractionId",
            "name",
            "description",
            "link",
            "url",
            "imageUrl",
            "rating",
        ]
    )

    # Value check on attraction id
    assert first_item["attractionId"] == "450962"


def test_attractions_failure():
    """Test a attractions failure with a short search_term"""
    with pytest.raises(
        pydantic.ValidationError,
        match="search_term must be atleast 3 characters long",
    ):
        list(EVENTIM.explore_attractions("a"))


def test_locations_success():
    """Tests the locations on a fixed location"""
    # Check the overall result to be a iterator
    result = EVENTIM.explore_locations(LOCATION)
    assert isinstance(result, Iterator)

    # Item check
    first_item = next(result)

    assert isinstance(first_item, Dict)
    assert sorted(list(first_item.keys())) == sorted(
        [
            "locationId",
            "name",
            "description",
            "city",
            "link",
            "url",
            "imageUrl",
            "rating",
        ]
    )

    # Value check on location id
    assert first_item["locationId"] == "vg_3880"


def test_locations_failure():
    """Test a failure with a short search_term"""
    with pytest.raises(
        pydantic.ValidationError,
        match="search_term must be atleast 3 characters long",
    ):
        list(EVENTIM.explore_locations("a"))


def test_product_group_success():
    """Tests the product_groups on a fixed attraction"""
    # Check the overall result to be a iterator
    result = EVENTIM.explore_product_groups(ATTRACTION)
    assert isinstance(result, Iterator)

    # Item check
    first_item = next(result)
    assert isinstance(first_item, Dict)
    assert sorted(list(first_item.keys())) == sorted(
        [
            "productGroupId",
            "name",
            "description",
            "startDate",
            "endDate",
            "productCount",
            "link",
            "url",
            "imageUrl",
            "currency",
            "rating",
            "categories",
            "tags",
            "status",
            "products",
        ]
    )

    # Value check on product_group id
    assert first_item["productGroupId"] == "473431"


def test_product_group_failure():
    """Test a failure with multiple known cases"""
    # Missing one of the required parameters
    with pytest.raises(
        pydantic.ValidationError,
        match="Must have either search_term, categories or city_ids",
    ):
        list(EVENTIM.explore_product_groups(sort=SORT))

    # Too short searchterm
    with pytest.raises(
        pydantic.ValidationError,
        match="search_term must be atleast 3 characters long",
    ):
        list(EVENTIM.explore_product_groups("a"))
