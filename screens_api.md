# Starting the works

POST /api/v1/applications

    works_started: bool
    date_works_started: date
    works_completed: bool
    date_works_completed: date
    works_description: str

Returns
    application: json


# About the works

POST /api/v1/extension-proposals

    application_id: str

Returns
    extension-proposal: json

POST /api/v1/equipment-proposals

    application_id: str

Returns
    equipment-proposal: json


# About the extension or alteration

PATCH /api/v1/extension-proposals/{id}


