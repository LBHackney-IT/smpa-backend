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
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
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
                  "items": {
                    "$ref": "#/components/schemas/Address"
                  }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.113171+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.113337+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "number": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "property_name": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "address_line_1": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "address_line_2": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "address_line_3": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "town_city": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "postcode": {
                      "type": "string",
                      "maxLength": 15
                    }
                  },
                  "required": [
                    "postcode"
                  ]
                }
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
                "schema": {
                  "$ref": "#/components/schemas/Address"
                }
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
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
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
                  "items": {
                    "$ref": "#/components/schemas/Address"
                  }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.123982+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.124139+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "number": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "property_name": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "address_line_1": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "address_line_2": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "address_line_3": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "town_city": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "postcode": {
                      "type": "string",
                      "maxLength": 15
                    }
                  },
                  "required": [
                    "postcode"
                  ]
                }
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
                "schema": {
                  "$ref": "#/components/schemas/Address"
                }
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
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
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
                  "items": {
                    "$ref": "#/components/schemas/SiteAddress"
                  }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.134077+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.134228+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "number": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "property_name": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "address_line_1": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "address_line_2": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "address_line_3": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "town_city": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "postcode": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 15
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "easting": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "northing": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "ward": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "bplu": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "uprn": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "property_type": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "description": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "application_id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
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
                "schema": {
                  "$ref": "#/components/schemas/SiteAddress"
                }
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
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "One or more SiteAddresses",
                "schema": {
                  "$ref": "#/components/schemas/SiteAddress"
                }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.151913+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.152175+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "number": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "property_name": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "address_line_1": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "address_line_2": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "address_line_3": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "town_city": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "postcode": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 15
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "easting": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "northing": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "ward": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "bplu": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "uprn": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "property_type": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "description": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "application_id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
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
                "schema": {
                  "$ref": "#/components/schemas/SiteAddress"
                }
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
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
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
                  "items": {
                    "$ref": "#/components/schemas/SiteArea"
                  }
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
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.171105+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.171266+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "area": {
                      "type": "number",
                      "format": "float"
                    }
                  },
                  "required": [
                    "area"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "unit": {
                      "type": "string",
                      "format": "uuid"
                    }
                  },
                  "required": [
                    "unit"
                  ]
                }
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
                "schema": {
                  "$ref": "#/components/schemas/SiteArea"
                }
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
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "The requested SiteArea",
                "schema": {
                  "$ref": "#/components/schemas/SiteArea"
                }
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
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.181793+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.181954+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "area": {
                      "type": "number",
                      "format": "float"
                    }
                  },
                  "required": [
                    "area"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "unit": {
                      "type": "string",
                      "format": "uuid"
                    }
                  },
                  "required": [
                    "unit"
                  ]
                }
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
                "schema": {
                  "$ref": "#/components/schemas/SiteArea"
                }
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
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
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
                  "items": {
                    "$ref": "#/components/schemas/SiteConstraints"
                  }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.191927+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.192089+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "has_boundry": {
                      "type": "string",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "nb_a4d": {
                      "type": "integer",
                      "format": "int32",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "a4d_name": {
                      "type": "string",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "nb_conarea": {
                      "type": "integer",
                      "format": "int32",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "conarea_name": {
                      "type": "string",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "nb_tpo": {
                      "type": "integer",
                      "format": "int32",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "tpo_name": {
                      "type": "string",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "is_listed_building": {
                      "type": "string",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "is_floodzone_2": {
                      "type": "string",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "is_floodzone_3a": {
                      "type": "string",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "is_floodzone_3b": {
                      "type": "string",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "geom": {
                      "type": "string",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "application_id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
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
                "schema": {
                  "$ref": "#/components/schemas/SiteConstraints"
                }
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
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "One SiteConstraints",
                "schema": {
                  "$ref": "#/components/schemas/SiteConstraints"
                }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.202182+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.202333+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "has_boundry": {
                      "type": "string",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "nb_a4d": {
                      "type": "integer",
                      "format": "int32",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "a4d_name": {
                      "type": "string",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "nb_conarea": {
                      "type": "integer",
                      "format": "int32",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "conarea_name": {
                      "type": "string",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "nb_tpo": {
                      "type": "integer",
                      "format": "int32",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "tpo_name": {
                      "type": "string",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "is_listed_building": {
                      "type": "string",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "is_floodzone_2": {
                      "type": "string",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "is_floodzone_3a": {
                      "type": "string",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "is_floodzone_3b": {
                      "type": "string",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "geom": {
                      "type": "string",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "application_id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
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
                "schema": {
                  "$ref": "#/components/schemas/SiteConstraints"
                }
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
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
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
                  "items": {
                    "$ref": "#/components/schemas/WorksLocation"
                  }
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
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.212831+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.212981+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
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
                "schema": {
                  "$ref": "#/components/schemas/WorksLocation"
                }
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
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "The requested WorksLocation",
                "schema": {
                  "$ref": "#/components/schemas/WorksLocation"
                }
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
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.222315+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.222449+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
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
                "schema": {
                  "$ref": "#/components/schemas/WorksLocation"
                }
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
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
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
                  "items": {
                    "$ref": "#/components/schemas/BasementWorksType"
                  }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.231268+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.231399+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
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
                "schema": {
                  "$ref": "#/components/schemas/BasementWorksType"
                }
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
        "/api/v1/roof-works-types": {
          "get": {
            "summary": "Get all RoofWorksTypes from the DB",
            "tags": [
              "RoofWorksType"
            ],
            "parameters": [
              {
                "in": "query",
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
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
                  "items": {
                    "$ref": "#/components/schemas/RoofWorksType"
                  }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.240790+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.240922+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
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
                "schema": {
                  "$ref": "#/components/schemas/RoofWorksType"
                }
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
        "/api/v1/border-works-types": {
          "get": {
            "summary": "Get all BorderWorksTypes from the DB",
            "tags": [
              "BorderWorksType"
            ],
            "parameters": [
              {
                "in": "query",
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
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
                  "items": {
                    "$ref": "#/components/schemas/BorderWorksType"
                  }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.269847+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.270025+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
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
                "schema": {
                  "$ref": "#/components/schemas/BorderWorksType"
                }
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
        "/api/v1/access-works-scopes": {
          "get": {
            "summary": "Get all AccessWorksScopes from the DB",
            "tags": [
              "AccessWorksScope"
            ],
            "parameters": [
              {
                "in": "query",
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
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
                  "items": {
                    "$ref": "#/components/schemas/AccessWorksScope"
                  }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.282402+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.282564+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
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
                "schema": {
                  "$ref": "#/components/schemas/AccessWorksScope"
                }
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
        "/api/v1/access-works-types": {
          "get": {
            "summary": "Get all AccessWorksTypes from the DB",
            "tags": [
              "AccessWorksType"
            ],
            "parameters": [
              {
                "in": "query",
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
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
                  "items": {
                    "$ref": "#/components/schemas/AccessWorksType"
                  }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.293974+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.294173+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
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
                "schema": {
                  "$ref": "#/components/schemas/AccessWorksType"
                }
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
        "/api/v1/parking-works-scopes": {
          "get": {
            "summary": "Get all ParkingWorksScopes from the DB",
            "tags": [
              "ParkingWorksScope"
            ],
            "parameters": [
              {
                "in": "query",
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
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
                  "items": {
                    "$ref": "#/components/schemas/ParkingWorksScope"
                  }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.305369+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.305533+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
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
                "schema": {
                  "$ref": "#/components/schemas/ParkingWorksScope"
                }
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
        "/api/v1/equipment-works-types": {
          "get": {
            "summary": "Get all EquipmentWorksTypes from the DB",
            "tags": [
              "EquipmentWorksType"
            ],
            "parameters": [
              {
                "in": "query",
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
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
                  "items": {
                    "$ref": "#/components/schemas/EquipmentWorksType"
                  }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.316209+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.316371+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
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
                "schema": {
                  "$ref": "#/components/schemas/EquipmentWorksType"
                }
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
        "/api/v1/equipment-works-conservation-types": {
          "get": {
            "summary": "Get all EquipmentWorksConservationTypes from the DB",
            "tags": [
              "EquipmentWorksConservationType"
            ],
            "parameters": [
              {
                "in": "query",
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
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
                  "items": {
                    "$ref": "#/components/schemas/EquipmentWorksConservationType"
                  }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.326745+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.326901+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
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
                "schema": {
                  "$ref": "#/components/schemas/EquipmentWorksConservationType"
                }
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
        "/api/v1/gate-fences-walls-types": {
          "get": {
            "summary": "Get all GatesFencesWallsType from the DB",
            "tags": [
              "GatesFencesWallsType"
            ],
            "parameters": [
              {
                "in": "query",
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All GatesFencesWallsTypes",
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/GatesFencesWallsType"
                  }
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add new GatesFencesWallsType to the database",
            "tags": [
              "GatesFencesWallsType"
            ],
            "parameters": [
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.336531+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.336648+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "nullable": true,
                      "maxLength": 255
                    }
                  }
                }
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
                "description": "GatesFencesWallsType created successfully",
                "schema": {
                  "$ref": "#/components/schemas/GatesFencesWallsType"
                }
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
        "/api/v1/materials/options/roof": {
          "get": {
            "summary": "Get all MaterialOptionRoofs from the DB",
            "tags": [
              "MaterialOptionRoof"
            ],
            "parameters": [
              {
                "in": "query",
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All MaterialOptionRoofs",
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/MaterialOptionRoof"
                  }
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add new MaterialOptionRoof to the database",
            "tags": [
              "MaterialOptionRoof"
            ],
            "parameters": [
              {
                "in": "path",
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.356533+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.356735+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "maxLength": 100
                    }
                  },
                  "required": [
                    "name"
                  ]
                }
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
                "schema": {
                  "$ref": "#/components/schemas/MaterialOptionRoof"
                }
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
            "summary": "Get all MaterialOptionWalls from the DB",
            "tags": [
              "MaterialOptionWall"
            ],
            "parameters": [
              {
                "in": "query",
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All MaterialOptionWalls",
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/MaterialOptionWall"
                  }
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add new MaterialOptionWall to the database",
            "tags": [
              "MaterialOptionWall"
            ],
            "parameters": [
              {
                "in": "path",
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.368319+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.368485+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "maxLength": 100
                    }
                  },
                  "required": [
                    "name"
                  ]
                }
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
                "schema": {
                  "$ref": "#/components/schemas/MaterialOptionWall"
                }
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
            "summary": "Get all MaterialOptionDoors from the DB",
            "tags": [
              "MaterialOptionDoor"
            ],
            "parameters": [
              {
                "in": "query",
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All MaterialOptionDoors",
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/MaterialOptionDoor"
                  }
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add new MaterialOptionDoor to the database",
            "tags": [
              "MaterialOptionDoor"
            ],
            "parameters": [
              {
                "in": "path",
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.379902+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.380070+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "maxLength": 100
                    }
                  },
                  "required": [
                    "name"
                  ]
                }
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
                "schema": {
                  "$ref": "#/components/schemas/MaterialOptionDoor"
                }
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
            "summary": "Get all MaterialOptionWindows from the DB",
            "tags": [
              "MaterialOptionWindow"
            ],
            "parameters": [
              {
                "in": "query",
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All MaterialOptionWindows",
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/MaterialOptionWindow"
                  }
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add new MaterialOptionWindow to the database",
            "tags": [
              "MaterialOptionWindow"
            ],
            "parameters": [
              {
                "in": "path",
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.391992+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.392173+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "maxLength": 100
                    }
                  },
                  "required": [
                    "name"
                  ]
                }
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
                "schema": {
                  "$ref": "#/components/schemas/MaterialOptionWindow"
                }
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
        "/api/v1/materials/roof": {
          "get": {
            "summary": "Get all MaterialRoofs from the DB",
            "tags": [
              "MaterialRoof"
            ],
            "parameters": [
              {
                "in": "query",
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All MaterialRoofs",
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/MaterialRoof"
                  }
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add new MaterialRoof to the database",
            "tags": [
              "MaterialRoof"
            ],
            "parameters": [
              {
                "in": "path",
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.403006+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.403159+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "colour_and_type": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "colour_and_type"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "material_id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "material_id"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "material": {
                      "nullable": true,
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/MaterialOptionRoof"
                        }
                      ]
                    }
                  }
                }
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
                "description": "MaterialRoof created successfully",
                "schema": {
                  "$ref": "#/components/schemas/MaterialRoof"
                }
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
        "/api/v1/materials/roof/{id}": {
          "get": {
            "summary": "Get one MaterialRoof from the DB",
            "tags": [
              "MaterialRoof"
            ],
            "parameters": [
              {
                "in": "path",
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "The requested MaterialRoof",
                "schema": {
                  "$ref": "#/components/schemas/MaterialRoof"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update an MaterialRoof in the database",
            "tags": [
              "MaterialRoof"
            ],
            "parameters": [
              {
                "in": "path",
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.413736+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.413890+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "colour_and_type": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "colour_and_type"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "material_id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "material_id"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "material": {
                      "nullable": true,
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/MaterialOptionRoof"
                        }
                      ]
                    }
                  }
                }
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
                "description": "Returns updated MaterialRoof",
                "schema": {
                  "$ref": "#/components/schemas/MaterialRoof"
                }
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
        "/api/v1/materials/wall": {
          "get": {
            "summary": "Get all MaterialWalls from the DB",
            "tags": [
              "MaterialWall"
            ],
            "parameters": [
              {
                "in": "query",
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All MaterialWalls",
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/MaterialWall"
                  }
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add new MaterialWall to the database",
            "tags": [
              "MaterialWall"
            ],
            "parameters": [
              {
                "in": "path",
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.423695+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.423828+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "colour_and_type": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "colour_and_type"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "material_id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "material_id"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "material": {
                      "nullable": true,
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/MaterialOptionWall"
                        }
                      ]
                    }
                  }
                }
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
                "description": "MaterialWall created successfully",
                "schema": {
                  "$ref": "#/components/schemas/MaterialWall"
                }
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
        "/api/v1/materials/wall/{id}": {
          "get": {
            "summary": "Get one MaterialWall from the DB",
            "tags": [
              "MaterialWall"
            ],
            "parameters": [
              {
                "in": "path",
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "The requested MaterialWall",
                "schema": {
                  "$ref": "#/components/schemas/MaterialWall"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update an MaterialWall in the database",
            "tags": [
              "MaterialWall"
            ],
            "parameters": [
              {
                "in": "path",
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.433246+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.433377+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "colour_and_type": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "colour_and_type"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "material_id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "material_id"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "material": {
                      "nullable": true,
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/MaterialOptionWall"
                        }
                      ]
                    }
                  }
                }
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
                "description": "Returns updated MaterialWall",
                "schema": {
                  "$ref": "#/components/schemas/MaterialWall"
                }
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
        "/api/v1/materials/wind": {
          "get": {
            "summary": "Get all MaterialWindows from the DB",
            "tags": [
              "MaterialWindow"
            ],
            "parameters": [
              {
                "in": "query",
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All MaterialWindows",
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/MaterialWindow"
                  }
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add new MaterialWindow to the database",
            "tags": [
              "MaterialWindow"
            ],
            "parameters": [
              {
                "in": "path",
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.450700+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.450988+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "colour_and_type": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "colour_and_type"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "material_id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "material_id"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "material": {
                      "nullable": true,
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/MaterialOptionWindow"
                        }
                      ]
                    }
                  }
                }
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
                "description": "MaterialWindow created successfully",
                "schema": {
                  "$ref": "#/components/schemas/MaterialWindow"
                }
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
        "/api/v1/materials/wind/{id}": {
          "get": {
            "summary": "Get one MaterialWindow from the DB",
            "tags": [
              "MaterialWindow"
            ],
            "parameters": [
              {
                "in": "path",
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "The requested MaterialWindow",
                "schema": {
                  "$ref": "#/components/schemas/MaterialWindow"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update an MaterialWindow in the database",
            "tags": [
              "MaterialWindow"
            ],
            "parameters": [
              {
                "in": "path",
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.471377+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.471550+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "colour_and_type": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "colour_and_type"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "material_id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "material_id"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "material": {
                      "nullable": true,
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/MaterialOptionWindow"
                        }
                      ]
                    }
                  }
                }
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
                "description": "Returns updated MaterialWindow",
                "schema": {
                  "$ref": "#/components/schemas/MaterialWindow"
                }
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
        "/api/v1/materials/door": {
          "get": {
            "summary": "Get all MaterialDoors from the DB",
            "tags": [
              "MaterialDoor"
            ],
            "parameters": [
              {
                "in": "query",
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "All MaterialDoors",
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/MaterialDoor"
                  }
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add new MaterialDoor to the database",
            "tags": [
              "MaterialDoor"
            ],
            "parameters": [
              {
                "in": "path",
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.484668+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.484838+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "colour_and_type": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "colour_and_type"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "material_id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "material_id"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "material": {
                      "nullable": true,
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/MaterialOptionDoor"
                        }
                      ]
                    }
                  }
                }
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
                "description": "MaterialDoor created successfully",
                "schema": {
                  "$ref": "#/components/schemas/MaterialDoor"
                }
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
        "/api/v1/materials/door/{id}": {
          "get": {
            "summary": "Get one MaterialDoor from the DB",
            "tags": [
              "MaterialDoor"
            ],
            "parameters": [
              {
                "in": "path",
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "The requested MaterialDoor",
                "schema": {
                  "$ref": "#/components/schemas/MaterialDoor"
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {
            "summary": "Update an MaterialDoor in the database",
            "tags": [
              "MaterialDoor"
            ],
            "parameters": [
              {
                "in": "path",
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.500368+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.501161+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "colour_and_type": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "colour_and_type"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "material_id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "material_id"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "material": {
                      "nullable": true,
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/MaterialOptionDoor"
                        }
                      ]
                    }
                  }
                }
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
                "description": "Returns updated MaterialDoor",
                "schema": {
                  "$ref": "#/components/schemas/MaterialDoor"
                }
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
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "The requested AreaUnit",
                "schema": {
                  "$ref": "#/components/schemas/AreaUnit"
                }
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
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.525519+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.525684+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "maxLength": 100
                    }
                  },
                  "required": [
                    "name"
                  ]
                }
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
                "schema": {
                  "$ref": "#/components/schemas/AreaUnit"
                }
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
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.526402+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.526551+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "maxLength": 100
                    }
                  },
                  "required": [
                    "name"
                  ]
                }
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
                "schema": {
                  "$ref": "#/components/schemas/AreaUnit"
                }
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
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
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
                  "items": {
                    "$ref": "#/components/schemas/AreaUnit"
                  }
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
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
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
                  "items": {
                    "$ref": "#/components/schemas/LinearUnit"
                  }
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
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "One LinearUnit",
                "schema": {
                  "$ref": "#/components/schemas/LinearUnit"
                }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.567287+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.567484+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "maxLength": 100
                    }
                  },
                  "required": [
                    "name"
                  ]
                }
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
                "schema": {
                  "$ref": "#/components/schemas/LinearUnit"
                }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.568181+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.568311+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "maxLength": 100
                    }
                  },
                  "required": [
                    "name"
                  ]
                }
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
                "schema": {
                  "$ref": "#/components/schemas/LinearUnit"
                }
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
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
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
                  "items": {
                    "$ref": "#/components/schemas/User"
                  }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.584374+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.584532+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "email": {
                      "type": "string",
                      "maxLength": 200
                    }
                  },
                  "required": [
                    "email"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "password": {
                      "type": "string",
                      "maxLength": 100
                    }
                  },
                  "required": [
                    "password"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "profile_id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "profile_id"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "role_id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "role_id"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "role": {
                      "nullable": true,
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/Role"
                        }
                      ]
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "profile": {
                      "nullable": true,
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/UserProfile"
                        }
                      ]
                    }
                  }
                }
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
                "schema": {
                  "$ref": "#/components/schemas/User"
                }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.585954+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.586099+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "email": {
                      "type": "string",
                      "maxLength": 200
                    }
                  },
                  "required": [
                    "email"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "password": {
                      "type": "string",
                      "maxLength": 100
                    }
                  },
                  "required": [
                    "password"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "profile_id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "profile_id"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "role_id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "role_id"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "role": {
                      "nullable": true,
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/Role"
                        }
                      ]
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "profile": {
                      "nullable": true,
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/UserProfile"
                        }
                      ]
                    }
                  }
                }
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
                "schema": {
                  "$ref": "#/components/schemas/User"
                }
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
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
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
                  "items": {
                    "$ref": "#/components/schemas/Agent"
                  }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.601322+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.601468+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name_id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "company_name_id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "address_id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "telephone_number_ids": {
                      "type": "array",
                      "nullable": true,
                      "items": {
                        "type": "string",
                        "format": "uuid",
                        "nullable": true
                      }
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "email_addresses_ids": {
                      "type": "array",
                      "nullable": true,
                      "items": {
                        "type": "string",
                        "format": "uuid",
                        "nullable": true
                      }
                    }
                  }
                }
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
                "schema": {
                  "$ref": "#/components/schemas/Agent"
                }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.602330+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.602468+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name_id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "company_name_id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "address_id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "telephone_number_ids": {
                      "type": "array",
                      "nullable": true,
                      "items": {
                        "type": "string",
                        "format": "uuid",
                        "nullable": true
                      }
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "email_addresses_ids": {
                      "type": "array",
                      "nullable": true,
                      "items": {
                        "type": "string",
                        "format": "uuid",
                        "nullable": true
                      }
                    }
                  }
                }
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
                "schema": {
                  "$ref": "#/components/schemas/Agent"
                }
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
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
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
                  "items": {
                    "$ref": "#/components/schemas/DocumentSize"
                  }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.617680+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.617827+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "maxLength": 20
                    }
                  },
                  "required": [
                    "name"
                  ]
                }
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
                "schema": {
                  "$ref": "#/components/schemas/DocumentSize"
                }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.618393+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.618533+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "maxLength": 20
                    }
                  },
                  "required": [
                    "name"
                  ]
                }
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
                "schema": {
                  "$ref": "#/components/schemas/DocumentSize"
                }
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
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "email": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "email"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "password": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "password"
                  ]
                }
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
        "/api/v1/applications": {
          "get": {
            "summary": "Get all Applications from the DB",
            "tags": [
              "Application"
            ],
            "parameters": [
              {
                "in": "query",
                "name": "page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "query",
                "name": "per_page",
                "required": false,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
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
                  "items": {
                    "$ref": "#/components/schemas/Application"
                  }
                }
              },
              "401": {
                "description": "Unauthorized"
              }
            }
          },
          "patch": {},
          "post": {
            "summary": "Add new Application to the database",
            "tags": [
              "Application"
            ],
            "parameters": [
              {
                "in": "path",
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.633556+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.633687+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "works_started": {
                      "type": "boolean",
                      "default": false,
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "date_works_started": {
                      "type": "string",
                      "format": "date",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "works_completed": {
                      "type": "boolean",
                      "default": false,
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "date_works_completed": {
                      "type": "string",
                      "format": "date",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "works_description": {
                      "type": "string",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "owner_id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "owner_id"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "owner": {
                      "nullable": true,
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/User"
                        }
                      ]
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "site_address": {
                      "nullable": true,
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/SiteAddress"
                        }
                      ]
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "site_constraints": {
                      "nullable": true,
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/SiteConstraints"
                        }
                      ]
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "proposal_extension": {
                      "nullable": true,
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/ProposalExtension"
                        }
                      ]
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "proposal_equipment": {
                      "nullable": true,
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/ProposalEquipment"
                        }
                      ]
                    }
                  }
                }
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
                "schema": {
                  "$ref": "#/components/schemas/Application"
                }
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
        "/api/v1/applications/{id}": {
          "get": {
            "summary": "Get one Application from the DB",
            "tags": [
              "Application"
            ],
            "parameters": [
              {
                "in": "path",
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              }
            ],
            "produces": [
              "application/json"
            ],
            "responses": {
              "200": {
                "description": "The requested Application",
                "schema": {
                  "$ref": "#/components/schemas/Application"
                }
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
                "name": "id",
                "required": true,
                "schema": {
                  "type": "string",
                  "nullable": true
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "format": "uuid",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "created_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.655771+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "updated_at": {
                      "type": "string",
                      "format": "date-time",
                      "default": "2019-07-04T09:16:09.656146+00:00",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "works_started": {
                      "type": "boolean",
                      "default": false,
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "date_works_started": {
                      "type": "string",
                      "format": "date",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "works_completed": {
                      "type": "boolean",
                      "default": false,
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "date_works_completed": {
                      "type": "string",
                      "format": "date",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "works_description": {
                      "type": "string",
                      "nullable": true
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "owner_id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "owner_id"
                  ]
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "owner": {
                      "nullable": true,
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/User"
                        }
                      ]
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "site_address": {
                      "nullable": true,
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/SiteAddress"
                        }
                      ]
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "site_constraints": {
                      "nullable": true,
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/SiteConstraints"
                        }
                      ]
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "proposal_extension": {
                      "nullable": true,
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/ProposalExtension"
                        }
                      ]
                    }
                  }
                }
              },
              {
                "in": "body",
                "name": "body",
                "required": false,
                "schema": {
                  "type": "object",
                  "properties": {
                    "proposal_equipment": {
                      "nullable": true,
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/ProposalEquipment"
                        }
                      ]
                    }
                  }
                }
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
                "schema": {
                  "$ref": "#/components/schemas/Application"
                }
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
        }
      },
      "info": {
        "title": "Submit my Planning Application",
        "version": "1.0.0"
      },
      "openapi": "3.0",
      "components": {
        "schemas": {
          "SiteArea": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.017507+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.017677+00:00",
                "nullable": true
              },
              "area": {
                "type": "number",
                "format": "float"
              },
              "unit": {
                "type": "string",
                "format": "uuid"
              }
            },
            "required": [
              "area",
              "unit"
            ]
          },
          "SiteConstraints": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.018242+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.018339+00:00",
                "nullable": true
              },
              "has_boundry": {
                "type": "string",
                "nullable": true
              },
              "nb_a4d": {
                "type": "integer",
                "format": "int32",
                "nullable": true
              },
              "a4d_name": {
                "type": "string",
                "nullable": true
              },
              "nb_conarea": {
                "type": "integer",
                "format": "int32",
                "nullable": true
              },
              "conarea_name": {
                "type": "string",
                "nullable": true
              },
              "nb_tpo": {
                "type": "integer",
                "format": "int32",
                "nullable": true
              },
              "tpo_name": {
                "type": "string",
                "nullable": true
              },
              "is_listed_building": {
                "type": "string",
                "nullable": true
              },
              "is_floodzone_2": {
                "type": "string",
                "nullable": true
              },
              "is_floodzone_3a": {
                "type": "string",
                "nullable": true
              },
              "is_floodzone_3b": {
                "type": "string",
                "nullable": true
              },
              "geom": {
                "type": "string",
                "nullable": true
              },
              "application_id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              }
            }
          },
          "AreaUnit": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.018930+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.019030+00:00",
                "nullable": true
              },
              "name": {
                "type": "string",
                "maxLength": 100
              }
            },
            "required": [
              "name"
            ]
          },
          "LinearUnit": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.019357+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.019472+00:00",
                "nullable": true
              },
              "name": {
                "type": "string",
                "maxLength": 100
              }
            },
            "required": [
              "name"
            ]
          },
          "Role": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.019842+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.019957+00:00",
                "nullable": true
              },
              "name": {
                "type": "string",
                "maxLength": 100
              }
            },
            "required": [
              "name"
            ]
          },
          "PersonName": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.020319+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.020437+00:00",
                "nullable": true
              },
              "title": {
                "type": "string",
                "maxLength": 100
              },
              "given_name": {
                "type": "string",
                "maxLength": 255
              },
              "family_name": {
                "type": "string",
                "maxLength": 255
              }
            },
            "required": [
              "family_name",
              "given_name",
              "title"
            ]
          },
          "ContactMethod": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.020914+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.021034+00:00",
                "nullable": true
              },
              "name": {
                "type": "string",
                "maxLength": 100
              }
            },
            "required": [
              "name"
            ]
          },
          "Email": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.021404+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.021526+00:00",
                "nullable": true
              },
              "email_address": {
                "type": "string",
                "maxLength": 255
              },
              "verified": {
                "type": "boolean",
                "default": false,
                "nullable": true
              }
            },
            "required": [
              "email_address"
            ]
          },
          "UserProfile": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.022310+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.022609+00:00",
                "nullable": true
              },
              "name": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/PersonName"
                  }
                ]
              },
              "preferred_contact_method": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/ContactMethod"
                  }
                ]
              },
              "email_addresses": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/Email"
                    }
                  ]
                }
              },
              "primary_email_id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "primary_phone_id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              }
            }
          },
          "TelephoneNumber": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.025814+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.026082+00:00",
                "nullable": true
              },
              "tel_number": {
                "type": "string",
                "maxLength": 100
              },
              "tel_type_id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              }
            },
            "required": [
              "tel_number"
            ]
          },
          "TelephoneNumberType": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.026810+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.026962+00:00",
                "nullable": true
              },
              "name": {
                "type": "string",
                "maxLength": 100
              }
            },
            "required": [
              "name"
            ]
          },
          "Applicant": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.027527+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.027668+00:00",
                "nullable": true
              },
              "name_id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "company_name_id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "address_id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "telephone_number_ids": {
                "type": "array",
                "nullable": true,
                "items": {
                  "type": "string",
                  "format": "uuid",
                  "nullable": true
                }
              },
              "email_addresses_ids": {
                "type": "array",
                "nullable": true,
                "items": {
                  "type": "string",
                  "format": "uuid",
                  "nullable": true
                }
              }
            }
          },
          "Agent": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.028363+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.028522+00:00",
                "nullable": true
              },
              "name_id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "company_name_id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "address_id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "telephone_number_ids": {
                "type": "array",
                "nullable": true,
                "items": {
                  "type": "string",
                  "format": "uuid",
                  "nullable": true
                }
              },
              "email_addresses_ids": {
                "type": "array",
                "nullable": true,
                "items": {
                  "type": "string",
                  "format": "uuid",
                  "nullable": true
                }
              }
            }
          },
          "User": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.029231+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.029382+00:00",
                "nullable": true
              },
              "email": {
                "type": "string",
                "maxLength": 200
              },
              "password": {
                "type": "string",
                "maxLength": 100
              },
              "profile_id": {
                "type": "string"
              },
              "role_id": {
                "type": "string"
              },
              "role": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/Role"
                  }
                ]
              },
              "profile": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/UserProfile"
                  }
                ]
              }
            },
            "required": [
              "email",
              "password",
              "profile_id",
              "role_id"
            ]
          },
          "WorksLocation": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.030494+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.030640+00:00",
                "nullable": true
              },
              "name": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              }
            }
          },
          "BasementWorksType": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.031190+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.031329+00:00",
                "nullable": true
              },
              "name": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              }
            }
          },
          "RoofWorksType": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.031754+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.031895+00:00",
                "nullable": true
              },
              "name": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              }
            }
          },
          "BorderWorksType": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.032311+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.032450+00:00",
                "nullable": true
              },
              "name": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              }
            }
          },
          "AccessWorksScope": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.032865+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.033004+00:00",
                "nullable": true
              },
              "name": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              }
            }
          },
          "AccessWorksType": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.033416+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.033555+00:00",
                "nullable": true
              },
              "name": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              }
            }
          },
          "ParkingWorksScope": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.034085+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.034238+00:00",
                "nullable": true
              },
              "name": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              }
            }
          },
          "EquipmentWorksType": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.034693+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.034834+00:00",
                "nullable": true
              },
              "name": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              }
            }
          },
          "EquipmentWorksConservationType": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.035259+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.035399+00:00",
                "nullable": true
              },
              "name": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              }
            }
          },
          "GatesFencesWallsType": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.035816+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.035955+00:00",
                "nullable": true
              },
              "name": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              }
            }
          },
          "WorkExtensionOption": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.036399+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.036537+00:00",
                "nullable": true
              },
              "works_location_ids": {
                "type": "string",
                "default": []
              },
              "works_locations": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/WorksLocation"
                    }
                  ]
                }
              }
            },
            "required": [
              "works_location_ids"
            ]
          },
          "ExtensionOriginalHouseSingleStoreyExtension": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.037598+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.037747+00:00",
                "nullable": true
              },
              "works_location_ids": {
                "type": "string",
                "default": []
              },
              "works_locations": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/WorksLocation"
                    }
                  ]
                }
              }
            },
            "required": [
              "works_location_ids"
            ]
          },
          "ExtensionOriginalHouseTwoStoreyExtension": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.038458+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.038600+00:00",
                "nullable": true
              },
              "works_location_ids": {
                "type": "string",
                "default": []
              },
              "works_locations": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/WorksLocation"
                    }
                  ]
                }
              }
            },
            "required": [
              "works_location_ids"
            ]
          },
          "ExtensionOriginalHousePartSinglePartTwoStoreyExtension": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.039280+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.039421+00:00",
                "nullable": true
              },
              "works_location_ids": {
                "type": "string",
                "default": []
              },
              "works_locations": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/WorksLocation"
                    }
                  ]
                }
              }
            },
            "required": [
              "works_location_ids"
            ]
          },
          "ExtensionOriginalHouseBasement": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.040134+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.040306+00:00",
                "nullable": true
              },
              "works_location_ids": {
                "type": "string",
                "default": []
              },
              "works_locations": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/WorksLocation"
                    }
                  ]
                }
              },
              "works_type_ids": {
                "type": "string",
                "default": []
              },
              "works_types": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/BasementWorksType"
                    }
                  ]
                }
              }
            },
            "required": [
              "works_location_ids",
              "works_type_ids"
            ]
          },
          "ExtensionOriginalHouseRoof": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.049846+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.050405+00:00",
                "nullable": true
              },
              "works_location_ids": {
                "type": "string",
                "default": []
              },
              "works_locations": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/WorksLocation"
                    }
                  ]
                }
              },
              "works_type_ids": {
                "type": "string",
                "default": []
              },
              "works_types": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/RoofWorksType"
                    }
                  ]
                }
              }
            },
            "required": [
              "works_location_ids",
              "works_type_ids"
            ]
          },
          "ExtensionOutbuilding": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.054391+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.054776+00:00",
                "nullable": true
              },
              "works_location_ids": {
                "type": "string",
                "default": []
              },
              "works_locations": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/WorksLocation"
                    }
                  ]
                }
              }
            },
            "required": [
              "works_location_ids"
            ]
          },
          "ExtensionOriginalHousePorch": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.055617+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.055778+00:00",
                "nullable": true
              },
              "works_location_ids": {
                "type": "string",
                "default": []
              },
              "works_locations": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/WorksLocation"
                    }
                  ]
                }
              }
            },
            "required": [
              "works_location_ids"
            ]
          },
          "ExtensionOriginalHouseBalconyTerrace": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.056566+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.056715+00:00",
                "nullable": true
              },
              "works_location_ids": {
                "type": "string",
                "default": []
              },
              "works_locations": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/WorksLocation"
                    }
                  ]
                }
              }
            },
            "required": [
              "works_location_ids"
            ]
          },
          "ExtensionOriginalHouseStaircase": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.057649+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.057795+00:00",
                "nullable": true
              },
              "works_location_ids": {
                "type": "string",
                "default": []
              },
              "works_locations": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/WorksLocation"
                    }
                  ]
                }
              }
            },
            "required": [
              "works_location_ids"
            ]
          },
          "ExtensionOriginalHouseWindowsDoors": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.058497+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.058639+00:00",
                "nullable": true
              },
              "works_location_ids": {
                "type": "string",
                "default": []
              },
              "works_locations": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/WorksLocation"
                    }
                  ]
                }
              }
            },
            "required": [
              "works_location_ids"
            ]
          },
          "ExtensionOriginalHouseCladding": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.059294+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.059493+00:00",
                "nullable": true
              },
              "works_location_ids": {
                "type": "string",
                "default": []
              },
              "works_locations": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/WorksLocation"
                    }
                  ]
                }
              }
            },
            "required": [
              "works_location_ids"
            ]
          },
          "ExtensionBoundaraiesGatesFencesWalls": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.060267+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.060410+00:00",
                "nullable": true
              },
              "works_location_ids": {
                "type": "string",
                "default": []
              },
              "works_locations": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/WorksLocation"
                    }
                  ]
                }
              },
              "works_type_ids": {
                "type": "string",
                "default": []
              },
              "works_types": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/GatesFencesWallsType"
                    }
                  ]
                }
              }
            },
            "required": [
              "works_location_ids",
              "works_type_ids"
            ]
          },
          "Work": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.061504+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.061648+00:00",
                "nullable": true
              }
            }
          },
          "WorkExtensionOriginalHouse": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.062242+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.062384+00:00",
                "nullable": true
              },
              "single_storey_extension": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/ExtensionOriginalHouseSingleStoreyExtension"
                  }
                ]
              },
              "two_storey_extension": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/ExtensionOriginalHouseTwoStoreyExtension"
                  }
                ]
              },
              "part_single_part_two_storey_extension": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/ExtensionOriginalHousePartSinglePartTwoStoreyExtension"
                  }
                ]
              },
              "basement": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/ExtensionOriginalHouseBasement"
                  }
                ]
              },
              "roof": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/ExtensionOriginalHouseRoof"
                  }
                ]
              },
              "porch": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/ExtensionOriginalHousePorch"
                  }
                ]
              },
              "balcony_terrace": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/ExtensionOriginalHouseBalconyTerrace"
                  }
                ]
              },
              "staircase": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/ExtensionOriginalHouseStaircase"
                  }
                ]
              },
              "windows_doors": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/ExtensionOriginalHouseWindowsDoors"
                  }
                ]
              },
              "cladding": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/ExtensionOriginalHouseCladding"
                  }
                ]
              }
            }
          },
          "WorkExtensionIncidentalBuildings": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.065544+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.065690+00:00",
                "nullable": true
              },
              "removal_or_demolition": {
                "type": "boolean",
                "default": false,
                "nullable": true
              },
              "details": {
                "type": "string",
                "nullable": true
              },
              "outbuilding": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/ExtensionOutbuilding"
                  }
                ]
              }
            }
          },
          "WorkExtensionBoundaries": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.066407+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.066549+00:00",
                "nullable": true
              },
              "gates_fences_walls": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/ExtensionBoundaraiesGatesFencesWalls"
                  }
                ]
              },
              "border_works_type_ids": {
                "type": "string",
                "default": []
              },
              "border_works_types": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/BorderWorksType"
                    }
                  ]
                }
              }
            },
            "required": [
              "border_works_type_ids"
            ]
          },
          "WorkExtensionMeansOfAccess": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.067533+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.067745+00:00",
                "nullable": true
              },
              "access_works_scope_id": {
                "type": "string"
              },
              "access_works_scope": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/BorderWorksType"
                  }
                ]
              },
              "access_works_sub_type_ids": {
                "type": "string",
                "default": []
              },
              "access_works_sub_types": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/AccessWorksType"
                    }
                  ]
                }
              }
            },
            "required": [
              "access_works_scope_id",
              "access_works_sub_type_ids"
            ]
          },
          "WorkExtensionParking": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.068821+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.068964+00:00",
                "nullable": true
              },
              "parking_works_scope_id": {
                "type": "string"
              },
              "parking_works_scope": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/ParkingWorksScope"
                  }
                ]
              },
              "current_car_parking_spaces": {
                "type": "integer",
                "format": "int32",
                "default": 0,
                "nullable": true
              },
              "planned_car_parking_spaces": {
                "type": "integer",
                "format": "int32",
                "default": 0,
                "nullable": true
              },
              "current_bike_parking_spaces": {
                "type": "integer",
                "format": "int32",
                "default": 0,
                "nullable": true
              },
              "planned_bike_parking_spaces": {
                "type": "integer",
                "format": "int32",
                "default": 0,
                "nullable": true
              },
              "new_ev_charging_points": {
                "type": "integer",
                "format": "int32",
                "default": 0,
                "nullable": true
              }
            },
            "required": [
              "parking_works_scope_id"
            ]
          },
          "WorkEquipmentLocation": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.069773+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.069914+00:00",
                "nullable": true
              },
              "location_ids": {
                "type": "string",
                "default": []
              },
              "locations": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/WorksLocation"
                    }
                  ]
                }
              },
              "equipment_type_id": {
                "type": "string"
              },
              "equipment_type": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/EquipmentWorksType"
                  }
                ]
              }
            },
            "required": [
              "equipment_type_id",
              "location_ids"
            ]
          },
          "WorkEquipmentConservationLocation": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.070865+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.071007+00:00",
                "nullable": true
              },
              "location_id": {
                "type": "string"
              },
              "location": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/WorksLocation"
                  }
                ]
              },
              "equipment_type_id": {
                "type": "string"
              },
              "equipment_conservation_type": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/EquipmentWorksConservationType"
                  }
                ]
              }
            },
            "required": [
              "equipment_type_id",
              "location_id"
            ]
          },
          "WorkEquipment": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.072218+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.072366+00:00",
                "nullable": true
              },
              "equipment_type_ids": {
                "type": "string",
                "default": []
              },
              "equipment_types": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/EquipmentWorksType"
                    }
                  ]
                }
              },
              "equipment_conservation_type_ids": {
                "type": "string",
                "default": []
              },
              "equipment_conservation_types": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/EquipmentWorksConservationType"
                    }
                  ]
                }
              },
              "equipment_locations": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/WorkEquipmentLocation"
                    }
                  ]
                }
              },
              "equipment_conservation_locations": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/WorkEquipmentLocation"
                    }
                  ]
                }
              }
            },
            "required": [
              "equipment_conservation_type_ids",
              "equipment_type_ids"
            ]
          },
          "WorkTrees": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.073920+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.074043+00:00",
                "nullable": true
              },
              "inside_boundry": {
                "type": "boolean",
                "default": false,
                "nullable": true
              },
              "removed_or_pruned": {
                "type": "boolean",
                "default": false,
                "nullable": true
              },
              "outside_boundry": {
                "type": "boolean",
                "default": false,
                "nullable": true
              }
            }
          },
          "SiteAddress": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.076275+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.076419+00:00",
                "nullable": true
              },
              "number": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "property_name": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "address_line_1": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "address_line_2": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "address_line_3": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "town_city": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "postcode": {
                "type": "string",
                "nullable": true,
                "maxLength": 15
              },
              "easting": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "northing": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "ward": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "bplu": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "uprn": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "property_type": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "description": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "application_id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              }
            }
          },
          "MaterialOptionRoof": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.084724+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.084855+00:00",
                "nullable": true
              },
              "name": {
                "type": "string",
                "maxLength": 100
              }
            },
            "required": [
              "name"
            ]
          },
          "MaterialRoof": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.083998+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.084129+00:00",
                "nullable": true
              },
              "colour_and_type": {
                "type": "string"
              },
              "material_id": {
                "type": "string"
              },
              "material": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/MaterialOptionRoof"
                  }
                ]
              }
            },
            "required": [
              "colour_and_type",
              "material_id"
            ]
          },
          "MaterialProposalRoof": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.083215+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.083348+00:00",
                "nullable": true
              },
              "proposals": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/MaterialRoof"
                    }
                  ]
                }
              },
              "matches_existing": {
                "type": "boolean",
                "default": false,
                "nullable": true
              },
              "not_applicable": {
                "type": "boolean",
                "default": false,
                "nullable": true
              }
            }
          },
          "MaterialProposalWalls": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.085607+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.085739+00:00",
                "nullable": true
              },
              "proposals": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/MaterialRoof"
                    }
                  ]
                }
              },
              "matches_existing": {
                "type": "boolean",
                "default": false,
                "nullable": true
              },
              "not_applicable": {
                "type": "boolean",
                "default": false,
                "nullable": true
              }
            }
          },
          "MaterialProposalWindows": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.086678+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.086810+00:00",
                "nullable": true
              },
              "proposals": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/MaterialRoof"
                    }
                  ]
                }
              },
              "matches_existing": {
                "type": "boolean",
                "default": false,
                "nullable": true
              },
              "not_applicable": {
                "type": "boolean",
                "default": false,
                "nullable": true
              }
            }
          },
          "MaterialProposalDoors": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.087869+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.088009+00:00",
                "nullable": true
              },
              "proposals": {
                "type": "array",
                "nullable": true,
                "items": {
                  "nullable": true,
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/MaterialRoof"
                    }
                  ]
                }
              },
              "matches_existing": {
                "type": "boolean",
                "default": false,
                "nullable": true
              },
              "not_applicable": {
                "type": "boolean",
                "default": false,
                "nullable": true
              }
            }
          },
          "MaterialExtension": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.082347+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.082490+00:00",
                "nullable": true
              },
              "definitions_in_documents": {
                "type": "boolean",
                "default": false,
                "nullable": true
              },
              "definitions_in_form": {
                "type": "boolean",
                "default": false,
                "nullable": true
              },
              "definitions_to_follow": {
                "type": "boolean",
                "default": false,
                "nullable": true
              },
              "roof": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/MaterialProposalRoof"
                  }
                ]
              },
              "walls": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/MaterialProposalWalls"
                  }
                ]
              },
              "windows": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/MaterialProposalWindows"
                  }
                ]
              },
              "doors": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/MaterialProposalDoors"
                  }
                ]
              },
              "other": {
                "type": "array",
                "nullable": true,
                "items": {
                  "type": "string",
                  "nullable": true
                }
              }
            }
          },
          "ProposalExtension": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.078584+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.078776+00:00",
                "nullable": true
              },
              "application_id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "original_house": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/WorkExtensionOriginalHouse"
                  }
                ]
              },
              "incidental_buildings": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/WorkExtensionIncidentalBuildings"
                  }
                ]
              },
              "boundaries": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/WorkExtensionBoundaries"
                  }
                ]
              },
              "means_of_access": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/WorkExtensionMeansOfAccess"
                  }
                ]
              },
              "parking": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/WorkExtensionParking"
                  }
                ]
              },
              "trees": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/WorkTrees"
                  }
                ]
              },
              "materials": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/MaterialExtension"
                  }
                ]
              },
              "additional_floor_area": {
                "type": "number",
                "format": "float",
                "nullable": true
              },
              "additional_floor_area_units_id": {
                "type": "string"
              },
              "additional_floor_area_units": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/AreaUnit"
                  }
                ]
              },
              "new_single_bedrooms": {
                "type": "integer",
                "format": "int32",
                "nullable": true
              },
              "new_double_bedrooms": {
                "type": "integer",
                "format": "int32",
                "nullable": true
              },
              "owner_id": {
                "type": "string"
              },
              "owner": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/User"
                  }
                ]
              }
            },
            "required": [
              "additional_floor_area_units_id",
              "owner_id"
            ]
          },
          "ProposalEquipment": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.089765+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.089896+00:00",
                "nullable": true
              },
              "application_id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "equipment": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/WorkEquipment"
                  }
                ]
              },
              "owner_id": {
                "type": "string"
              },
              "owner": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/User"
                  }
                ]
              }
            },
            "required": [
              "owner_id"
            ]
          },
          "Application": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.074671+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.074825+00:00",
                "nullable": true
              },
              "works_started": {
                "type": "boolean",
                "default": false,
                "nullable": true
              },
              "date_works_started": {
                "type": "string",
                "format": "date",
                "nullable": true
              },
              "works_completed": {
                "type": "boolean",
                "default": false,
                "nullable": true
              },
              "date_works_completed": {
                "type": "string",
                "format": "date",
                "nullable": true
              },
              "works_description": {
                "type": "string",
                "nullable": true
              },
              "owner_id": {
                "type": "string"
              },
              "owner": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/User"
                  }
                ]
              },
              "site_address": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SiteAddress"
                  }
                ]
              },
              "site_constraints": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/SiteConstraints"
                  }
                ]
              },
              "proposal_extension": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/ProposalExtension"
                  }
                ]
              },
              "proposal_equipment": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/ProposalEquipment"
                  }
                ]
              }
            },
            "required": [
              "owner_id"
            ]
          },
          "Address": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.091025+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.091154+00:00",
                "nullable": true
              },
              "number": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "property_name": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "address_line_1": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "address_line_2": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "address_line_3": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "town_city": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "postcode": {
                "type": "string",
                "maxLength": 15
              }
            },
            "required": [
              "postcode"
            ]
          },
          "Article4Direction": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.091654+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.091781+00:00",
                "nullable": true
              },
              "name": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              }
            }
          },
          "BS7666Address": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.092244+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.092370+00:00",
                "nullable": true
              },
              "street_description": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "locality": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "town": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "post_town": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "postcode": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "unique_property_reference_number": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "paon": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "country": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              }
            }
          },
          "InternationalAddress": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.092997+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.093123+00:00",
                "nullable": true
              },
              "line1": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "country": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              },
              "international_postal_code": {
                "type": "string",
                "nullable": true,
                "maxLength": 255
              }
            }
          },
          "ExternalAddress": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.093539+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.093665+00:00",
                "nullable": true
              },
              "international_address_id": {
                "type": "string",
                "format": "uuid"
              }
            },
            "required": [
              "international_address_id"
            ]
          },
          "DocumentSize": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.094038+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.094163+00:00",
                "nullable": true
              },
              "name": {
                "type": "string",
                "maxLength": 20
              }
            },
            "required": [
              "name"
            ]
          },
          "MaterialOption": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.094537+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.094662+00:00",
                "nullable": true
              },
              "name": {
                "type": "string",
                "maxLength": 100
              }
            },
            "required": [
              "name"
            ]
          },
          "MaterialOptionWall": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.095047+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.095167+00:00",
                "nullable": true
              },
              "name": {
                "type": "string",
                "maxLength": 100
              }
            },
            "required": [
              "name"
            ]
          },
          "MaterialOptionWindow": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.095642+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.095772+00:00",
                "nullable": true
              },
              "name": {
                "type": "string",
                "maxLength": 100
              }
            },
            "required": [
              "name"
            ]
          },
          "MaterialOptionDoor": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.096167+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.096292+00:00",
                "nullable": true
              },
              "name": {
                "type": "string",
                "maxLength": 100
              }
            },
            "required": [
              "name"
            ]
          },
          "BaseExistingMaterial": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.096679+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.096803+00:00",
                "nullable": true
              },
              "name": {
                "type": "string"
              },
              "colour_and_type": {
                "type": "string"
              }
            },
            "required": [
              "colour_and_type",
              "name"
            ]
          },
          "BaseMaterial": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.097193+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.097318+00:00",
                "nullable": true
              },
              "colour_and_type": {
                "type": "string"
              }
            },
            "required": [
              "colour_and_type"
            ]
          },
          "MaterialWall": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.097730+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.097858+00:00",
                "nullable": true
              },
              "colour_and_type": {
                "type": "string"
              },
              "material_id": {
                "type": "string"
              },
              "material": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/MaterialOptionWall"
                  }
                ]
              }
            },
            "required": [
              "colour_and_type",
              "material_id"
            ]
          },
          "MaterialWindow": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.098480+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.098605+00:00",
                "nullable": true
              },
              "colour_and_type": {
                "type": "string"
              },
              "material_id": {
                "type": "string"
              },
              "material": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/MaterialOptionWindow"
                  }
                ]
              }
            },
            "required": [
              "colour_and_type",
              "material_id"
            ]
          },
          "MaterialDoor": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.099308+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.099677+00:00",
                "nullable": true
              },
              "colour_and_type": {
                "type": "string"
              },
              "material_id": {
                "type": "string"
              },
              "material": {
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/MaterialOptionDoor"
                  }
                ]
              }
            },
            "required": [
              "colour_and_type",
              "material_id"
            ]
          },
          "OtherMaterial": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.100669+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.100807+00:00",
                "nullable": true
              },
              "description": {
                "type": "string"
              }
            },
            "required": [
              "description"
            ]
          },
          "ExternalBuildingMaterial": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.101384+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.101518+00:00",
                "nullable": true
              },
              "element": {
                "type": "string"
              },
              "proposed_material": {
                "type": "string"
              },
              "colour_and_type": {
                "type": "string"
              }
            },
            "required": [
              "colour_and_type",
              "element",
              "proposed_material"
            ]
          },
          "WorksProposal": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              },
              "created_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.102332+00:00",
                "nullable": true
              },
              "updated_at": {
                "type": "string",
                "format": "date-time",
                "default": "2019-07-04T09:16:09.102532+00:00",
                "nullable": true
              },
              "application_id": {
                "type": "string",
                "format": "uuid",
                "nullable": true
              }
            }
          }
        }
      }
    }
