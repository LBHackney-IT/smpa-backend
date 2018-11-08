# Generated Schema

This is the generated OpenAPI schema doc. It's currently missing the details in the `components.schemas` section. This is a bug.

    {
      "openapi": "3.0.1",
      "info": {
        "title": "Submit my Planning Application",
        "description": "An API for managing planning applications.",
        "version": "0.0.1"
      },
      "paths": {
        "/_debugger": {
          "get": {
            "tags": [],
            "operationId": "debugger",
            "description": "",
            "parameters": [],
            "deprecated": false,
            "responses": {
              "200": {
                "description": "A successful response.",
                "content": {}
              }
            }
          }
        },
        "/_docs": {
          "get": {
            "tags": [],
            "operationId": "OpenAPIUIHandler",
            "description": "Renders the Swagger UI.",
            "parameters": [],
            "deprecated": false,
            "responses": {
              "200": {
                "description": null
              }
            }
          }
        },
        "/_schema": {
          "get": {
            "tags": [],
            "operationId": "OpenAPIHandler",
            "description": "Generates an OpenAPI v3 document.",
            "parameters": [],
            "deprecated": false,
            "responses": {
              "200": {
                "description": "A successful response.",
                "content": {}
              }
            }
          }
        },
        "/addresses/": {
          "get": {
            "tags": [],
            "operationId": "addresses:index",
            "description": "",
            "parameters": [],
            "deprecated": false,
            "responses": {
              "200": {
                "description": "A successful response.",
                "content": {}
              }
            }
          },
          "post": {
            "tags": [],
            "operationId": "addresses:create",
            "description": "",
            "parameters": [],
            "deprecated": false,
            "responses": {
              "200": {
                "description": "A successful response.",
                "content": {}
              }
            }
          }
        },
        "/addresses/{id}": {
          "get": {
            "tags": [],
            "operationId": "addresses:fetch",
            "description": "",
            "parameters": [
              {
                "name": "id",
                "in": "path",
                "required": true,
                "deprecated": false,
                "schema": {
                  "type": "string"
                }
              }
            ],
            "deprecated": false,
            "responses": {
              "200": {
                "description": "A successful response.",
                "content": {}
              }
            }
          },
          "post": {
            "tags": [],
            "operationId": "addresses:update",
            "description": "",
            "parameters": [],
            "deprecated": false,
            "responses": {
              "200": {
                "description": "A successful response.",
                "content": {}
              }
            }
          },
          "delete": {
            "tags": [],
            "operationId": "addresses:delete",
            "description": "",
            "parameters": [
              {
                "name": "id",
                "in": "path",
                "required": true,
                "deprecated": false,
                "schema": {
                  "type": "string"
                }
              }
            ],
            "deprecated": false,
            "responses": {
              "200": {
                "description": "A successful response.",
                "content": {}
              }
            }
          }
        },
        "/applicants/": {
          "get": {
            "tags": [],
            "operationId": "applicants:index",
            "description": "",
            "parameters": [],
            "deprecated": false,
            "responses": {
              "200": {
                "description": "A successful response.",
                "content": {}
              }
            }
          },
          "post": {
            "tags": [],
            "operationId": "applicants:create",
            "description": "",
            "parameters": [],
            "deprecated": false,
            "responses": {
              "200": {
                "description": "A successful response.",
                "content": {}
              }
            }
          }
        },
        "/applicants/{id}": {
          "get": {
            "tags": [],
            "operationId": "applicants:fetch",
            "description": "",
            "parameters": [
              {
                "name": "id",
                "in": "path",
                "required": true,
                "deprecated": false,
                "schema": {
                  "type": "string"
                }
              }
            ],
            "deprecated": false,
            "responses": {
              "200": {
                "description": "A successful response.",
                "content": {}
              }
            }
          },
          "post": {
            "tags": [],
            "operationId": "applicants:update",
            "description": "",
            "parameters": [],
            "deprecated": false,
            "responses": {
              "200": {
                "description": "A successful response.",
                "content": {}
              }
            }
          },
          "delete": {
            "tags": [],
            "operationId": "applicants:delete",
            "description": "",
            "parameters": [
              {
                "name": "id",
                "in": "path",
                "required": true,
                "deprecated": false,
                "schema": {
                  "type": "string"
                }
              }
            ],
            "deprecated": false,
            "responses": {
              "200": {
                "description": "A successful response.",
                "content": {}
              }
            }
          }
        },
        "/planning_applications/": {
          "get": {
            "tags": [],
            "operationId": "planning_applications:index",
            "description": "",
            "parameters": [],
            "deprecated": false,
            "responses": {
              "200": {
                "description": "A successful response.",
                "content": {}
              }
            }
          },
          "post": {
            "tags": [],
            "operationId": "planning_applications:create",
            "description": "",
            "parameters": [],
            "deprecated": false,
            "responses": {
              "200": {
                "description": "A successful response.",
                "content": {}
              }
            }
          }
        },
        "/planning_applications/{id}": {
          "get": {
            "tags": [],
            "operationId": "planning_applications:fetch",
            "description": "",
            "parameters": [
              {
                "name": "id",
                "in": "path",
                "required": true,
                "deprecated": false,
                "schema": {
                  "type": "string"
                }
              }
            ],
            "deprecated": false,
            "responses": {
              "200": {
                "description": "A successful response.",
                "content": {}
              }
            }
          },
          "post": {
            "tags": [],
            "operationId": "planning_applications:update",
            "description": "",
            "parameters": [],
            "deprecated": false,
            "responses": {
              "200": {
                "description": "A successful response.",
                "content": {}
              }
            }
          },
          "delete": {
            "tags": [],
            "operationId": "planning_applications:delete",
            "description": "",
            "parameters": [
              {
                "name": "id",
                "in": "path",
                "required": true,
                "deprecated": false,
                "schema": {
                  "type": "string"
                }
              }
            ],
            "deprecated": false,
            "responses": {
              "200": {
                "description": "A successful response.",
                "content": {}
              }
            }
          }
        },
        "/site_addresses/": {
          "get": {
            "tags": [],
            "operationId": "site_addresses:index",
            "description": "",
            "parameters": [],
            "deprecated": false,
            "responses": {
              "200": {
                "description": "A successful response.",
                "content": {}
              }
            }
          },
          "post": {
            "tags": [],
            "operationId": "site_addresses:create",
            "description": "",
            "parameters": [],
            "deprecated": false,
            "responses": {
              "200": {
                "description": "A successful response.",
                "content": {}
              }
            }
          }
        },
        "/site_addresses/{id}": {
          "get": {
            "tags": [],
            "operationId": "site_addresses:fetch",
            "description": "",
            "parameters": [
              {
                "name": "id",
                "in": "path",
                "required": true,
                "deprecated": false,
                "schema": {
                  "type": "string"
                }
              }
            ],
            "deprecated": false,
            "responses": {
              "200": {
                "description": "A successful response.",
                "content": {}
              }
            }
          },
          "post": {
            "tags": [],
            "operationId": "site_addresses:update",
            "description": "",
            "parameters": [],
            "deprecated": false,
            "responses": {
              "200": {
                "description": "A successful response.",
                "content": {}
              }
            }
          },
          "delete": {
            "tags": [],
            "operationId": "site_addresses:delete",
            "description": "",
            "parameters": [
              {
                "name": "id",
                "in": "path",
                "required": true,
                "deprecated": false,
                "schema": {
                  "type": "string"
                }
              }
            ],
            "deprecated": false,
            "responses": {
              "200": {
                "description": "A successful response.",
                "content": {}
              }
            }
          }
        }
      },
      "components": {
        "schemas": {},
        "securitySchemes": {}
      }
    }
