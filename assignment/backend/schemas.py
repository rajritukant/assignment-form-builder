source_form_template_schema = {
    "type": "object",
    "properties": {
        "type": {"type": "string"},
        "fields": {
            "type": "object",
            "properties": {
                "apiKey": {
                    "type": "object",
                    "properties": {
                        "type": {"type": "string"},
                        "label": {"type": "string"},
                        "regexErrorMessage": {"type": "string"},
                        "placeholder": {"type": "string"},
                        "regex": {"type": "string"},
                        "required": {"type": "boolean"},
                    },
                    "required": ["type", "label", "regexErrorMessage", "placeholder", "regex", "required"],
                    "additionalProperties": False
                },
                "useHTTP": {
                    "type": "object",
                    "properties": {
                        "type": {"type": "string"},
                        "required": {"type": "boolean"},
                        "label": {"type": "string"},
                    },
                    "required": [
                        "type",
                        "required",
                        "label",
                    ],
                    "additionalProperties": False
                },
                "category": {
                    "type": "object",
                    "properties": {
                        "type": {"type": "string"},
                        "label": {"type": "string"},
                        "required": {"type": "boolean"},
                        "options": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "label": {"type": "string"},
                                    "value": {"type": "string"}
                                },
                                "required": ["label", "value"],
                                "additionalProperties": False
                            },
                            "minItems": 1
                        },
                    },
                    "required": [
                        "type", "label", "required", "options"],
                    "additionalProperties": False
                }
            },
            "required": ["apiKey", "useHTTP", "category"]
        }
    },
    "required": ["type", "fields"],
    "additionalProperties": False
}
