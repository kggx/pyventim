import pytest
from pyventim.public import EventimExploration 

import datetime

explorer: EventimExploration = EventimExploration()

search_term = "Disneys DER KÖNIG DER LÖWEN"
categories = ['Musical & Show|Musical']
days = 7
sort = "DateAsc"
in_stock = False
start_date = datetime.datetime.now()
end_date = start_date + datetime.timedelta(days=days)
    
# def test_explore_content():
#     # We check for needed keys
#     needed_keys = ['content', 'results', 'totalResults', 'page', 'totalPages', '_links']
#     json = explorer.explore_content(search_term)
#     assert(x in needed_keys for x in json.keys())

# def test_explore_attractions():
#     # We check for needed keys
#     needed_keys = ['attractions', 'results', 'totalResults', 'page', 'totalPages', '_links']
#     json = explorer.explore_attractions(search_term)
#     assert(x in needed_keys for x in json.keys())
    
# def test_explore_locations():
#     # We check for needed keys
#     needed_keys = ['locations', 'results', 'totalResults', 'page', 'totalPages', '_links']
#     json = explorer.explore_locations(search_term)
#     assert(x in needed_keys for x in json.keys())
        

def test_explore_product_groups():    
    json = explorer.explore_product_groups(
        search_term=search_term,
        categories=categories,
        start_date=start_date,
        end_date=end_date,
        sort=sort,
        in_stock=in_stock
    )
    
    # We check for needed keys
    needed_keys = ['productGroups', 'results', 'totalResults', 'page', 'totalPages', '_links']
    json = explorer.explore_product_groups(search_term)
    assert(x in needed_keys for x in json.keys())
    

# Query parameter validation tests
def test_build_query_parameters_required_parameters():
    with pytest.raises(ValueError, match = 'Must have search_term, categories or city_ids in the query parameters!'):
        explorer._build_query_parameters()        

def test_build_query_parameters_page_parameter():
    with pytest.raises(ValueError, match = 'page must be a positive integer > 0!'):
        explorer._build_query_parameters(search_term = search_term, page = -1)

def test_build_query_parameters_sort_parameter():
    with pytest.raises(ValueError, match = 'sort must be one of the following values: "DateAsc", "DateDesc", "NameAsc", "NameDesc", "Rating", "Recommendation"!'):
        explorer._build_query_parameters(search_term = "ABC", sort = "This should fail.")
        
def test_build_query_parameters_search_term_parameter():
    with pytest.raises(ValueError, match = 'search_term must have atleast two characters!'):
        explorer._build_query_parameters(search_term = "A")
    
def test_build_query_parameters_categories_parameter():    
    with pytest.raises(ValueError, match = 'categories must be of type List\[str\]!'):
        # Variable should be a list.
        explorer._build_query_parameters(categories = "abcs")
        
    with pytest.raises(ValueError, match = 'categories must be of type List\[str\]!'):
        # All values in the list must be str   
        explorer._build_query_parameters(categories = [123, "abcs"])     
    
    with pytest.raises(ValueError, match = 'categories must be of type List\[str\]!'):
        # All values in the list must be str   
        explorer._build_query_parameters(categories = [123, 234])  
        
def test_build_query_parameters_city_ids_parameter():    
    with pytest.raises(ValueError, match = 'city_ids must be of type List\[int\]!'):
        # Variable should be a list.
        explorer._build_query_parameters(city_ids = 123)
        
    with pytest.raises(ValueError, match = 'city_ids must be of type List\[int\]!'):
        # All values in the list must be str   
        explorer._build_query_parameters(city_ids = [123, "abcs"])     
    
    with pytest.raises(ValueError, match = 'city_ids must be of type List\[int\]!'):
        # All values in the list must be str   
        explorer._build_query_parameters(city_ids = ["123", "234"])  
        
def test_build_query_parameters_start_date_parameter():
    with pytest.raises(ValueError, match = 'start_date must be of type datetime!'):
        # Variable should be a list.
        explorer._build_query_parameters(search_term = search_term, start_date="This is not a valid timestamp")
 
def test_build_query_parameters_end_date_parameter():
    with pytest.raises(ValueError, match = 'end_date must be of type datetime!'):
        # Variable should be a list.
        explorer._build_query_parameters(search_term = search_term, end_date="This is not a valid timestamp")

def test_build_query_parameters_in_stock_parameter():
    with pytest.raises(ValueError, match = 'in_stock must be of type bool!'):
        # Variable should be a list.
        explorer._build_query_parameters(search_term = search_term, in_stock="This is not a valid boolean")
