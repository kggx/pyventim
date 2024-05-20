from datetime import date, time
from typing import Dict, Any, Optional, List, Literal
from typing_extensions import Self

from pydantic import BaseModel, model_validator


class RestResult(BaseModel):
    """Model for a REST result."""

    status_code: int
    message: str
    json_data: Dict[str, Any]


class ExplorationParameters(BaseModel):
    """BaseModel for Eventim Exploration Endpoint Parameters.
    Validates rulesets that are required by the string.
    """

    search_term: Optional[str] = None
    categories: Optional[List[str]] = None
    city_ids: Optional[List[int]] = None
    date_from: Optional[date] = None
    date_to: Optional[date] = None
    time_from: Optional[time] = None
    time_to: Optional[time] = None
    in_stock: Optional[bool] = None
    page: int = 1
    sort: Literal[
        "DateAsc", "DateDesc", "NameAsc", "NameDesc", "Rating", "Recommendation"
    ] = "DateAsc"

    @model_validator(mode="after")
    def check_required(self) -> Self:
        if not self.search_term and not self.categories and not self.city_ids:
            raise ValueError("Must have either search_term, categories or city_ids")

        return self

    @model_validator(mode="after")
    def check_search_term(self) -> Self:
        if self.search_term:
            if len(self.search_term) < 3:
                raise ValueError("search_term must be atleast 3 characters long")

        return self


# class Attraction(BaseModel):
#     attraction_id: int
#     name: str
#     description: Optional[str]
#     link: str
#     url: Dict[str, str]
#     image_url: Optional[str]
#     rating: Dict[str, Union[int, float]]


# class ExplorationResult(BaseModel):
#     data: list[Dict[str, Any]]
#     search_term: str
#     results: int
#     total_results: int
#     page: int
#     total_pages: int
#     _links: dict[str, dict[str, str]]
