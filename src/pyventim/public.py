import requests
from typing import Dict
import pprint


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
        
    def _validate_search_term(self, search_term: str) -> None:
        """Function validates an input string. Should only be used internally.

        Args:
            search_term (str): Search term to check

        Raises:
            ValueError: If the search_term is not valid then raise an error.
        """
        if len(search_term) < 2:
            raise ValueError(f"search_term must have atleast two characters...")
            

    def attractions(self, search_term: str, page: int = 1) -> Dict:
        """This function returns a requested page for the given search_term of the attractions endpoint.

        Args:
            search_term (str): Search term to be querried.
            page (int, optional): Page number to fetch. Defaults to 1.

        Returns:
            Dict: Returns the requested page with meta data.
        """
        self._validate_search_term(search_term)
        
        r: requests.Response = self.session.get(
            f"{self.endpoint}/v1/attractions",
            params={"search_term": search_term, "page": page},
        )
        r.raise_for_status()
        return r.json()

    def content(self, search_term: str, page: int = 1):
        """This function returns a requested page for the given search_term of the content endpoint.

        Args:
            search_term (str): Search term to be querried.
            page (int, optional): Page number to fetch. Defaults to 1.

        Returns:
            Dict: Returns the requested page with meta data.
        """
        self._validate_search_term(search_term)
        
        r: requests.Response = self.session.get(
            f"{self.endpoint}/v1/content",
            params={"search_term": search_term, "page": page},
        )
        r.raise_for_status()
        return r.json()

    def locations(self, search_term: str, page: int = 1):
        """This function returns a requested page for the given search_term of the locations endpoint.

        Args:
            search_term (str): Search term to be querried.
            page (int, optional): Page number to fetch. Defaults to 1.

        Returns:
            Dict: Returns the requested page with meta data.
        """
        self._validate_search_term(search_term)
        r: requests.Response = self.session.get(
            f"{self.endpoint}/v1/locations",
            params={"search_term": search_term, "page": page},
        )
        r.raise_for_status()
        return r.json()

    def product_groups(self, search_term: str, page: int = 1):
        """This function returns a requested page for the given search_term of the product_groups endpoint.
        
        Args:
            search_term (str): Search term to be querried.
            page (int, optional): Page number to fetch. Defaults to 1.

        Returns:
            Dict: Returns the requested page with meta data.
        """
        self._validate_search_term(search_term)
        r: requests.Response = self.session.get(
            f"{self.endpoint}/v2/productGroups",
            params={"search_term": search_term, "page": page},
        )
        
        r.raise_for_status()
        return r.json()