## Seatmap Endpoint

This endpoint can be used to get seatmap data of specific attraction.

Functionality can break without notice because this is parsed via HTML.

### get_event_seatmap_information

This function can return data about the seatmap if found in the HTML of the event page. If no seat map is found then None will be returned.

```python
# This will fetch the html for the given event. Note the url must match the structure in the example!
result = eventim.get_event_seatmap_information("/event/disneys-der-koenig-der-loewen-stage-theater-im-hafen-hamburg-18500464/")
```

A sample for the seatmap information can be found here (Note this is truncated.):

```json
{
  "fansale": { <- ... -> },
  "seatmapOptions": { <- ... -> },
  "seatmapIsDefault": false,
  "packageData": { <- ... -> },
  "price": { <- ... -> },
  "maxAmountForEvent": 10,
  "minAmountForEvent": 1,
  "maxAmountForPromo": 0,
  "preselectedPcId": 0,
  "showBackLink": false,
  "backLink": "/event/disneys-der-koenig-der-loewen-stage-theater-im-hafen-hamburg-16828914/",
  "eventName": "Disneys DER K\u00d6NIG DER L\u00d6WEN",
  "restrictions": { <- ... -> },
  "cartData": { <- ... -> },
  "panoramaOptions": { <- ... -> },
  "imageviewerOptions": { <- ... -> },
  "ccEnabled": true,
  "initialRequestPath": "/api/shoppingCart/?affiliate=EVE&token=518ACD577869FB764ED195DF569D347C",
  "captchaActive": false,
  "captchaAPIPath": "//www.google.com/recaptcha/api.js?hl=de",
  "captchaSiteKey": "",
  "pcFlyoutExpanded": true,
  "pcUpgradeActiveClass": "js-pc-upgrade-active",
  "pricePlaceholder": "#PRICE#",
  "hasPriceDisclaimerHint": false,
  "hasCorporateBenefits": false,
  "hasCombinedTicketTypes": false,
  "hasAllCategoriesToggleText": true,
  "reducedAvailabilityWidgetLink": "",
  "hasOptionsFilter": false,
  "ticketTypeFilterMap": { <- ... -> },
  "api": "/api/corporate/benefit/limits/?affiliate=EVE",
  "useParis24Styles": false,
  "messages": { <- ... -> }
}
```

### get_event_seatmap

This function returns seatmap data with avialible seats and their pricing data. This could be used to generate a seatmap image or make yield analytics.

```python
# This will fetch the html for the given event. Note the url must match the structure in the example!
result = eventim.get_event_seatmap_information("/event/disneys-der-koenig-der-loewen-stage-theater-im-hafen-hamburg-18500464/")
seatmap = eventim.get_event_seatmap(result["seatmapOptions"])
```

A sample for the seatmap information can be found here (Note this is fictional data):

```json
{
  "seatmap_key": "web_1_16828914_0_EVE_0",
  "seatmap_timestamp": 1716717879990,
  "seatmap_individual_seats": 2051,
  "seatmap_dimension_x": 8192,
  "seatmap_dimension_y": 8192,
  "seatmap_seat_size": 59,
  "blocks": [
    {
      "block_id": "b1",
      "block_name": "Parkett links",
      "block_description": "Parkett links",
      "block_rows": [
        {
          "row_code": "r4",
          "row_seats": [
            {
              "seat_code": "s515",
              "seat_price_category_index": 1,
              "seat_coordinate_x": 3846,
              "seat_coordinate_y": 1699
            }
          ]
        }
      ]
    }
  ],
  "price_categories": [
    {
      "price_category_id": "p32919041",
      "price_category_name": "Kat. 1 Premium",
      "price_category_color": "#f1075e"
    }
  ]
}
```
