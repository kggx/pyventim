"""Custom adapters to handle traffic from Eventim"""

from json import JSONDecodeError
from typing import Dict, Any

import requests

from .exceptions import RestException, HtmlException
from .models import RestResult, HtmlResult


class RestAdapter:
    """Adapter for all resta based requests"""

    def __init__(self, session: requests.Session | None = None) -> None:
        self.session: requests.Session = session or requests.Session()
        self.session.headers.update(
            {
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0"  # pylint: disable=C0301
            }
        )

        self.hostname = (
            "https://public-api.eventim.com/websearch/search/api/exploration"
        )

    def _do(
        self,
        method: str,
        endpoint: str,
        params: Dict | None = None,
        json_data: Dict | None = None,
    ) -> RestResult:
        print(method, self.hostname, endpoint, params, json_data)
        try:
            response: requests.Response = self.session.request(
                method=method,
                url=f"{self.hostname}/{endpoint}",
                params=params,
                json=json_data,
            )

        except requests.exceptions.RequestException as e:
            raise RestException("Request failed") from e

        try:
            data_out: Dict[str, Any] = response.json()
        except (ValueError, JSONDecodeError) as e:
            raise RestException("Bad JSON in response") from e

        if 299 >= response.status_code >= 200:
            return RestResult(
                status_code=response.status_code,
                message=response.reason,
                json_data=data_out,
            )

        raise RestException(f"{response.status_code}: {response.reason}")

    def get(self, endpoint: str, params: Dict | None = None) -> RestResult:
        """Get a choosen endpoint on a restful API.

        Args:
            endpoint (str): Endpoint to query.
            params (Dict | None, optional): Parameters to query. Defaults to None.

        Returns:
            RestResult: RestResult with status_code, message and json_data
        """
        return self._do(method="GET", endpoint=endpoint, params=params)


class HtmlAdapter:
    """Adapter for all html based requests."""

    def __init__(self, session: requests.Session | None = None) -> None:
        self.session: requests.Session = session or requests.Session()
        self.session.headers.update(
            {
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0"  # pylint: disable=C0301
            }
        )

        self.hostname = "https://www.eventim.de/"

    def _do(
        self,
        method: str,
        endpoint: str,
        params: Dict | None = None,
        json_data: Dict | None = None,
    ) -> HtmlResult:
        try:
            response = self.session.request(
                method=method,
                url=f"{self.hostname}/{endpoint}",
                params=params,
                json=json_data,
            )
        except requests.exceptions.RequestException as e:
            raise HtmlException("Request failed") from e

        try:
            data_out: str = response.content.decode("utf-8")
        except (ValueError, JSONDecodeError) as e:
            raise HtmlException("Bad HTML in response") from e

        if 299 >= response.status_code >= 200:
            return HtmlResult(
                status_code=response.status_code,
                message=response.reason,
                html_data=data_out,
            )

        raise HtmlException(f"{response.status_code}: {response.reason}")

    def get(self, endpoint: str, params: Dict | None = None) -> HtmlResult:
        """Get a choosen endpoint on the html page.

        Args:
            endpoint (str): Endpoint to query.
            params (Dict | None, optional): Parameters to query. Defaults to None.

        Returns:
            RestResult: RestResult with status_code, message and json_data
        """
        return self._do(method="GET", endpoint=endpoint, params=params)
