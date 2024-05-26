"""Pydantic models for the module.
"""

from datetime import date, time
from typing import Dict, Any, Optional, List, Literal
from typing_extensions import Self

from pydantic import BaseModel, model_validator, field_serializer


class RestResult(BaseModel):
    """Model for a REST result."""

    status_code: int
    message: str
    json_data: Dict[str, Any]


class HtmlResult(BaseModel):
    """Model for a REST result."""

    status_code: int
    message: str
    html_data: str


class ComponentParameters(BaseModel):
    """BaseModel for Eventim Component Endpoint Parameters.
    Validates rulesets that are required by the endpoint.
    """

    doc: Literal["component"] = "component"
    fun: Literal["eventselectionbox"] = "eventselectionbox"

    esid: int  # product_group_id
    pnum: int = 1  # This is optional but recommended to start at 1

    startdate: Optional[date] = None
    enddate: Optional[date] = None
    ptype: Optional[Literal["tickets", "vip_packages", "extras"]] = None
    cityname: Optional[str] = None
    filterused: Optional[bool] = True  # Has litterly no effect but might change.

    @model_validator(mode="after")
    def check_required(self) -> Self:
        """Validates the model on required parameters

        Raises:
            ValueError: Raised if not one required parameter is set.

        Returns:
            Self: The pydantic model.
        """
        if self.doc != "component" or self.fun != "eventselectionbox":
            raise ValueError(
                "doc parameter != component and fun parameter != component"
            )

        return self


class ExplorationParameters(BaseModel):
    """BaseModel for Eventim Exploration Endpoint Parameters.
    Validates rulesets that are required by the endpoint.
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
        """Validates the model on required parameters

        Raises:
            ValueError: Raised if not one required parameter is set.

        Returns:
            Self: The pydantic model.
        """
        if not self.search_term and not self.categories and not self.city_ids:
            raise ValueError("Must have either search_term, categories or city_ids")

        return self

    @model_validator(mode="after")
    def check_search_term(self) -> Self:
        """Validates on a valid search term.

        Raises:
            ValueError: Raised if not a valid search term

        Returns:
            Self: The pydantic model.
        """
        if self.search_term:
            if len(self.search_term) < 3:
                raise ValueError("search_term must be atleast 3 characters long")

        return self

    # custom time values
    @field_serializer("time_from", "time_to")
    def serialize_dt(self, value: time, _info) -> str:
        """The eventim API expects time_from & time_to in the format of "HH:MM"

        Returns:
            str: Time in HH:MM format
        """
        return value.strftime("%H:%M")


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
