# pylint: skip-file

import pytest
import datetime
from typing import Dict, List, Any

# Module to test
from pyventim.public import EventimExploration

# Setup
# We are testing against a long running german musical prone NOT to change
SEARCH_TERM = "Disneys DER KÖNIG DER LÖWEN"
CATEGORIES = ["Musical & Show|Musical"]
SORT = "DateAsc"

TODAY = datetime.date.today()
NEXT_YEAR = TODAY + datetime.timedelta(days=365)

EXPLORER: EventimExploration = EventimExploration()
RESULT = EXPLORER.explore_product_groups(
    search_term=SEARCH_TERM,
    categories=CATEGORIES,
    date_from=TODAY,
    date_to=NEXT_YEAR,
    sort=SORT,
)


############################
### API validation tests ###
############################
# Make a sample request and reuse the result to verify varous components
def test_request_successfull():
    excepted_keys = [
        "productGroups",
        "results",
        "totalResults",
        "page",
        "totalPages",
        "_links",
    ]

    assert isinstance(RESULT, Dict)
    assert (key in excepted_keys for key in RESULT.keys())


def test_request_product_group_id():
    # Get the first as this should be the only result
    excepted_id = 473431
    RESULT["productGroups"][0]["productGroupId"] = excepted_id


def test_request_product_group_categories():
    # Get the first as this should be the only result and check against known categories
    excepted_categories = ["Musical & Show", "Musical"]

    assert (
        category in excepted_categories
        for category in RESULT["productGroups"][0]["categories"]
    )


def test_page_product_group_request():
    excepted_page = 2

    page_result = EXPLORER.explore_product_groups(
        search_term="The",
        page=2,
        sort=SORT,
    )

    page_result["page"] = excepted_page
