from typing import Dict

import pytest
import pydantic
from pyventim import Eventim  # pylint: disable=E0401


EVENTIM = Eventim()
EVENT_URL = (
    "/event/disneys-der-koenig-der-loewen-stage-theater-im-hafen-hamburg-18500464/"
)


def test_get_event_seatmap_information():
    result = EVENTIM.get_event_seatmap_information(EVENT_URL)
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


def test_get_event_seatmap():
    # Get the event
    result = EVENTIM.get_event_seatmap_information(EVENT_URL)
    assert isinstance(result, Dict)

    seatmap = EVENTIM.get_event_seatmap(result["seatmapOptions"])
    assert isinstance(seatmap, Dict)
    assert sorted(list(seatmap.keys())) == sorted(
        [
            "seatmap_key",
            "seatmap_timestamp",
            "seatmap_individual_seats",
            "blocks",
            "price_categories",
        ]
    )

    # Check block
    first_block = seatmap["blocks"][0]
    assert isinstance(first_block, Dict)
    assert sorted(list(first_block.keys())) == sorted(
        [
            "block_id",
            "block_name",
            "block_description",
            "block_rows",
        ]
    )
    # find first block with fileld row and check row
    for block in seatmap["blocks"]:
        for row in block["block_rows"]:
            if len(row["row_seats"]) > 0:
                filled_row = row
                break

    assert isinstance(filled_row, Dict)
    assert sorted(list(filled_row.keys())) == sorted(["row_code", "row_seats"])

    # Check seat
    row_seats = filled_row["row_seats"][0]
    assert isinstance(row_seats, Dict)
    assert sorted(list(row_seats.keys())) == sorted(
        [
            "seat_code",
            "seat_price_category_index",
            "seat_coordinate_x",
            "seat_coordinate_y",
        ]
    )
