# SmPA API

This API backend is focused on development speed and agility due to the number of unknowns around the schema, SSO and accounts.

For this reason it is using the schemaless RethinkDB which also has built in GIS support.

## Technical design

The app uses schematics models so that data structures can still be enforced at a code level. This allows us to validate data in and out against schematics. All model access should be via a service class so that the data store can be swapped out for a different one at any time in the future. Currently, even though development on RethinkDB has stalled, it's still the best and most developer-friendly, GIS enabled, schemaless data store around.

## Getting started

    pip install -r smpaf/requirements.txt
    gunicorn --reload smpaf.app -b 0.0.0.0:5000


## IPython Shell

Use `konch` to get a shell. This preloads some useful things including the app.

