# 35. Submitting

## Submit an application

`PATCH /api/v1/applications/{id}/submit`

This endpoint will only accept a body of...

    {
        "submitted": true
    }

It then sets the `status_id` of the application, updates the `reference` if it's still a DRAFT reference (ie: if the user has skipped payment), and sets a `submitted_at` time stamp.

