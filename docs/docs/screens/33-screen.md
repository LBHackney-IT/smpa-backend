# 33. Declarations

## Update Declarations

![](/static/screen34.png)

### Example

`PATCH /api/v1/applications/{id}`

    {
        "declaration_id": "e0bbf434-9c28-4fe8-b4ae-892b3e359479"
    }

To update a declaration with the hidden fields filled too...

    {
        "declaration_id": "746b41c8-54b3-4cd6-89d7-2d41d1c55fbe",
        "declaration_detail": {
            "name": "Sido Jombati",
            "role": "Defender",
            "details": "Everyone's favourite defender"
        }
    }


## Update Ownership

![](/static/screen35.png)

### Example

`PATCH /api/v1/applications/{id}`

    {
        "ownership_type_id": "784e54c7-d6da-4613-ac5a-046a27278f4b"
    }


## Update Ownership Certificate Declaration

![](/static/screen36.png)

### Example

`PATCH /api/v1/applications/{id}`

    {
        "ownership_declaration": true
    }


## Update Fee Reduction Eligibility

![](/static/screen37.png)

### Example

`PATCH /api/v1/applications/{id}`

    {
        "reduction_eligible": true
    }


