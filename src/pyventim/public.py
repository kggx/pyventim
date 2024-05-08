import requests
from typing import Dict
import pprint


class EventimExploration:
    def __init__(self, session: requests.Session = None):
        # If a valid session is not provided by the user create a new one.
        if not isinstance(session, requests.Session):
            self.session = requests.Session()
        else:
            self.session = session

        self.endpoint = (
            "https://public-api.eventim.com/websearch/search/api/exploration"
        )
        
    def _validate_search_term(self, search_term: str):
        if len(search_term) == 0:
            raise ValueError(f"search_term must have atleast one character...")
            

    def attrations(self, search_term: str, page: int = 1) -> Dict:
        self._validate_search_term(search_term)
        
        r: requests.Response = self.session.get(
            f"{self.endpoint}/v1/attractions",
            params={"search_term": search_term, "page": page},
        )
        r.raise_for_status()
        return r.json()

    def content(self, search_term: str, page: int = 1):
        self._validate_search_term(search_term)
        
        r: requests.Response = self.session.get(
            f"{self.endpoint}/v1/content",
            params={"search_term": search_term, "page": page},
        )
        r.raise_for_status()
        return r.json()

    def locations(self, search_term: str, page: int = 1):
        self._validate_search_term(search_term)
        r: requests.Response = self.session.get(
            f"{self.endpoint}/v1/locations",
            params={"search_term": search_term, "page": page},
        )
        r.raise_for_status()
        return r.json()

    def product_groups(self, search_term: str, page: int = 1):
        self._validate_search_term(search_term)
        r: requests.Response = self.session.get(
            f"{self.endpoint}/v2/productGroups",
            params={"search_term": search_term, "page": page},
        )
        
        r.raise_for_status()
        return r.json()

if __name__ == "__main__":
    exp = EventimExploration()
    search_term = "Disneys Der König der Löwen"

    pprint.pprint(exp.attrations(search_term=search_term))
    pprint.pprint(exp.content(search_term=search_term))
    pprint.pprint(exp.locations(search_term=search_term))
    pprint.pprint(exp.product_groups(search_term=search_term))
