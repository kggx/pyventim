from pyventim.public import EventimExploration 

explorer: EventimExploration = EventimExploration()
search_term:str = "Sleep"

def test_validate_search_term():
    # Check if validation passes for a invalid search term
    try:
        explorer._validate_search_term(search_term[0])
    except ValueError:
        assert(True)
        
    # Validate if given a valid word it should return nothing
    assert(explorer._validate_search_term(search_term) is None)
    
def test_content():
    # We check for needed keys
    needed_keys = ['content', 'results', 'totalResults', 'page', 'totalPages', '_links']
    json = explorer.content(search_term)
    assert(x in needed_keys for x in json.keys())

def test_attractions():
    # We check for needed keys
    needed_keys = ['attractions', 'results', 'totalResults', 'page', 'totalPages', '_links']
    json = explorer.attractions(search_term)
    assert(x in needed_keys for x in json.keys())
    
def test_locations():
    # We check for needed keys
    needed_keys = ['locations', 'results', 'totalResults', 'page', 'totalPages', '_links']
    json = explorer.locations(search_term)
    assert(x in needed_keys for x in json.keys())
        

def test_product_groups():
    # We check for needed keys
    needed_keys = ['productGroups', 'results', 'totalResults', 'page', 'totalPages', '_links']
    json = explorer.product_groups(search_term)
    assert(x in needed_keys for x in json.keys())
