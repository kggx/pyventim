import requests
from typing import Dict, List, Literal, Any
from datetime import datetime


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
        query: Dict[str, Any] = {}
        parameters = kwargs.keys()
        
        # Check if atlease one of the required keywords is present
        if "search_term" not in parameters and "categories" not in parameters and "city_ids" not in parameters:
            raise ValueError('Must have search_term, categories or city_ids in the query parameters!')
                
        # Validate if page is valid        
        if kwargs.get('page'):
            page: int = kwargs.get('page')
            if page < 1:
                raise ValueError('page must be a positive integer > 0!')
            
            query['page'] = page
                
        # Validate if sort is valid        
        if kwargs.get('sort'):
            sort: str = kwargs.get('sort')
            allowed: List[str] = ['DateAsc', 'DateDesc' , 'NameAsc', 'NameDesc' , 'Rating' , 'Recommendation']
            if sort not in allowed:
                raise ValueError('sort must be one of the following values: "DateAsc", "DateDesc", "NameAsc", "NameDesc", "Rating", "Recommendation"!')
            
            query['sort'] = sort
        
        # Validate if search_term is valid
        if kwargs.get('search_term'):
            search_term: str = kwargs.get('search_term')
            if len(search_term) < 2:
                raise ValueError("search_term must have atleast two characters!")
            
            query['search_term'] = search_term
        
        # Validate if categories is valid
        if kwargs.get('categories'):
            categories: List[str] = kwargs.get('categories')
            if not isinstance(categories, List):
                raise ValueError("categories must be of type List[str]!")
                        
            # Check values to be of type str
            for x in categories:
                if not isinstance(x, str):
                    raise ValueError("categories must be of type List[str]!")
            
            query['categories'] = categories        
        
        # Validate if city_ids are valid
        if kwargs.get('city_ids'):
            city_ids: List[int] = kwargs.get('city_ids')
            if not isinstance(city_ids, List):
                raise ValueError(f"city_ids must be of type List[int]!")
            
            # Check values to be of type str
            for x in city_ids:
                if not isinstance(x, int):
                    raise ValueError("city_ids must be of type List[int]!")
                
            query['city_ids'] = city_ids    
            
        # Validate if start_date is valid
        if kwargs.get('start_date'):
            start_date:datetime = kwargs.get('start_date')
            if not isinstance(start_date, datetime):
                raise ValueError(f"start_date must be of type datetime!")
            
            query['date_from'] = start_date.strftime('%Y-%m-%d')  
            query['time_from'] = start_date.strftime('%H:%M')
        
        # Validate if end_date is valid
        if kwargs.get('end_date'):
            end_date:datetime = kwargs.get('end_date')
            if not isinstance(end_date, datetime):
                raise ValueError(f"end_date must be of type datetime!")
            
            query['date_to'] = end_date.strftime('%Y-%m-%d')  
            query['time_to'] = end_date.strftime('%H:%M')
        
        # Validate if in_stock is valid
        if kwargs.get('in_stock'):
            in_stock:bool = kwargs.get('in_stock')
            if not isinstance(in_stock, bool):
                raise ValueError(f"in_stock must be of type bool!")
            
            query['in_stock'] = in_stock
        
        return query        

    def explore_attractions(self, search_term: str, page: int = 1) -> Dict:
        # AKA: Events / Artists etc... will give an artist
        # TODO: Update function
        self._validate_search_term(search_term)
        
        r: requests.Response = self.session.get(
            f"{self.endpoint}/v1/attractions",
            params={"search_term": search_term, "page": page},
        )
        r.raise_for_status()
        return r.json()

    def explore_content(self, search_term: str, page: int = 1):
        # TODO: Update function
        #self._validate_search_term(search_term)
        
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
            categories: List['str'] = None,
            city_ids: List[int] = None,
            start_date:datetime = None,
            end_date:datetime = None,
            page: int = 1, 
            sort: Literal['DateAsc','DateDesc' , 'NameAsc', 'NameDesc' , 'Rating' , 'Recommendation' ] = 'DateAsc',
            in_stock:bool = True,
        ):
        #TODO: Documentation
        params: Dict[str, Any] = self._build_query_parameters(
            search_term=search_term,
            categories=categories,
            city_ids=city_ids,
            start_date=start_date,
            end_date=end_date,
            page=page,
            sort=sort,
            in_stock=in_stock,
        )
        
        print(params)
        
        r: requests.Response = self.session.get(
            f"{self.endpoint}/v2/productGroups",
            params=params,
        )
        
        r.raise_for_status()
        print(r.request.url)
        return r.json()
    
    
        