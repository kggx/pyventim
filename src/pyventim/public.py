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
        
    def _validate_query(self, query_parameters:Dict[str, Any]) -> bool:
        # TODO: Docs
        parameters = query_parameters.keys()
        if "search_term" not in parameters and "categories" not in parameters and "city_ids" not in parameters:
            raise ValueError('Must have search_term, categories or city_ids in the query parameters')
        
        if query_parameters.get('search_term'):
            if len(search_term) < 2:
                raise ValueError(f"search_term must have atleast two characters...")
                
        
        return True        

    def explore_attractions(self, search_term: str, page: int = 1) -> Dict:
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