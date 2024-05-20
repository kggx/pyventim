"""Custom adapters to handle traffic from Eventim"""

from json import JSONDecodeError
from typing import Dict, Any

import requests

from .exceptions import ExplorationException, ComponentException
from .models import RestResult, HtmlResult


class ExplorationAdapter:
    """Adapter for the exploration endpoint"""

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
        try:
            response = self.session.request(
                method=method,
                url=f"{self.hostname}/{endpoint}",
                params=params,
                json=json_data,
            )
        except requests.exceptions.RequestException as e:
            raise ExplorationException("Request failed") from e

        try:
            data_out: Dict[str, Any] = response.json()
        except (ValueError, JSONDecodeError) as e:
            raise ExplorationException("Bad JSON in response") from e

        if 299 >= response.status_code >= 200:
            return RestResult(
                status_code=response.status_code,
                message=response.reason,
                json_data=data_out,
            )

        raise ExplorationException(f"{response.status_code}: {response.reason}")

    def get(self, endpoint: str, params: Dict | None = None) -> RestResult:
        """Get a choosen endpoint on the public-api.eventim.com.

        Args:
            endpoint (str): Endpoint to query.
            params (Dict | None, optional): Parameters to query. Defaults to None.

        Returns:
            RestResult: RestResult with status_code, message and json_data
        """
        return self._do(method="GET", endpoint=endpoint, params=params)


class ComponentAdapter:
    def __init__(self, session: requests.Session | None = None) -> None:
        self.session: requests.Session = session or requests.Session()
        self.session.headers.update(
            {
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0"  # pylint: disable=C0301
            }
        )

        self.hostname = "https://www.eventim.de/component"

    def _do(
        self,
        method: str,
        params: Dict | None = None,
        json_data: Dict | None = None,
    ) -> HtmlResult:
        try:
            response = self.session.request(
                method=method,
                url=f"{self.hostname}",
                params=params,
                json=json_data,
            )
        except requests.exceptions.RequestException as e:
            raise ComponentException("Request failed") from e

        try:
            data_out: str = response.content.decode("utf-8")
        except (ValueError, JSONDecodeError) as e:
            raise ComponentException("Bad HTML in response") from e

        if 299 >= response.status_code >= 200:
            return HtmlResult(
                status_code=response.status_code,
                message=response.reason,
                html_data=data_out,
            )

        raise ComponentException(f"{response.status_code}: {response.reason}")

    def get(self, params: Dict | None = None) -> HtmlResult:
        """Get a choosen endpoint on the public-api.eventim.com.

        Args:
            endpoint (str): Endpoint to query.
            params (Dict | None, optional): Parameters to query. Defaults to None.

        Returns:
            RestResult: RestResult with status_code, message and json_data
        """
        return self._do(method="GET", params=params)


# class EventimCompenent:
#     """Class that handles access to the public Eventim API for components."""

#     def __init__(self, session: requests.Session = None) -> None:
#         # If a valid session is not provided by the user create a new one.
#         if not isinstance(session, requests.Session):
#             self.session: requests.Session = requests.Session()
#         else:
#             self.session: requests.Session = session

#         # Requires a desktop browser user-agent
#         self.session.headers.update(
#             {
#                 "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0"
#             }
#         )
#         self.endpoint = "https://www.eventim.de/component/"


#     def get_attraction_events(self, attraction_id: int) -> dict:
#         r = self.session.get(
#             f"{self.endpoint}",
#             headers={},
#             params={
#                 "doc": "component",
#                 "esid": f"{attraction_id}",
#                 "fun": "eventselectionbox",
#                 # "startdate": None,
#                 # "enddate": None,
#                 # "ptype": None,
#                 # "cityname": None,
#                 # "filterused": True,
#                 # "pnum": 1,
#             },
#         )
#         r.raise_for_status()
#         return r.content.decode("utf-8")
#         # Actually returning json in scheme: https://schema.org/MusicEvent
#         # https://www.eventim.de/component/?affiliate=EVE&cityname=Berlin&doc=component&esid=3642502&filterused=true&fun=eventselectionbox&tab=1&startdate=2024-05-22
#         # https://www.eventim.de/component/?doc=component&enddate=2024-09-30&esid=473431&fun=eventlisting&pnum=2&ptype=&startdate=2024-05-18
#         # Parameters
#         # esid via public exploration API aka artist id
#         # pnum = page number
#         # filterused = true
#         # startdate
#         # enddate
#         # ptype=tickets | vip_packages (TODO: Look for types)
#         # fun=eventselectionbox
#         # doc=component
#         # cityname=Hamburg

#         # raise NotImplementedError()

#     # König der Löwen:
#     # https://www.eventim.de/component/?affiliate=EVE&cityname=Hamburg&doc=component&esid=473431&filterused=true&fun=eventselectionbox&startdate=2024-05-12&tab=2&enddate=2024-05-12

#     # Sleep Token https://www.eventim.de/component/
