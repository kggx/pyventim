"""Module for the public Eventim-API wrapper."""

from typing import Dict, List, Literal, Any
from datetime import datetime, date, time

import requests


class EventimExploration:
    """Class that handles access to the public Eventim API."""

    def __init__(self, session: requests.Session = None) -> None:
        # If a valid session is not provided by the user create a new one.
        if not isinstance(session, requests.Session):
            self.session = requests.Session()
        else:
            self.session = session

        self.endpoint = (
            "https://public-api.eventim.com/websearch/search/api/exploration"
        )

    def validate_required_parameters(self, **kwargs) -> bool:
        if (
            "search_term" not in kwargs
            and "categories" not in kwargs
            and "city_ids" not in kwargs
        ):
            raise ValueError(
                "Must have search_term, categories or city_ids in the query parameters!"
            )

        return True

    def validate_page_parameter(self, page: int) -> bool:
        if page:
            if not isinstance(page, int):
                raise ValueError("page must be a positive integer!")

            if not page >= 1:
                raise ValueError("page must be a positive integer!")

        return True

    def validate_sort_parameter(self, sort: str) -> bool:
        _allowed_values = [
            "DateAsc",
            "DateDesc",
            "NameAsc",
            "NameDesc",
            "Rating",
            "Recommendation",
        ]

        if sort:
            if not isinstance(sort, str):
                raise ValueError(f"sort must match: {", ".join(_allowed_values)}")
            if not sort in _allowed_values:
                raise ValueError(f"sort must match: {", ".join(_allowed_values)}")

        return True

    def validate_search_term_parameter(self, search_term: str) -> bool:
        if search_term:
            if not isinstance(search_term, str):
                raise ValueError("search_term must have atleast two characters!")
            if len(search_term) < 2:
                raise ValueError("search_term must have atleast two characters!")
        return True

    def validate_categories_parameter(self, categories: List[str]) -> bool:
        if categories:
            if not isinstance(categories, List):
                raise ValueError("categories must be a list of strings!")

            for value in categories:
                if not isinstance(value, str):
                    raise ValueError("categories must be a list of strings!")

        return True

    def validate_city_ids_parameter(self, city_ids: List[int]) -> bool:
        if city_ids:
            if not isinstance(city_ids, List):
                raise ValueError("city_ids must be a list of integers!")

            for value in city_ids:
                if not isinstance(value, int):
                    raise ValueError("city_ids must be a list of integers!")

        return True

    def validate_date_from_parameter(self, date_from) -> bool:
        if date_from:
            if not isinstance(date_from, date):
                raise ValueError("date_from must be of type datetime.date!")
        return True

    def validate_date_to_parameter(self, date_to) -> bool:
        if date_to:
            if not isinstance(date_to, date):
                raise ValueError("date_to must be of type datetime.date!")
        return True

    def validate_time_from_parameter(self, time_from) -> bool:
        if time_from:
            if not isinstance(time_from, time):
                raise ValueError("time_from must be of type datetime.time!")
        return True

    def validate_time_to_parameter(self, time_to) -> bool:
        if time_to:
            if not isinstance(time_to, time):
                raise ValueError("time_to must be of type datetime.time!")
        return True

    def validate_in_stock_parameter(self, in_stock) -> bool:
        if in_stock:
            if not isinstance(in_stock, bool):
                raise ValueError("in_stock must be of type bool!")

        return True

    def build_query_parameters(self, **kwargs) -> Dict[str, Any]:
        """Build & validates known input parameters for the Eventim-API on obvious mistakes.

        Raises:
            ValueError: Raises an error if a know invalid parameter is found.


        Returns:
            Dict[str, Any]: The query parameters based on the **kwargs
        """
        query: Dict[str, Any] = {}

        # Check if atlease one of the required keywords is present
        self.validate_required_parameters(**kwargs)

        for kwarg in kwargs.items():
            if not kwarg[1]:
                continue

            match kwarg[0]:
                case "page":
                    self.validate_page_parameter(kwarg[1])
                    query[kwarg[0]] = kwarg[1]
                case "sort":
                    self.validate_sort_parameter(kwarg[1])
                    query[kwarg[0]] = kwarg[1]
                case "search_term":
                    self.validate_search_term_parameter(kwarg[1])
                    query[kwarg[0]] = kwarg[1]
                case "categories":
                    self.validate_categories_parameter(kwarg[1])
                    query[kwarg[0]] = kwarg[1]
                case "city_ids":
                    self.validate_city_ids_parameter(kwarg[1])
                    query[kwarg[0]] = kwarg[1]
                case "date_from":
                    self.validate_date_from_parameter(kwarg[1])
                    query[kwarg[0]] = kwarg[1].strftime("%Y-%m-%d")
                case "date_to":
                    self.validate_date_to_parameter(kwarg[1])
                    query[kwarg[0]] = kwarg[1].strftime("%Y-%m-%d")
                case "time_from":
                    self.validate_time_from_parameter(kwarg[1])
                    query[kwarg[0]] = kwarg[1].strftime("%H:%M")
                case "time_to":
                    self.validate_time_to_parameter(kwarg[1])
                    query[kwarg[0]] = kwarg[1].strftime("%H:%M")
                case "in_stock":
                    self.validate_in_stock_parameter(kwarg[1])
                    query[kwarg[0]] = kwarg[1]
                case _:
                    query[kwarg[0]] = kwarg[1]

        return query

    def explore_attractions(
        self,
        search_term: str,
        page: int = 1,
        sort: Literal[
            "DateAsc", "DateDesc", "NameAsc", "NameDesc", "Rating", "Recommendation"
        ] = "DateAsc",
    ) -> Dict:
        params: Dict[str, Any] = self.build_query_parameters(
            search_term=search_term, page=page, sort=sort
        )
        r: requests.Response = self.session.get(
            f"{self.endpoint}/v1/attractions", params=params
        )
        r.raise_for_status()
        return r.json()

    def explore_content(
        self,
        search_term: str,
        page: int = 1,
        sort: Literal[
            "DateAsc", "DateDesc", "NameAsc", "NameDesc", "Rating", "Recommendation"
        ] = "DateAsc",
    ) -> Dict:
        # Refactor if this returns any meaning full output:
        # https://github.com/kggx/pyventim/issues/6
        params: Dict[str, Any] = self.build_query_parameters(
            search_term=search_term, page=page, sort=sort
        )

        r: requests.Response = self.session.get(
            f"{self.endpoint}/v1/content", params=params
        )
        r.raise_for_status()
        return r.json()

    def explore_locations(
        self,
        search_term: str,
        page: int = 1,
        sort: Literal[
            "DateAsc", "DateDesc", "NameAsc", "NameDesc", "Rating", "Recommendation"
        ] = "DateAsc",
    ) -> Dict:
        params: Dict[str, Any] = self.build_query_parameters(
            search_term=search_term, page=page, sort=sort
        )

        r: requests.Response = self.session.get(
            f"{self.endpoint}/v1/locations", params=params
        )
        r.raise_for_status()
        return r.json()

    def explore_product_groups(
        self,
        search_term: str = None,
        categories: List["str"] = None,
        city_ids: List[int] = None,
        date_from: datetime.date = None,
        date_to: datetime.date = None,
        time_from: datetime.time = None,
        time_to: datetime.time = None,
        page: int = 1,
        sort: Literal[
            "DateAsc", "DateDesc", "NameAsc", "NameDesc", "Rating", "Recommendation"
        ] = "DateAsc",
        in_stock: bool = True,
    ) -> Dict:
        params: Dict[str, Any] = self.build_query_parameters(
            search_term=search_term,
            categories=categories,
            city_ids=city_ids,
            date_from=date_from,
            date_to=date_to,
            time_from=time_from,
            time_to=time_to,
            page=page,
            sort=sort,
            in_stock=in_stock,
        )

        r: requests.Response = self.session.get(
            f"{self.endpoint}/v2/productGroups", params=params
        )

        r.raise_for_status()
        return r.json()
