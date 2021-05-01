schema_brew = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "array",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": [],
    "examples": [
        [
            {
                "id": 9094,
                "obdb_id": "bnaf-llc-austin",
                "name": "Bnaf, LLC",
                "brewery_type": "planning",
                "street": "None",
                "address_2": "None",
                "address_3": "None",
                "city": "Austin",
                "state": "Texas",
                "county_province": "None",
                "postal_code": "78727-7602",
                "country": "United States",
                "longitude": "None",
                "latitude": "None",
                "phone": "None",
                "website_url": "None",
                "updated_at": "2018-07-24T00:00:00.000Z",
                "created_at": "2018-07-24T00:00:00.000Z"
            }
        ]
    ],
    "additionalItems": True,
    "items": {
        "$id": "#/items",
        "anyOf": [
            {
                "$id": "#/items/anyOf/0",
                "type": "object",
                "title": "The first anyOf schema",
                "description": "An explanation about the purpose of this instance.",
                "default": {},
                "examples": [
                    {
                        "id": 9094,
                        "obdb_id": "bnaf-llc-austin",
                        "name": "Bnaf, LLC",
                        "brewery_type": "planning",
                        "street": "None",
                        "address_2": "None",
                        "address_3": "None",
                        "city": "Austin",
                        "state": "Texas",
                        "county_province": "None",
                        "postal_code": "78727-7602",
                        "country": "United States",
                        "longitude": "None",
                        "latitude": "None",
                        "phone": "None",
                        "website_url": "None",
                        "updated_at": "2018-07-24T00:00:00.000Z",
                        "created_at": "2018-07-24T00:00:00.000Z"
                    }
                ],
                "required": [
                    "id",
                    "obdb_id",
                    "name",
                    "brewery_type",
                    "street",
                    "address_2",
                    "address_3",
                    "city",
                    "state",
                    "county_province",
                    "postal_code",
                    "country",
                    "longitude",
                    "latitude",
                    "phone",
                    "website_url",
                    "updated_at",
                    "created_at"
                ],
                "properties": {
                    "id": {
                        "$id": "#/items/anyOf/0/properties/id",
                        "type": "integer",
                        "title": "The id schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": 0,
                        "examples": [
                            9094
                        ]
                    },
                    "obdb_id": {
                        "$id": "#/items/anyOf/0/properties/obdb_id",
                        "type": "string",
                        "title": "The obdb_id schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "bnaf-llc-austin"
                        ]
                    },
                    "name": {
                        "$id": "#/items/anyOf/0/properties/name",
                        "type": "string",
                        "title": "The name schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "Bnaf, LLC"
                        ]
                    },
                    "brewery_type": {
                        "$id": "#/items/anyOf/0/properties/brewery_type",
                        "type": "string",
                        "title": "The brewery_type schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "planning"
                        ]
                    },
                    "street": {
                        "$id": "#/items/anyOf/0/properties/street",
                        "type": ["string", "null"],
                        "title": "The street schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            None
                        ]
                    },
                    "address_2": {
                        "$id": "#/items/anyOf/0/properties/address_2",
                        "type": ["string", "null"],
                        "title": "The address_2 schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            None
                        ]
                    },
                    "address_3": {
                        "$id": "#/items/anyOf/0/properties/address_3",
                        "type": ["string", "null"],
                        "title": "The address_3 schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            None
                        ]
                    },
                    "city": {
                        "$id": "#/items/anyOf/0/properties/city",
                        "type": ["string", "null"],
                        "title": "The city schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            None
                        ]
                    },
                    "state": {
                        "$id": "#/items/anyOf/0/properties/state",
                        "type": ["string", "null"],
                        "title": "The state schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "Texas", None
                        ]
                    },
                    "county_province": {
                        "$id": "#/items/anyOf/0/properties/county_province",
                        "type": ["string", "null"],
                        "title": "The county_province schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            None
                        ]
                    },
                    "postal_code": {
                        "$id": "#/items/anyOf/0/properties/postal_code",
                        "type": ["string", "null"],
                        "title": "The postal_code schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "78727-7602", None
                        ]
                    },
                    "country": {
                        "$id": "#/items/anyOf/0/properties/country",
                        "type": ["string", "null"],
                        "title": "The country schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "United States", None
                        ]
                    },
                    "longitude": {
                        "$id": "#/items/anyOf/0/properties/longitude",
                        "type": ["string", "null"],
                        "title": "The longitude schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            None
                        ]
                    },
                    "latitude": {
                        "$id": "#/items/anyOf/0/properties/latitude",
                        "type": ["string", "null"],
                        "title": "The latitude schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            None
                        ]
                    },
                    "phone": {
                        "$id": "#/items/anyOf/0/properties/phone",
                        "type": ["string", "null"],
                        "title": "The phone schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            None
                        ]
                    },
                    "website_url": {
                        "$id": "#/items/anyOf/0/properties/website_url",
                        "type": ["string", "null"],
                        "title": "The website_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            None
                        ]
                    },
                    "updated_at": {
                        "$id": "#/items/anyOf/0/properties/updated_at",
                        "type": "string",
                        "title": "The updated_at schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "2018-07-24T00:00:00.000Z"
                        ]
                    },
                    "created_at": {
                        "$id": "#/items/anyOf/0/properties/created_at",
                        "type": "string",
                        "title": "The created_at schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "2018-07-24T00:00:00.000Z"
                        ]
                    }
                },
                "additionalProperties": True
            }
        ]
    }
}

schema_dog_one_image = {
    'type': "object",
    "properties": {
        'message': {'type': "string"},
        'status': {'type': "string"}
    }
}

schema_dog_images = {
    'type': "object",
    "properties": {
        'message': {'type': "array",
                    "items": {
                        "type": "string"
                    },
                    "maxItems": None
                    },
        'status': {'type': "string"}
    },
    "required": ["message", "status"]
}

schema_jsonplaceholder = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "userId": 1,
            "id": 1,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut "
                    "ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto "
        }
    ],
    "required": [
        "userId",
        "id",
        "title",
        "body"
    ],
    "properties": {
        "userId": {
            "$id": "#/properties/userId",
            "type": "integer",
            "title": "The userId schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "id": {
            "$id": "#/properties/id",
            "type": "integer",
            "title": "The id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "title": {
            "$id": "#/properties/title",
            "type": "string",
            "title": "The title schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
            ]
        },
        "body": {
            "$id": "#/properties/body",
            "type": "string",
            "title": "The body schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut "
                "quas totam\nnostrum rerum est autem sunt rem eveniet architecto "
            ]
        }
    },
    "additionalProperties": True
}
