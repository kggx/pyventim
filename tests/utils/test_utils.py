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


def test_parse_seatmap_url_params_from_seatmap_information():
    options = {
        "cType": "web",
        "cId": 1,
        "evId": 16828914,
        "additionalRequestParams": "&a_systemId=1&a_promotionId=0&a_sessionId=EVE_NO_SESSION&timestamp=28611964&expiryTime=28611974&chash=L_itK5sj-4&signature=yGTajJUzWiNtRSGzif1ajavSfxKMBfIKiSDyQfjXaGg",
        "holds": True,
        "drawMarker": True,
        "useCommonBackground": True,
        "onlyOnePcBookable": False,
        "server": "https://api.eventim.com",
        "seatThreshold": 2500,
        "skipHulls": True,
        "stage": {"mode": "drag", "iconUrl": "../images/green_arrow.png"},
        "shopLogoPath": "/obj/media/DE-eventim/specialLogos/checkoutApp/logo_blue_01.svg",
    }

    params = pyventim.utils.parse_seatmap_url_params_from_seatmap_information(options)
    assert isinstance(params, Dict)

    required_keys = [
        "cType",
        "evId",
        "cId",
        "fun",
        "a_sessionId",
        "timestamp",
        "expiryTime",
        "chash",
        "signature",
    ]

    for key in required_keys:
        assert key in list(params.keys())


def test_parse_has_seatmap_from_event_html():
    html_adapter = pyventim.adapters.HtmlAdapter()
    html_result = html_adapter.get(
        endpoint=f"event/disneys-der-koenig-der-loewen-stage-theater-im-hafen-hamburg-18500464/",
        params=None,
    )
    assert (
        pyventim.utils.parse_has_seatmap_from_event_html(html_result.html_data) == True
    )

    html_adapter = pyventim.adapters.HtmlAdapter()
    html_result = html_adapter.get(
        endpoint=f"event/beartooth-sporthalle-hamburg-17585252/",
        params=None,
    )
    assert (
        pyventim.utils.parse_has_seatmap_from_event_html(html_result.html_data) == False
    )


def test_parse_seatmap_configuration_from_event_html():
    html_adapter = pyventim.adapters.HtmlAdapter()
    html_result = html_adapter.get(
        endpoint=f"event/disneys-der-koenig-der-loewen-stage-theater-im-hafen-hamburg-18500464/",
        params=None,
    )

    result = pyventim.utils.parse_seatmap_configuration_from_event_html(
        html_result.html_data
    )
    assert isinstance(result, Dict)
    assert sorted(list(result.keys())) == sorted(
        [
            "fansale",
            "seatmapOptions",
            "seatmapIsDefault",
            "packageData",
            "price",
            "maxAmountForEvent",
            "minAmountForEvent",
            "maxAmountForPromo",
            "preselectedPcId",
            "showBackLink",
            "backLink",
            "eventName",
            "restrictions",
            "cartData",
            "panoramaOptions",
            "imageviewerOptions",
            "ccEnabled",
            "initialRequestPath",
            "captchaActive",
            "captchaAPIPath",
            "captchaSiteKey",
            "pcFlyoutExpanded",
            "pcUpgradeActiveClass",
            "pricePlaceholder",
            "hasPriceDisclaimerHint",
            "hasCorporateBenefits",
            "hasCombinedTicketTypes",
            "hasAllCategoriesToggleText",
            "reducedAvailabilityWidgetLink",
            "hasOptionsFilter",
            "ticketTypeFilterMap",
            "api",
            "useParis24Styles",
            "messages",
        ]
    )

    # Value check on backLink & name
    assert (
        result["backLink"]
        == "/event/disneys-der-koenig-der-loewen-stage-theater-im-hafen-hamburg-18500464/"
    )
    assert result["eventName"] == "Disneys DER K\u00d6NIG DER L\u00d6WEN"


def test_parse_seathamp_data_from_api():
    dummy_block = {
        "blockId": "b1",
        "name": "Parkett links",
        "blockDescription": "Parkett links",
        "rows": [["r2", [["s260", 0, 3783, 1471]]]],
    }

    seatmap_data = {
        "key": "web_1_16825147_0_EVE_0",
        "availabilityTimestamp": 1716215061170,
        "individualSeats": 2051,
        "dimension": [4096, 4096],
        "seatSize": 59,
        "blocks": [dummy_block],
        "pcs": [["p32914323", "Kat. 1 Premium", "#f1075e", "#ffffff"]],
    }
    result = pyventim.utils.parse_seathamp_data_from_api(seatmap_data)

    assert isinstance(result, Dict)
    assert sorted(list(result.keys())) == sorted(
        [
            "seatmap_key",
            "seatmap_timestamp",
            "seatmap_individual_seats",
            "seatmap_dimension_x",
            "seatmap_dimension_y",
            "seatmap_seat_size",
            "blocks",
            "price_categories",
        ]
    )

    # Value checks
    assert result["seatmap_key"] == "web_1_16825147_0_EVE_0"
    assert result["seatmap_timestamp"] == 1716215061170
    assert result["seatmap_individual_seats"] == 2051

    assert result["seatmap_dimension_x"] == 4096
    assert result["seatmap_dimension_y"] == 4096
    assert result["seatmap_seat_size"] == 59

    # Block
    block = result["blocks"][0]
    assert block["block_id"] == "b1"
    assert block["block_name"] == "Parkett links"
    assert block["block_description"] == "Parkett links"

    # Row
    row = block["block_rows"][0]
    assert row["row_code"] == "r2"

    seat = row["row_seats"][0]
    assert seat["seat_code"] == "s260"
    assert seat["seat_price_category_index"] == 0
    assert seat["seat_coordinate_x"] == 3783
    assert seat["seat_coordinate_y"] == 1471

    # Price Categories
    price_category = result["price_categories"][0]
    assert price_category["price_category_id"] == "p32914323"
    assert price_category["price_category_name"] == "Kat. 1 Premium"
    assert price_category["price_category_color"] == "#f1075e"
