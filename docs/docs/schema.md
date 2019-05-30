# Generated Schema

This is the generated OpenAPI schema doc. Still to do is generating the fields of the model schemas and correctly linking refs where they're mentioned in the paths.


    {
      "paths": {
        "/api/v1/addresses": {
          "get": {
            "summary": "Get all Addresses from the DB",
            "tags": [
              "Address"
            ],
            "parameters": [
              {
                "in": "query",
                "schema": "CoreListSchema"
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All Addresses",
                "schema": {
                  "type": "array",
                  "items": "Address"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add a new Address to the database",
            "tags": [
              "Address"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "Address"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "Address created successfully",
                "schema": "Address"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/addresses/{id}": {
          "get": {
            "summary": "Get one or more Addresses from the database",
            "tags": [
              "Address"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "One or more Addresses",
                "schema": {
                  "type": "array",
                  "items": "Address"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update an Address in the database",
            "tags": [
              "Address"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "Address"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated Address",
                "schema": "Address"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {}
        },
        "/api/v1/site-addresses": {
          "get": {
            "summary": "Get all SiteAddresses from the DB",
            "tags": [
              "Address"
            ],
            "parameters": [
              {
                "in": "query",
                "schema": "CoreListSchema"
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All SiteAddresses",
                "schema": {
                  "type": "array",
                  "items": "SiteAddress"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add new SiteAddress to the database",
            "tags": [
              "SiteAddress"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "SiteAddress"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "SiteAddress created successfully",
                "schema": "SiteAddress"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/site-addresses/{id}": {
          "get": {
            "summary": "Get one or more SiteAddresses from the database",
            "tags": [
              "SiteAddress"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "One or more SiteAddresses",
                "schema": "SiteAddress"
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update a SiteAddress in the database",
            "tags": [
              "SiteAddress"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "SiteAddress"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated SiteAddress",
                "schema": "SiteAddress"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {}
        },
        "/api/v1/site-areas": {
          "get": {
            "summary": "Get all SiteAreas from the DB",
            "tags": [
              "SiteArea"
            ],
            "parameters": [
              {
                "in": "query",
                "schema": "CoreListSchema"
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All SiteAreas",
                "schema": {
                  "type": "array",
                  "items": "SiteArea"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add new SiteArea to the database",
            "tags": [
              "SiteArea"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              },
              {
                "in": "body",
                "schema": "SiteArea"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "SiteArea created successfully",
                "schema": "SiteArea"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/site-areas/{id}": {
          "get": {
            "summary": "Get one SiteArea from the DB",
            "tags": [
              "SiteArea"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "The requested SiteArea",
                "schema": "SiteArea"
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update an SiteArea in the database",
            "tags": [
              "SiteArea"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              },
              {
                "in": "body",
                "schema": "SiteArea"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated SiteArea",
                "schema": "SiteArea"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {}
        },
        "/api/v1/site-constraints": {
          "get": {
            "summary": "Get all SiteConstraintss from the DB",
            "tags": [
              "SiteConstraints"
            ],
            "parameters": [
              {
                "in": "query",
                "schema": "CoreListSchema"
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All SiteConstraintss",
                "schema": {
                  "type": "array",
                  "items": "SiteConstraints"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add new SiteConstraints to the database",
            "tags": [
              "SiteConstraints"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "SiteConstraints"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "SiteConstraints created successfully",
                "schema": "SiteConstraints"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/site-constraints/{id}": {
          "get": {
            "summary": "Get one SiteConstraints from the database",
            "tags": [
              "SiteConstraints"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "One SiteConstraints",
                "schema": "SiteConstraints"
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update an SiteConstraints in the database",
            "tags": [
              "SiteConstraints"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "SiteConstraints"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated SiteConstraints",
                "schema": "SiteConstraints"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {}
        },
        "/api/v1/works-locations": {
          "get": {
            "summary": "Get all WorksLocations from the DB",
            "tags": [
              "WorksLocation"
            ],
            "parameters": [
              {
                "in": "query",
                "schema": "CoreListSchema"
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All WorksLocations",
                "schema": {
                  "type": "array",
                  "items": "WorksLocation"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add new WorksLocation to the database",
            "tags": [
              "WorksLocation"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              },
              {
                "in": "body",
                "schema": "WorksLocation"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "WorksLocation created successfully",
                "schema": "WorksLocation"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/works-locations/{id}": {
          "get": {
            "summary": "Get one WorksLocation from the DB",
            "tags": [
              "WorksLocation"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "The requested WorksLocation",
                "schema": "WorksLocation"
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update an WorksLocation in the database",
            "tags": [
              "WorksLocation"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              },
              {
                "in": "body",
                "schema": "WorksLocation"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated WorksLocation",
                "schema": "WorksLocation"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {}
        },
        "/api/v1/basement-works-types": {
          "get": {
            "summary": "Get all BasementWorksTypes from the DB",
            "tags": [
              "BasementWorksType"
            ],
            "parameters": [
              {
                "in": "query",
                "schema": "CoreListSchema"
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All BasementWorksTypes",
                "schema": {
                  "type": "array",
                  "items": "BasementWorksType"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add new BasementWorksType to the database",
            "tags": [
              "BasementWorksType"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "BasementWorksType"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "BasementWorksType created successfully",
                "schema": "BasementWorksType"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/basement-works-types/{id}": {
          "get": {
            "summary": "Get one BasementWorksType from the database",
            "tags": [
              "BasementWorksType"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "One BasementWorksType",
                "schema": "BasementWorksType"
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update an BasementWorksType in the database",
            "tags": [
              "BasementWorksType"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "BasementWorksType"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated BasementWorksType",
                "schema": "BasementWorksType"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {}
        },
        "/api/v1/roof-works-types": {
          "get": {
            "summary": "Get all RoofWorksTypes from the DB",
            "tags": [
              "RoofWorksType"
            ],
            "parameters": [
              {
                "in": "query",
                "schema": "CoreListSchema"
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All RoofWorksTypes",
                "schema": {
                  "type": "array",
                  "items": "RoofWorksType"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add new RoofWorksType to the database",
            "tags": [
              "RoofWorksType"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "RoofWorksType"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "RoofWorksType created successfully",
                "schema": "RoofWorksType"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/roof-works-types/{id}": {
          "get": {
            "summary": "Get one RoofWorksType from the database",
            "tags": [
              "RoofWorksType"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "One RoofWorksType",
                "schema": "RoofWorksType"
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update an RoofWorksType in the database",
            "tags": [
              "RoofWorksType"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "RoofWorksType"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated RoofWorksType",
                "schema": "RoofWorksType"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {}
        },
        "/api/v1/border-works-types": {
          "get": {
            "summary": "Get all BorderWorksTypes from the DB",
            "tags": [
              "BorderWorksType"
            ],
            "parameters": [
              {
                "in": "query",
                "schema": "CoreListSchema"
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All BorderWorksTypes",
                "schema": {
                  "type": "array",
                  "items": "BorderWorksType"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add new BorderWorksType to the database",
            "tags": [
              "BorderWorksType"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "BorderWorksType"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "BorderWorksType created successfully",
                "schema": "BorderWorksType"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/border-works-types/{id}": {
          "get": {
            "summary": "Get one BorderWorksType from the database",
            "tags": [
              "BorderWorksType"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "One BorderWorksType",
                "schema": "BorderWorksType"
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update an BorderWorksType in the database",
            "tags": [
              "BorderWorksType"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "BorderWorksType"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated BorderWorksType",
                "schema": "BorderWorksType"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {}
        },
        "/api/v1/access-works-scopes": {
          "get": {
            "summary": "Get all AccessWorksScopes from the DB",
            "tags": [
              "AccessWorksScope"
            ],
            "parameters": [
              {
                "in": "query",
                "schema": "CoreListSchema"
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All AccessWorksScopes",
                "schema": {
                  "type": "array",
                  "items": "AccessWorksScope"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add new AccessWorksScope to the database",
            "tags": [
              "AccessWorksScope"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "AccessWorksScope"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "AccessWorksScope created successfully",
                "schema": "AccessWorksScope"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/access-works-scopes/{id}": {
          "get": {
            "summary": "Get one AccessWorksScope from the database",
            "tags": [
              "AccessWorksScope"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "One AccessWorksScope",
                "schema": "AccessWorksScope"
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update an AccessWorksScope in the database",
            "tags": [
              "AccessWorksScope"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "AccessWorksScope"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated AccessWorksScope",
                "schema": "AccessWorksScope"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {}
        },
        "/api/v1/access-works-types": {
          "get": {
            "summary": "Get all AccessWorksTypes from the DB",
            "tags": [
              "AccessWorksType"
            ],
            "parameters": [
              {
                "in": "query",
                "schema": "CoreListSchema"
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All AccessWorksTypes",
                "schema": {
                  "type": "array",
                  "items": "AccessWorksType"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add new AccessWorksType to the database",
            "tags": [
              "AccessWorksType"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "AccessWorksType"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "AccessWorksType created successfully",
                "schema": "AccessWorksType"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/access-works-types/{id}": {
          "get": {
            "summary": "Get one AccessWorksType from the database",
            "tags": [
              "AccessWorksType"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "One AccessWorksType",
                "schema": "AccessWorksType"
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update an AccessWorksType in the database",
            "tags": [
              "AccessWorksType"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "AccessWorksType"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated AccessWorksType",
                "schema": "AccessWorksType"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {}
        },
        "/api/v1/parking-works-scopes": {
          "get": {
            "summary": "Get all ParkingWorksScopes from the DB",
            "tags": [
              "ParkingWorksScope"
            ],
            "parameters": [
              {
                "in": "query",
                "schema": "CoreListSchema"
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All ParkingWorksScopes",
                "schema": {
                  "type": "array",
                  "items": "ParkingWorksScope"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add new ParkingWorksScope to the database",
            "tags": [
              "ParkingWorksScope"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "ParkingWorksScope"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "ParkingWorksScope created successfully",
                "schema": "ParkingWorksScope"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/parking-works-scopes/{id}": {
          "get": {
            "summary": "Get one ParkingWorksScope from the database",
            "tags": [
              "ParkingWorksScope"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "One ParkingWorksScope",
                "schema": "ParkingWorksScope"
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update an ParkingWorksScope in the database",
            "tags": [
              "ParkingWorksScope"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "ParkingWorksScope"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated ParkingWorksScope",
                "schema": "ParkingWorksScope"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {}
        },
        "/api/v1/equipment-works-types": {
          "get": {
            "summary": "Get all EquipmentWorksTypes from the DB",
            "tags": [
              "EquipmentWorksType"
            ],
            "parameters": [
              {
                "in": "query",
                "schema": "CoreListSchema"
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All EquipmentWorksTypes",
                "schema": {
                  "type": "array",
                  "items": "EquipmentWorksType"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add new EquipmentWorksType to the database",
            "tags": [
              "EquipmentWorksType"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "EquipmentWorksType"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "EquipmentWorksType created successfully",
                "schema": "EquipmentWorksType"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/equipment-works-types/{id}": {
          "get": {
            "summary": "Get one EquipmentWorksType from the database",
            "tags": [
              "EquipmentWorksType"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "One EquipmentWorksType",
                "schema": "EquipmentWorksType"
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update an EquipmentWorksType in the database",
            "tags": [
              "EquipmentWorksType"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "EquipmentWorksType"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated EquipmentWorksType",
                "schema": "EquipmentWorksType"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {}
        },
        "/api/v1/equipment-works-conservation-types": {
          "get": {
            "summary": "Get all EquipmentWorksConservationTypes from the DB",
            "tags": [
              "EquipmentWorksConservationType"
            ],
            "parameters": [
              {
                "in": "query",
                "schema": "CoreListSchema"
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All EquipmentWorksConservationTypes",
                "schema": {
                  "type": "array",
                  "items": "EquipmentWorksConservationType"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add new EquipmentWorksConservationType to the database",
            "tags": [
              "EquipmentWorksConservationType"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "EquipmentWorksConservationType"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "EquipmentWorksConservationType created successfully",
                "schema": "EquipmentWorksConservationType"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/equipment-works-conservation-types/{id}": {
          "get": {
            "summary": "Get one EquipmentWorksConservationType from the database",
            "tags": [
              "EquipmentWorksConservationType"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "One EquipmentWorksConservationType",
                "schema": "EquipmentWorksConservationType"
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update an EquipmentWorksConservationType in the database",
            "tags": [
              "EquipmentWorksConservationType"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "EquipmentWorksConservationType"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated EquipmentWorksConservationType",
                "schema": "EquipmentWorksConservationType"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {}
        },
        "/api/v1/area-units/{id}": {
          "get": {
            "summary": "Get one AreaUnit from the DB",
            "tags": [
              "AreaUnit"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "The requested AreaUnit",
                "schema": "AreaUnit"
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update an AreaUnit in the database",
            "tags": [
              "AreaUnit"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              },
              {
                "in": "body",
                "schema": "AreaUnit"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated AreaUnit",
                "schema": "AreaUnit"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {
            "summary": "Add new AreaUnit to the database",
            "tags": [
              "AreaUnit"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              },
              {
                "in": "body",
                "schema": "AreaUnit"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "AreaUnit created successfully",
                "schema": "AreaUnit"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/area-units": {
          "get": {
            "summary": "Get all AreaUnits from the DB",
            "tags": [
              "AreaUnit"
            ],
            "parameters": [
              {
                "in": "query",
                "schema": "CoreListSchema"
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All AreaUnits",
                "schema": {
                  "type": "array",
                  "items": "AreaUnit"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {}
        },
        "/api/v1/linear-units": {
          "get": {
            "summary": "Get all LinearUnits from the DB",
            "tags": [
              "LinearUnit"
            ],
            "parameters": [
              {
                "in": "query",
                "schema": "CoreListSchema"
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All LinearUnits",
                "schema": {
                  "type": "array",
                  "items": "LinearUnit"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {}
        },
        "/api/v1/linear-units/{id}": {
          "get": {
            "summary": "Get one LinearUnit from the database",
            "tags": [
              "LinearUnit"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "One LinearUnit",
                "schema": "LinearUnit"
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update an LinearUnit in the database",
            "tags": [
              "LinearUnit"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "LinearUnit"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated LinearUnit",
                "schema": "LinearUnit"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {
            "summary": "Add new LinearUnit to the database",
            "tags": [
              "LinearUnit"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "LinearUnit"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "LinearUnit created successfully",
                "schema": "LinearUnit"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/users/{id}": {
          "get": {
            "summary": "Get one or more Users from the database",
            "tags": [
              "User"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "One or more Users",
                "schema": {
                  "type": "array",
                  "items": "User"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update a User in the database",
            "tags": [
              "User"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "User"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated User",
                "schema": "User"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {
            "summary": "Add new User to the database",
            "tags": [
              "User"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "User"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "User created successfully",
                "schema": "User"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/agents/{id}": {
          "get": {
            "summary": "Get one or more Agents from the database",
            "tags": [
              "Agent"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "One or more Agents",
                "schema": {
                  "type": "array",
                  "items": "Agent"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update an Agent in the database",
            "tags": [
              "Agent"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "Agent"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated Agent",
                "schema": "Agent"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {
            "summary": "Add new Agent to the database",
            "tags": [
              "Agent"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "Agent"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "Agent created successfully",
                "schema": "Agent"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/document-sizes/{id}": {
          "get": {
            "summary": "Get one or more DocumentSizes from the database",
            "tags": [
              "DocumentSize"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "One or more DocumentSizes",
                "schema": {
                  "type": "array",
                  "items": "DocumentSize"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update a DocumentSize in the database",
            "tags": [
              "DocumentSize"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "DocumentSize"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated DocumentSize",
                "schema": "DocumentSize"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {
            "summary": "Add new DocumentSize to the database",
            "tags": [
              "DocumentSize"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "DocumentSize"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "DocumentSize created successfully",
                "schema": "DocumentSize"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/auth": {
          "post": {
            "summary": "Login into user account and generate JWT",
            "tags": [
              "Login"
            ],
            "parameters": [
              {
                "in": "body",
                "schema": "LoginSchema"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Login Successful",
                "schema": {
                  "type": "object",
                  "properties": {
                    "message": {
                      "type": "string"
                    },
                    "jwt": {
                      "type": "string"
                    }
                  }
                }
              },
              "401": {
                "description": "Login Unsuccessful"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/materials/options/roof": {
          "get": {
            "summary": "Get one or more MaterialOptionRoofs from the database",
            "tags": [
              "MaterialOptionRoof"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "One or more MaterialOptionRoofs",
                "schema": {
                  "type": "array",
                  "items": "MaterialOptionRoof"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update a MaterialOptionRoof in the database",
            "tags": [
              "MaterialOptionRoof"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              },
              {
                "in": "body",
                "schema": "MaterialOptionRoof"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated MaterialOptionRoof",
                "schema": "MaterialOptionRoof"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {
            "summary": "Add new MaterialOptionRoof to the database",
            "tags": [
              "MaterialOptionRoof"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              },
              {
                "in": "body",
                "schema": "MaterialOptionRoof"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "MaterialOptionRoof created successfully",
                "schema": "MaterialOptionRoof"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/materials/options/wall": {
          "get": {
            "summary": "Get one or more MaterialOptionWalls from the database",
            "tags": [
              "MaterialOptionWall"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              },
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "One or more MaterialOptionWalls",
                "schema": {
                  "type": "array",
                  "items": "MaterialOptionWall"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update a MaterialOptionWall in the database",
            "tags": [
              "MaterialOptionWall"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              },
              {
                "in": "body",
                "schema": "MaterialOptionWall"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated MaterialOptionWall",
                "schema": "MaterialOptionWall"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {
            "summary": "Add new MaterialOptionWall to the database",
            "tags": [
              "MaterialOptionWall"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              },
              {
                "in": "body",
                "schema": "MaterialOptionWall"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "MaterialOptionWall created successfully",
                "schema": "MaterialOptionWall"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/materials/options/door": {
          "get": {
            "summary": "Get one or more MaterialOptionDoors from the database",
            "tags": [
              "MaterialOptionDoor"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              },
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "One or more MaterialOptionDoors",
                "schema": {
                  "type": "array",
                  "items": "MaterialOptionDoor"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update a MaterialOptionDoor in the database",
            "tags": [
              "MaterialOptionDoor"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              },
              {
                "in": "body",
                "schema": "MaterialOptionDoor"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated MaterialOptionDoor",
                "schema": "MaterialOptionDoor"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {
            "summary": "Add new MaterialOptionDoor to the database",
            "tags": [
              "MaterialOptionDoor"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              },
              {
                "in": "body",
                "schema": "MaterialOptionDoor"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "MaterialOptionDoor created successfully",
                "schema": "MaterialOptionDoor"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/materials/options/window": {
          "get": {
            "summary": "Get one or more MaterialOptionWindows from the database",
            "tags": [
              "MaterialOptionWindow"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              },
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "One or more MaterialOptionWindows",
                "schema": {
                  "type": "array",
                  "items": "MaterialOptionWindow"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update a MaterialOptionWindow in the database",
            "tags": [
              "MaterialOptionWindow"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              },
              {
                "in": "body",
                "schema": "MaterialOptionWindow"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated MaterialOptionWindow",
                "schema": "MaterialOptionWindow"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {
            "summary": "Add new MaterialOptionWindow to the database",
            "tags": [
              "MaterialOptionWindow"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              },
              {
                "in": "body",
                "schema": "MaterialOptionWindow"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "MaterialOptionWindow created successfully",
                "schema": "MaterialOptionWindow"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        },
        "/api/v1/applications": {
          "get": {
            "summary": "Get all Applications from the DB",
            "tags": [
              "Application"
            ],
            "parameters": [
              {
                "in": "query",
                "schema": "CoreListSchema"
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All Applications",
                "schema": {
                  "type": "array",
                  "items": "Application"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {}
        },
        "/api/v1/applications/{id}": {
          "get": {
            "summary": "Get one Application from the DB",
            "tags": [
              "Application"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "The requested Application",
                "schema": "Application"
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update an Application in the database",
            "tags": [
              "Application"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              },
              {
                "in": "body",
                "schema": "Application"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "Returns updated Application",
                "schema": "Application"
              },
              "401": {
                "description": "Unauthorized"
              },
              "404": {
                "description": "Object does not exist"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          },
          "post": {
            "summary": "Add new Application to the database",
            "tags": [
              "Application"
            ],
            "parameters": [
              {
                "in": "path",
                "schema": "CoreGetSchema",
                "required": true
              },
              {
                "in": "body",
                "schema": "Application"
              }
            ],
            "consumes": [
              "application/json"
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "201": {
                "description": "Application created successfully",
                "schema": "Application"
              },
              "401": {
                "description": "Unauthorized"
              },
              "422": {
                "description": "Input body formatting issue"
              }
            }
          }
        }
      },
      "tags": [],
      "info": {
        "title": "Submit my Planning Application",
        "version": "1.0.0"
      },
      "openapi": "3.0",
      "components": {
        "schemas": {
          "SiteArea": {},
          "SiteConstraints": {},
          "Test": {},
          "AreaUnit": {},
          "LinearUnit": {},
          "Role": {},
          "PersonName": {},
          "ContactMethod": {},
          "Email": {},
          "UserProfile": {},
          "TelephoneNumber": {},
          "TelephoneNumberType": {},
          "Applicant": {},
          "Agent": {},
          "User": {},
          "WorksLocation": {},
          "BasementWorksType": {},
          "RoofWorksType": {},
          "BorderWorksType": {},
          "AccessWorksScope": {},
          "AccessWorksType": {},
          "ParkingWorksScope": {},
          "EquipmentWorksType": {},
          "EquipmentWorksConservationType": {},
          "WorkExtensionOption": {},
          "ExtensionOriginalHouseSingleStoreyExtension": {},
          "ExtensionOriginalHouseTwoStoreyExtension": {},
          "ExtensionOriginalHousePartSinglePartTwoStoreyExtension": {},
          "ExtensionOriginalHouseBasement": {},
          "ExtensionOriginalHouseRoofWorks": {},
          "ExtensionOriginalHouseOutbuilding": {},
          "ExtensionOriginalHousePorch": {},
          "ExtensionOriginalHouseBalconyTerrace": {},
          "ExtensionOriginalHouseStaircase": {},
          "ExtensionOriginalHouseAddReplacementWindowsDoors": {},
          "ExtensionOriginalHouseCladding": {},
          "Work": {},
          "WorkExtensionOriginalHouse": {},
          "WorkExtensionIncidentalBuildings": {},
          "WorkExtensionGatesFencesEtc": {},
          "WorkExtensionMeansOfAccessToSite": {},
          "WorkExtensionCarBikeSpaces": {},
          "WorkEquipment": {},
          "WorkTrees": {},
          "Application": {},
          "Address": {},
          "SiteAddress": {},
          "Article4Direction": {},
          "BS7666Address": {},
          "InternationalAddress": {},
          "ExternalAddress": {},
          "DocumentSize": {},
          "MaterialOption": {},
          "MaterialOptionRoof": {},
          "MaterialOptionWall": {},
          "MaterialOptionWindow": {},
          "MaterialOptionDoor": {},
          "BaseExistingMaterial": {},
          "BaseMaterial": {},
          "MaterialRoof": {},
          "MaterialWall": {},
          "MaterialWindow": {},
          "MaterialDoor": {},
          "OtherMaterial": {},
          "ExternalBuildingMaterial": {},
          "WorksProposal": {},
          "ProposalExtension": {},
          "ProposalEquipment": {}
        },
        "parameters": {},
        "responses": {},
        "securitySchemes": {}
      }
    }
