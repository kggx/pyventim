# pylint: skip-file

from typing import Dict, Iterator

import pytest
import pydantic
from pyventim import Eventim  # pylint: disable=E0401


EVENTIM = Eventim()
# We are testing against a long running german musical prone NOT to change with a known theater
LOCATION = "Stage Theater im Hafen Hamburg"
ATTRACTION = "Disneys DER KÖNIG DER LÖWEN"
PRODUCT_GROUP_ID = 473431

SORT = "DateAsc"


def test_get_product_group_events():
    """Tests on a fixed product_group"""
    # Check the overall result to be a iterator
    product_group_events = EVENTIM.get_product_group_events(PRODUCT_GROUP_ID)

    assert isinstance(product_group_events, Iterator)

    # Item check
    first_item = next(product_group_events)

    assert isinstance(first_item, Dict)

    assert sorted(list(first_item.keys())) == sorted(
        [
            "@context",
            "@type",
            "description",
            "endDate",
            "image",
            "location",
            "name",
            "offers",
            "performer",
            "startDate",
            "url",
        ]
    )
    # Validate json-schema
    assert first_item["@context"] == "https://schema.org"
    assert first_item["@type"] == "MusicEvent"

    # Value check name
    assert first_item["name"] == "Disneys DER K\u00d6NIG DER L\u00d6WEN"

    # Value check location
    assert first_item["location"]["name"] == "Stage Theater im Hafen Hamburg"


def test_get_product_group_events_from_calendar():
    """Tests on a fixed product_group"""
    # Check the overall result to be a iterator
    product_group_events = EVENTIM.get_product_group_events_from_calendar(
        PRODUCT_GROUP_ID
    )

    assert isinstance(product_group_events, Iterator)

    # Item check
    first_item = next(product_group_events)

    assert isinstance(first_item, Dict)

    assert sorted(list(first_item.keys())) == sorted(
        [
            "id",
            "title",
            "url",
            "start",
            "eventTime",
            "price",
            "eventDate",
            "tileFirstLine",
            "priceAvailable",
            "ticketAvailable",
            "ticketStatusMessage",
            "eventState",
            "voucher",
            "promotionContained",
            "subscriptionPackage",
            "subscriptionPackageData",
            "venueName",
            "first",
            "second",
            "third",
            "eventWeekday",
            "identicalCity",
            "identicalVenue",
            "marketingLabels",
            "clubIcon",
            "subListings",
            "externalOffers",
            "tdlId",
            "formattedDay",
            "formattedMonthYear",
            "formattedWeekdayTime",
            "formattedIsoDate",
            "continuousEventData",
            "eventFavoritesItem",
            "imagePath",
            "linkToModalLayer",
            "medalIcon",
            "genderIcon",
            "formattedDateTime",
            "desc1",
            "desc2",
            "crossedOutPrice",
            "bookable",
            "availabilityIndicator",
            "mobileTicket",
            "red",
            "ticketDirect",
            "fanticket",
            "willCall",
            "eventimPass",
            "trackingData",
        ]
    )

    # Value check name
    assert first_item["title"] == "Disneys DER K\u00d6NIG DER L\u00d6WEN"

    # Value check location
    assert first_item["third"] == "Stage Theater im Hafen Hamburg"
