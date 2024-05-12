from pyventim.public import EventimExploration 

explorer: EventimExploration = EventimExploration()
search_term:str = "Sleep"
    
def test_explore_content():
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
