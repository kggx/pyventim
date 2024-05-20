<hr>

# Getting started

Here you will find a quickstart quide and some information about the data returned by the API.

## Exploration Endpoint

### explore_attractions

The explore_attractions returns matching attractions based on the search_term parameter
(In the Eventim-Universe that's a musical, artist, band, etc..)

```python
# Returns an iterator that fetches all pages off the search endpoint.
attractions = eventim.explore_attractions(search_term="The Rolling Stones", sort=sort)

# We can loop over each attraction and print the item. The module handles fetching pages automatically.
for attraction in attractions:
    print(attraction)

```

A sample attraction can be found here:

```json
{
  "attractionId": "662",
  "name": "The Rolling Stones",
  "description": "The Rolling Stones sind zweifellos eine der legend\u00e4rsten Rockbands der Welt \u2013 und das liegt auch an ihren spektakul\u00e4ren Live-Shows.",
  "link": "https://www.eventim.de/artist/the-rolling-stones/",
  "url": {
    "path": "/artist/the-rolling-stones/",
    "domain": "https://www.eventim.de"
  },
  "imageUrl": "https://www.eventim.de/obj/media/DE-eventim/galery/222x222/r/rolling-stones-tickets-2022-02-neu.jpg",
  "rating": {
    "count": 460,
    "average": 4.284800052642822
  }
}
```

### explore_locations

The explore_attractions returns matching locations based on the search_term parameter.
A location can be a thing like an arena, a bar or a theatere.

```python
# Returns an iterator that fetches all pages off the search endpoint.
locations = eventim.explore_locations("Stage Theater im Hafen Hamburg")

# We can loop over each location and print the item. The module handles fetching pages automatically.
for location in locations:
    print(location)

```

A sample location can be found here:

```json
{
  "locationId": "vg_3880",
  "name": "Stage Theater im Hafen Hamburg",
  "description": "Erleben Sie live wie Kunst, Phantasie, Traum und Wirklichkeit miteinander verschmelzen.",
  "city": "Hamburg",
  "link": "https://www.eventim.de/city/hamburg-7/venue/stage-theater-im-hafen-hamburg-3880/",
  "url": {
    "path": "/city/hamburg-7/venue/stage-theater-im-hafen-hamburg-3880/",
    "domain": "https://www.eventim.de"
  },
  "imageUrl": "https://www.eventim.de/obj/media/DE-eventim/teaser/venue/222x222/2012/stage-theater-im-hafen-tickets-hamburg.jpg",
  "rating": {
    "count": 2842,
    "average": 4.585855007171631
  }
}
```

### explore_product_groups

The explore_attractions returns matching product groups with the 5 most relevant products based on the provided parameters.
A product group is something like a tour, musical, festival, etc.
A product is a concert, festical day pass, musical performance

Please note that time_from and time_to are matched against the event start date. Therefore the below will return the product groups and 5 latest products for "Disneys DER KÖNIG DER LÖWEN"
between 2024-12-01 and 2024-12-31 with a start time between 3pm and 6pm.

```python
    product_groups = eventim.explore_product_groups(
        search_term="Disneys DER KÖNIG DER LÖWEN",
        sort="DateDesc",
        categories=["Musical & Show"],
        date_from=datetime.date(2024, 12, 1),
        date_to=datetime.date(2024, 12, 31),
        time_from=datetime.time(15, 00),
        time_to=datetime.time(18, 00),
    )

    for product_group in product_groups:
        print(product_group)
```

A sample product group can be found here:

```json
{
    "productGroupId": "473431",
    "name": "Disneys DER K\u00d6NIG DER L\u00d6WEN",
    "description": "Das Musical bringt die farbenpr\u00e4chtige Welt Afrikas mit wilden Tieren und der wundersch\u00f6nen Serengeti nach Hamburg.\n",
    "startDate": "2024-03-19T18:30:00+01:00",
    "endDate": "2025-12-21T18:30:00+01:00",
    "productCount": 678,
    "link": "https://www.eventim.de/artist/disneys-der-koenig-der-loewen/",
    "url": {
        "path": "/artist/disneys-der-koenig-der-loewen/",
        "domain": "https://www.eventim.de"
    },
    "imageUrl": "https://www.eventim.de/obj/media/DE-eventim/teaser/222x222/2022/disneys-koenig-der-loewen-musical-tickets-2022.jpg",
    "currency": "EUR",
    "rating": {
        "count": 5265,
        "average": 4.660600185394287
    },
    "categories": [
        {
            "name": "Musical & Show"
        },
        {
            "name": "Musical",
            "parentCategory": {
                "name": "Musical & Show"
            }
        }
    ],
    "tags": ["TICKETDIRECT", "FANTICKET", "MOBILE_TICKET", "FANSALE"],
    "status": "Available",
    "products": [
    {
        "productId": "18637122",
        "name": "Disneys DER K\u00d6NIG DER L\u00d6WEN",
        "type": "LiveEntertainment",
        "status": "Available",
        "link": "https://www.eventim.de/event/disneys-der-koenig-der-loewen-stage-theater-im-hafen-hamburg-18637122/",
        "url": {
            "path": "/event/disneys-der-koenig-der-loewen-stage-theater-im-hafen-hamburg-18637122/",
            "domain": "https://www.eventim.de"
        },
        "typeAttributes": {
            "liveEntertainment": {
                "startDate": "2024-12-31T17:00:00+01:00",
                "location": {
                    "name": "Stage Theater im Hafen Hamburg",
                    "city": "Hamburg",
                    "geoLocation": {
                    "longitude": 9.995280019552826,
                    "latitude": 53.545300001826604
                    }
                }
            }
        },
        "rating": {
            "count": 5265,
            "average": 4.660600185394287
        },
        "tags": ["TICKETDIRECT", "FANTICKET", "MOBILE_TICKET"],
        "hasRecommendation": false
        },
        ... 4 more products
    ]
}
```
