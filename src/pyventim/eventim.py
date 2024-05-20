"""Highlevel wrapper functions for the Eventim API."""

from datetime import date, time
from typing import Literal, Iterator, Dict, List

from .models import ExplorationParameters, ComponentParameters
from .adapters import ExplorationAdapter, ComponentAdapter  # pylint: disable=E0401
from .utils import (
    parse_has_next_page_from_component_html,
    parse_list_from_component_html,
    parse_calendar_from_component_html,
)


class Eventim:
    """Class for high level functions"""

    def __init__(
        self,
    ) -> None:
        self.explorer_api: ExplorationAdapter = ExplorationAdapter()
        self.component_adapter: ComponentAdapter = ComponentAdapter()

    def explore_attractions(
        self,
        search_term: str,
        sort: Literal[
            "DateAsc", "DateDesc", "NameAsc", "NameDesc", "Rating", "Recommendation"
        ] = "DateAsc",
    ) -> Iterator[Dict]:
        # pylint: disable=line-too-long
        """This function returns attractions from the exploration API.

        Args:
            search_term (str): Search term to query the API.
            sort (Literal[ &quot;DateAsc&quot;, &quot;DateDesc&quot;, &quot;NameAsc&quot;, &quot;NameDesc&quot;, &quot;Rating&quot;, &quot;Recommendation&quot; ], optional): Sorted by. Defaults to "DateAsc".

        Yields:
            Iterator[Dict]: Iterator that returns one item at the time and handles the pagination of eventim.
        """
        params = ExplorationParameters(
            search_term=search_term,
            sort=sort,
            page=1,
        )

        while True:

            rest_result = self.explorer_api.get(
                endpoint="v1/attractions", params=params.model_dump(exclude_none=True)
            )

            for attraction in rest_result.json_data["attractions"]:
                yield attraction

            if (
                params.page >= rest_result.json_data["totalPages"]
                or "next" not in rest_result.json_data["_links"].keys()
            ):
                break

            params.page = params.page + 1

    def explore_locations(
        self,
        search_term: str,
        sort: Literal[
            "DateAsc", "DateDesc", "NameAsc", "NameDesc", "Rating", "Recommendation"
        ] = "DateAsc",
    ) -> Iterator[Dict]:
        # pylint: disable=line-too-long
        """This function returns locations from the exploration API.

        Args:
            search_term (str): Search term to query the API.
            sort (Literal[ &quot;DateAsc&quot;, &quot;DateDesc&quot;, &quot;NameAsc&quot;, &quot;NameDesc&quot;, &quot;Rating&quot;, &quot;Recommendation&quot; ], optional): Sorted by. Defaults to "DateAsc".

        Yields:
            Iterator[Dict]: Iterator that returns one item at the time and handles the pagination of eventim.
        """
        params = ExplorationParameters(
            search_term=search_term,
            sort=sort,
            page=1,
        )

        while True:
            rest_result = self.explorer_api.get(
                endpoint="v1/locations", params=params.model_dump(exclude_none=True)
            )

            for location in rest_result.json_data["locations"]:
                yield location

            if (
                params.page >= rest_result.json_data["totalPages"]
                or "next" not in rest_result.json_data["_links"].keys()
            ):
                break

            params.page = params.page + 1

    def explore_product_groups(
        self,
        search_term: str | None = None,
        categories: List[str] | None = None,
        city_ids: List[int] | None = None,
        date_from: date | None = None,
        date_to: date | None = None,
        time_from: time | None = None,
        time_to: time | None = None,
        sort: Literal[
            "DateAsc", "DateDesc", "NameAsc", "NameDesc", "Rating", "Recommendation"
        ] = "DateAsc",
    ) -> Iterator[Dict]:
        # pylint: disable=line-too-long
        """Function to return product groups and top 5 matching products from the API.
        Combining multiple parameters act as AND operators.

        Args:
            search_term (str | None, optional): Search term to query the API.. Defaults to None.
            categories (List[str] | None, optional): Categories to limit the search. Defaults to None.
            city_ids (List[int] | None, optional): Cities to limit the search. Defaults to None.
            date_from (date | None, optional): Product date later than. Defaults to None.
            date_to (date | None, optional): Product date earlier than. Defaults to None.
            time_from (time | None, optional): Start time of product later than. Defaults to None.
            time_to (time | None, optional): Start time of product earlier than. Defaults to None.
            sort (Literal[ &quot;DateAsc&quot;, &quot;DateDesc&quot;, &quot;NameAsc&quot;, &quot;NameDesc&quot;, &quot;Rating&quot;, &quot;Recommendation&quot; ], optional): Sorted by. Defaults to "DateAsc".

        Yields:
            - Iterator[Dict]: Iterator that returns one item at the time and handles the pagination of eventim.
        """
        params = ExplorationParameters(
            search_term=search_term,
            categories=categories,
            city_ids=city_ids,
            date_from=date_from,
            date_to=date_to,
            time_from=time_from,
            time_to=time_to,
            sort=sort,
            page=1,
        )

        while True:
            rest_result = self.explorer_api.get(
                endpoint="v2/productGroups", params=params.model_dump(exclude_none=True)
            )

            for product_group in rest_result.json_data["productGroups"]:
                yield product_group

            if (
                params.page >= rest_result.json_data["totalPages"]
                or "next" not in rest_result.json_data["_links"].keys()
            ):
                break

            params.page = params.page + 1

    def get_attraction_events(
        self,
        attraction_id: int,
        date_from: date | None = None,
        date_to: date | None = None,
        ticket_type: Literal["tickets", "vip_packages", "extras"] | None = None,
        city_name: str | None = None,
    ) -> Iterator[Dict]:
        # pylint: disable=line-too-long
        """This returns the attraction events. The attraction events follow this schema: https://schema.org/MusicEvent.
        The API only returns a maximum of 90 events. This should be plenty but some event types like continous musicals have more than 90 events
        **If you try to fetching many events (>90) at a time then get_attraction_events_from_calendar() should be used.**

        Args:
            attraction_id (int): Attraction ID to query
            date_from (date | None, optional): Event date later than. Defaults to None.
            date_to (date | None, optional): Event date earlier than. Defaults to None.
            ticket_type (Literal[&quot;tickets&quot;, &quot;vip_packages&quot;, &quot;extras&quot;] | None, optional): Include only events with tickets avialible in type. Defaults to None.
            city_name (str | None, optional): Include only events in city. Defaults to None.

        Yields:
            Iterator[Dict]: The events in the MusicEvent schema.
        """

        params = ComponentParameters(
            esid=attraction_id,
            startdate=date_from,
            enddate=date_to,
            ptype=ticket_type,
            cityname=city_name,
        )

        while params.pnum <= 10:
            comp_result = self.component_adapter.get(
                params=params.model_dump(exclude_none=True)
            )
            attraction_events = parse_list_from_component_html(comp_result.html_data)

            for attraction_event in attraction_events:
                yield attraction_event

            if parse_has_next_page_from_component_html(comp_result.html_data) is False:
                break

            params.pnum = params.pnum + 1

    def get_attraction_events_from_calendar(
        self,
        attraction_id: int,
        date_from: date | None = None,
        date_to: date | None = None,
        ticket_type: Literal["tickets", "vip_packages", "extras"] | None = None,
        city_name: str | None = None,
    ) -> Iterator[Dict]:
        # pylint: disable=line-too-long
        """This returns the attraction events. The attraction events follow a custom calendar schema.

        Args:
            attraction_id (int): Attraction ID to query
            date_from (date | None, optional): Event date later than. Defaults to None.
            date_to (date | None, optional): Event date earlier than. Defaults to None.
            ticket_type (Literal[&quot;tickets&quot;, &quot;vip_packages&quot;, &quot;extras&quot;] | None, optional): Include only events with tickets avialible in type. Defaults to None.
            city_name (str | None, optional): Include only events in city. Defaults to None.

        Yields:
            Iterator[Dict]: The events in a calendar schema.
        """
        params = ComponentParameters(
            esid=attraction_id,
            startdate=date_from,
            enddate=date_to,
            ptype=ticket_type,
            cityname=city_name,
        )

        comp_result = self.component_adapter.get(
            params=params.model_dump(exclude_none=True)
        )

        calendar_configuration = parse_calendar_from_component_html(
            comp_result.html_data
        )

        calendar_content = calendar_configuration["calendar_content"]

        for attraction_event in calendar_content["result"]:
            yield attraction_event
