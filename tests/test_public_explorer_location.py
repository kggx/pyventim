# pylint: skip-file

import pytest
import datetime
from typing import Dict, List, Any

# Module to test
from pyventim.public import EventimExploration

# Setup
# We are testing against a long running german musical prone NOT to change
SEARCH_TERM = "Stage Theater im Hafen Hamburg"
SORT = "DateAsc"

EXPLORER: EventimExploration = EventimExploration()
RESULT = EXPLORER.explore_locations(
    search_term=SEARCH_TERM,
    sort=SORT,
)


############################
### API validation tests ###
############################
# Make a sample request and reuse the result to verify varous components
def test_request_successfull():
    excepted_keys = [
        "locations",
        "results",
        "totalResults",
        "page",
        "totalPages",
        "_links",
    ]

    assert isinstance(RESULT, Dict)
    assert (key in excepted_keys for key in RESULT.keys())


def test_request_location_id():
    # Get the first as this should be the only result
    excepted_id = "vg_3880"
    RESULT["locations"][0]["locationId"] = excepted_id


def test_request_location_city():
    # Get the first as this should be the only result
    excepted_id = "Hamburg"
    RESULT["locations"][0]["city"] = excepted_id
