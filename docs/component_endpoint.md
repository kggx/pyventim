## Component Endpoint

This endpoint can be used to get data to specifict attractions. An example would be all events by an artist. The data is fetched by a lxml parser to look for key words in the HTML code that include interesting data.

Functionality can break without notice because this is parsed via HTML.

### get_attraction_events

This endpoint fetches data about upcomming events in the [https://schema.org/MusicEvent](https://schema.org/MusicEvent) schema. Attraction ids can be found in the `explore_attractions` function.

**Note**: This only returns the next 90 events. If you need more events consider using the [get_attraction_events_from_calendar](###get_attraction_events_from_calendar) function which is faster in any case.

```python
# The attraction id for "Disneys DER KÖNIG DER LÖWEN"
attraction_id = 473431

# Return the next 7 days
now = datetime.datetime.now()
date_from = now.date()
date_to = (now + datetime.timedelta(days=7)).date()

# Make the request and loop over attraction events
attraction_events = eventim.get_attraction_events(
    attraction_id=attraction_id,
    date_from=date_from,
    date_to=date_to,
)

for attraction_event in attraction_events:
    print(attraction_event)

```

A sample attraction event can be found here:

```json
{
  "@context": "https://schema.org",
  "@type": "MusicEvent",
  "description": "Das Musical bringt die farbenpr\u00e4chtige Welt Afrikas mit wilden Tieren und der wundersch\u00f6nen Serengeti nach Hamburg.\n",
  "endDate": "2024-05-21T18:30:00.000+02:00",
  "image": [
    "https://www.eventim.de/obj/media/DE-eventim/teaser/222x222/2022/disneys-koenig-der-loewen-musical-tickets-2022.jpg",
    "https://www.eventim.de/obj/media/DE-eventim/teaser/222x222/2022/disneys-koenig-der-loewen-musical-tickets-2022.jpg",
    "https://www.eventim.de/obj/media/DE-eventim/teaser/artworks/2024/disneys-der-koenig-der-loewen-musical-tickets-header.jpg"
  ],
  "location": {
    "name": "Stage Theater im Hafen Hamburg",
    "sameAs": "https://www.eventim.de/city/hamburg-7/venue/stage-theater-im-hafen-hamburg-3880/",
    "address": {
      "streetAddress": "Norderelbstrasse 6",
      "postalCode": "20457",
      "addressLocality": "Hamburg",
      "addressRegion": "",
      "addressCountry": "DE",
      "@type": "PostalAddress"
    },
    "@type": "Place"
  },
  "name": "Disneys DER K\u00d6NIG DER L\u00d6WEN",
  "offers": {
    "category": "primary",
    "price": 96.99000000000001,
    "priceCurrency": "EUR",
    "availability": "InStock",
    "url": "https://www.eventim.de/event/disneys-der-koenig-der-loewen-stage-theater-im-hafen-hamburg-16825147/",
    "validFrom": "2023-03-28T10:00:00.000+02:00",
    "@type": "Offer"
  },
  "performer": {
    "name": "Disneys DER K\u00d6NIG DER L\u00d6WEN",
    "@type": "PerformingGroup"
  },
  "startDate": "2024-05-21T18:30:00.000+02:00",
  "url": "https://www.eventim.de/event/disneys-der-koenig-der-loewen-stage-theater-im-hafen-hamburg-16825147/"
}
```

### get_attraction_events_from_calendar

This function will return all available events for the attraction with similar data like the [get_attraction_events](###get_attraction_events) function. Attraction ids can be found in the `explore_attractions` function.

```python
# The attraction id for "Disneys DER KÖNIG DER LÖWEN"
attraction_id = 473431

# Return the next 7 days
now = datetime.datetime.now()
date_from = now.date()
date_to = (now + datetime.timedelta(days=7)).date()

# Make the request and loop over attraction calendar events
attraction_calendar_events = eventim.get_attraction_events_from_calendar(
    attraction_id=attraction_id,
    date_from=date_from,
    date_to=date_to,
)

for attraction_calendar_event in attraction_calendar_events:
    print(attraction_calendar_event)
```

A sample calendar attraction event can be found here:

```json
{
  "id": "16825147",
  "title": "Disneys DER K\u00d6NIG DER L\u00d6WEN",
  "url": "/event/disneys-der-koenig-der-loewen-stage-theater-im-hafen-hamburg-16825147/",
  "start": "2024-05-21T18:30:00",
  "eventTime": "18:30",
  "price": "ab \u20ac\u00a096,99",
  "eventDate": "21.05.2024",
  "tileFirstLine": "\u00a0",
  "priceAvailable": true,
  "ticketAvailable": true,
  "ticketStatusMessage": "Verf\u00fcgbar",
  "eventState": 2,
  "voucher": false,
  "promotionContained": false,
  "subscriptionPackage": false,
  "subscriptionPackageData": null,
  "venueName": "\u00a0",
  "first": "Disneys DER K\u00d6NIG DER L\u00d6WEN",
  "second": "HAMBURG",
  "third": "Stage Theater im Hafen Hamburg",
  "eventWeekday": "Dienstag",
  "identicalCity": true,
  "identicalVenue": true,
  "marketingLabels": [],
  "clubIcon": {
    "iconVisible": false,
    "marketingLabel": null,
    "ticketTypeInfoVisible": false,
    "ticketTypeInfo": "",
    "iconColor": ""
  },
  "subListings": [],
  "externalOffers": false,
  "tdlId": 3357219,
  "formattedDay": "21",
  "formattedMonthYear": "Mai 2024",
  "formattedWeekdayTime": "Di. 18:30",
  "formattedIsoDate": "2024-05-21T18:30:00.000+02:00",
  "continuousEventData": null,
  "eventFavoritesItem": null,
  "imagePath": null,
  "linkToModalLayer": null,
  "medalIcon": null,
  "genderIcon": null,
  "formattedDateTime": null,
  "desc1": null,
  "desc2": null,
  "crossedOutPrice": "",
  "bookable": true,
  "availabilityIndicator": -1,
  "willCall": false,
  "ticketDirect": true,
  "eventimPass": false,
  "mobileTicket": true,
  "fanticket": true,
  "red": false,
  "trackingData": {
    "label": "1",
    "id": "16825147",
    "name": "Disneys DER K&Ouml;NIG DER L&Ouml;WEN"
  }
}
```
