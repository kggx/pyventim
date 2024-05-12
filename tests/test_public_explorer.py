import pytest
import datetime
from typing import Dict

# Module to test
from pyventim.public import EventimExploration

# Setup
explorer: EventimExploration = EventimExploration()
search_term = "Disneys DER KÖNIG DER LÖWEN"
categories = ["Musical & Show|Musical"]
days = 7
sort = "DateAsc"
in_stock = False

now = datetime.datetime.now()
current_time = datetime.time(now.hour, now.minute, now.second)
today = datetime.date.today()
next_week = today + datetime.timedelta(days=7)


# def test_explore_content():
#     # We check for needed keys
#     needed_keys = ['content', 'results', 'totalResults', 'page', 'totalPages', '_links']
#     json = explorer.explore_content(search_term)
#     assert(x in needed_keys for x in json.keys())

# def test_explore_attractions():
#     # We check for needed keys
#     needed_keys = ['attractions', 'results', 'totalResults', 'page', 'totalPages', '_links']
#     json = explorer.explore_attractions(search_term)
#     assert(x in needed_keys for x in json.keys())

# def test_explore_locations():
#     # We check for needed keys
#     needed_keys = ['locations', 'results', 'totalResults', 'page', 'totalPages', '_links']
#     json = explorer.explore_locations(search_term)
#     assert(x in needed_keys for x in json.keys())


def test_explore_product_groups():
    json = explorer.explore_product_groups(
        search_term=search_term,
        categories=categories,
        date_from=today,
        date_to=next_week,
        sort=sort,
        in_stock=in_stock,
    )

    # We check for needed keys
    needed_keys = [
        "productGroups",
        "results",
        "totalResults",
        "page",
        "totalPages",
        "_links",
    ]
    json = explorer.explore_product_groups(search_term)
    assert (x in needed_keys for x in json.keys())


# Query parameter validation tests
def test_build_query_parameters_required_parameters():
    with pytest.raises(
        ValueError,
        match="Must have search_term, categories or city_ids in the query parameters!",
    ):
        explorer._build_query_parameters()


def test_build_query_parameters_page_parameter():
    with pytest.raises(ValueError, match="page must be a positive integer > 0!"):
        explorer._build_query_parameters(search_term=search_term, page=-1)

    assert isinstance(
        explorer._build_query_parameters(search_term=search_term, page=1), Dict
    )


def test_build_query_parameters_sort_parameter():
    with pytest.raises(
        ValueError,
        match='sort must be one of the following values: "DateAsc", "DateDesc", "NameAsc", "NameDesc", "Rating", "Recommendation"!',
    ):
        explorer._build_query_parameters(search_term="ABC", sort="This should fail.")

    assert isinstance(
        explorer._build_query_parameters(search_term=search_term, sort=sort), Dict
    )


def test_build_query_parameters_search_term_parameter():
    with pytest.raises(
        ValueError, match="search_term must have atleast two characters!"
    ):
        explorer._build_query_parameters(search_term="A")

    assert isinstance(explorer._build_query_parameters(search_term=search_term), Dict)


def test_build_query_parameters_categories_parameter():
    with pytest.raises(ValueError, match="categories must be a list of strings!"):
        explorer._build_query_parameters(categories="abcs")

    with pytest.raises(ValueError, match="categories must be a list of strings!"):
        explorer._build_query_parameters(categories=[123, "abcs"])

    with pytest.raises(ValueError, match="categories must be a list of strings!"):
        explorer._build_query_parameters(categories=[123, 234])

    assert isinstance(explorer._build_query_parameters(categories=categories), Dict)


def test_build_query_parameters_city_ids_parameter():
    with pytest.raises(ValueError, match="city_ids must be a list of integers!"):
        explorer._build_query_parameters(city_ids=123)

    with pytest.raises(ValueError, match="city_ids must be a list of integers!"):
        explorer._build_query_parameters(city_ids=[123, "abcs"])

    with pytest.raises(ValueError, match="city_ids must be a list of integers!"):
        explorer._build_query_parameters(city_ids=["123", "234"])

    assert isinstance(explorer._build_query_parameters(city_ids=[1]), Dict)


def test_build_query_parameters_date_from_parameter():
    with pytest.raises(ValueError, match="date_from must be of type date!"):
        explorer._build_query_parameters(
            search_term=search_term, date_from="Not a valid date"
        )

    assert isinstance(
        explorer._build_query_parameters(search_term=search_term, date_from=today), Dict
    )


def test_build_query_parameters_date_to_parameter():
    with pytest.raises(ValueError, match="date_to must be of type date!"):
        explorer._build_query_parameters(
            search_term=search_term, date_to="Not a valid date"
        )

    assert isinstance(
        explorer._build_query_parameters(search_term=search_term, date_to=today), Dict
    )


def test_build_query_parameters_time_from_parameter():
    with pytest.raises(ValueError, match="time_from must be of type time!"):
        explorer._build_query_parameters(
            search_term=search_term, time_from="Not a valid time"
        )

    assert isinstance(
        explorer._build_query_parameters(
            search_term=search_term, time_from=current_time
        ),
        Dict,
    )


def test_build_query_parameters_time_to_parameter():
    with pytest.raises(ValueError, match="time_to must be of type time!"):
        explorer._build_query_parameters(
            search_term=search_term, time_to="Not a valid time"
        )

    assert isinstance(
        explorer._build_query_parameters(search_term=search_term, time_to=current_time),
        Dict,
    )


def test_build_query_parameters_in_stock_parameter():
    with pytest.raises(ValueError, match="in_stock must be of type bool!"):
        # Variable should be a list.
        explorer._build_query_parameters(
            search_term=search_term, in_stock="This is not a valid boolean"
        )
