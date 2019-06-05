# 3. About the extension or alteration

![](/static/screen3.png)

`PATCH /api/v1/extension-proposals/{id}`

    original_house: json
    incidental_buildings: json
    gates_fences_etc: json
    means_of_access_to_site: json
    car_bike_spaces: json

For each option that the user has checked, send an empty json object {}

## Example

    {
        "original_house": {},
        "incidental_buildings": {}
    }

### Returns

This returns an extension proposal object. You'll need the ID from this for future calls to update the proposal.

    {
      "id": "fb104ff2-eece-4f26-ab2a-1bc8c666ab67",
      "created_at": "2019-04-04T14:47:32.608333",
      "updated_at": "2019-04-04T14:47:32.608385",
      "application_id": "9e7cf43a-6860-4061-b585-65b4fb778a30",
      "original_house": {
        "id": null,
        "created_at": "2019-04-04T14:47:32.608544",
        "updated_at": "2019-04-04T14:47:32.608577",
        "single_storey_extension": null,
        "two_storey_extension": null,
        "part_single_part_two_storey_extension": null,
        "basement": null,
        "roof_works": null,
        "outbuilding": null,
        "porch": null,
        "balcony_terrace": null,
        "staircase": null,
        "add_replacement_windows_doors": null,
        "cladding": null
      },
      "incidental_buildings": {
        "id": null,
        "created_at": "2019-04-04T14:47:32.608974",
        "updated_at": "2019-04-04T14:47:32.609007",
        "removal_or_demolition": false,
        "details": null
      },
      "gates_fences_etc": null,
      "means_of_access_to_site": null,
      "car_bike_spaces": null
    }
