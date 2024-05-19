from datetime import date, time
from typing import Literal, Iterator, Dict, List

from .adapters import ExplorationAdapter
from .models import ExplorationParameters


class Eventim:
    """Class for high level functions"""

    def __init__(
        self,
    ) -> None:
        self.explorer_api: ExplorationAdapter = ExplorationAdapter()

    def explore_attractions(
        self,
        search_term: str,
        sort: Literal[
            "DateAsc", "DateDesc", "NameAsc", "NameDesc", "Rating", "Recommendation"
        ] = "DateAsc",
    ) -> Iterator[Dict]:
        next_page: int = 1
        while True:
            rest_result = self.explorer_api.get(
                endpoint="v1/attractions",
                params={"search_term": search_term, "page": next_page, "sort": sort},
            )

            for attraction in rest_result.json_data["attractions"]:
                yield attraction

            if (
                next_page >= rest_result.json_data["totalPages"]
                or "next" not in rest_result.json_data["_links"].keys()
            ):
                break

            next_page += 1

    def explore_locations(
        self,
        search_term: str,
        sort: Literal[
            "DateAsc", "DateDesc", "NameAsc", "NameDesc", "Rating", "Recommendation"
        ] = "DateAsc",
    ) -> Iterator[Dict]:
        next_page: int = 1

        while True:
            rest_result = self.explorer_api.get(
                endpoint="v1/locations",
                params={"search_term": search_term, "page": next_page, "sort": sort},
            )

            for location in rest_result.json_data["locations"]:
                yield location

            if (
                next_page >= rest_result.json_data["totalPages"]
                or "next" not in rest_result.json_data["_links"].keys()
            ):
                break

            next_page += 1

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
        next_page: int = 1
        params = ExplorationParameters(
            search_term=search_term,
            categories=categories,
            city_ids=city_ids,
            date_from=date_from,
            date_to=date_to,
            time_from=time_from,
            time_to=time_to,
            sort=sort,
            page=next_page,
        )

        while True:
            params.page = next_page
            print(params.model_dump(exclude_none=True))

            rest_result = self.explorer_api.get(
                endpoint="v2/productGroups", params=params.model_dump(exclude_none=True)
            )

            for product_group in rest_result.json_data["productGroups"]:
                yield product_group

            if (
                next_page >= rest_result.json_data["totalPages"]
                or "next" not in rest_result.json_data["_links"].keys()
            ):
                break

            next_page += 1

    def get_attraction_events(self):
        raise NotImplementedError()
