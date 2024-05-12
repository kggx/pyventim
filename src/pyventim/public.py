import requests
from typing import Dict, List, Literal, Any
from datetime import datetime, date, time

import warnings


class EventimExploration:
    def __init__(self, session: requests.Session = None) -> None:
        # If a valid session is not provided by the user create a new one.
        if not isinstance(session, requests.Session):
            self.session = requests.Session()
        else:
            self.session = session

        self.endpoint = (
            "https://public-api.eventim.com/websearch/search/api/exploration"
        )

    def _build_query_parameters(self, **kwargs) -> Dict[str, Any]:
        # TODO: Docs
        print(kwargs.keys())
        query: Dict[str, Any] = {}
        parameters = kwargs.keys()

        # Check if atlease one of the required keywords is present
        if (
            "search_term" not in parameters
            and "categories" not in parameters
            and "city_ids" not in parameters
        ):
            raise ValueError(
                "Must have search_term, categories or city_ids in the query parameters!"
            )

        # Validate if page is valid
        if kwargs.get("page"):
            page: int = kwargs.get("page")
            if page < 1:
                raise ValueError("page must be a positive integer > 0!")

            query["page"] = page

        # Validate if sort is valid
        if kwargs.get("sort"):
            sort: str = kwargs.get("sort")
            allowed: List[str] = [
                "DateAsc",
                "DateDesc",
                "NameAsc",
                "NameDesc",
                "Rating",
                "Recommendation",
            ]
            if sort not in allowed:
                raise ValueError(
                    'sort must be one of the following values: "DateAsc", "DateDesc", "NameAsc", "NameDesc", "Rating", "Recommendation"!'
                )

            query["sort"] = sort

        # Validate if search_term is valid
        if kwargs.get("search_term"):
            search_term: str = kwargs.get("search_term")
            if len(search_term) < 2:
                raise ValueError("search_term must have atleast two characters!")

            query["search_term"] = search_term

        # Validate if categories is valid
        if kwargs.get("categories"):
            categories: List[str] = kwargs.get("categories")
            if not isinstance(categories, List):
                raise ValueError("categories must be a list of strings!")

            # Check values to be of type str
            for x in categories:
                if not isinstance(x, str):
                    raise ValueError("categories must be a list of strings!")

            query["categories"] = categories

        # Validate if city_ids are valid
        if kwargs.get("city_ids"):
            city_ids: List[int] = kwargs.get("city_ids")
            if not isinstance(city_ids, List):
                raise ValueError(f"city_ids must be a list of integers!")

            # Check values to be of type str
            for x in city_ids:
                if not isinstance(x, int):
                    raise ValueError("city_ids must be a list of integers!")

            query["city_ids"] = city_ids

        # Validate if valid date_from
        if kwargs.get("date_from"):
            date_from: date = kwargs.get("date_from")
            if not isinstance(date_from, date):
                raise ValueError(f"date_from must be of type date!")

            query["date_from"] = date_from.strftime("%Y-%m-%d")

        # Validate if valid date_to
        if kwargs.get("date_to"):
            date_to: date = kwargs.get("date_to")
            if not isinstance(date_to, date):
                raise ValueError(f"date_to must be of type date!")

            query["date_to"] = date_to.strftime("%Y-%m-%d")

        # Validate if valid time_from
        if kwargs.get("time_from"):
            time_from: time = kwargs.get("time_from")
            if not isinstance(time_from, time):
                raise ValueError(f"time_from must be of type time!")

            query["time_from"] = time_from.strftime("%H:%M")

        # Validate if valid time_to
        if kwargs.get("time_to"):
            time_to: time = kwargs.get("time_to")
            if not isinstance(time_to, time):
                raise ValueError(f"time_to must be of type time!")

            query["time_to"] = time_to.strftime("%Y-%m-%d")

        # Validate if in_stock is valid
        if kwargs.get("in_stock"):
            in_stock: bool = kwargs.get("in_stock")
            if not isinstance(in_stock, bool):
                raise ValueError(f"in_stock must be of type bool!")

            query["in_stock"] = in_stock

        return query

    def explore_attractions(
        self,
        search_term: str = None,
        categories: List["str"] = None,
        city_ids: List[int] = None,
        page: int = 1,
        sort: Literal[
            "DateAsc", "DateDesc", "NameAsc", "NameDesc", "Rating", "Recommendation"
        ] = "DateAsc",
        in_stock: bool = True,
    ) -> Dict:
        # AKA: Events / Artists etc... will give an artist
        # TODO: Update function
        params = self._build_query_parameters()

        r: requests.Response = self.session.get(
            f"{self.endpoint}/v1/attractions",
            params=params,
            # params={"search_term": search_term, "page": page},
        )
        r.raise_for_status()
        return r.json()

    def explore_content(self, search_term: str, page: int = 1):
        # TODO: Update function
        # self._validate_search_term(search_term)

        r: requests.Response = self.session.get(
            f"{self.endpoint}/v1/content",
            params={"search_term": search_term, "page": page},
        )
        r.raise_for_status()
        return r.json()

    def explore_locations(self, search_term: str, page: int = 1):
        # TODO: Update function
        # self._validate_search_term(search_term)

        r: requests.Response = self.session.get(
            f"{self.endpoint}/v1/locations",
            params={"search_term": search_term, "page": page},
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
        # TODO: Documentation
        params: Dict[str, Any] = self._build_query_parameters(
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
            f"{self.endpoint}/v2/productGroups",
            params=params,
        )

        r.raise_for_status()
        return r.json()
