import json


def buildPHP(code: str) -> str:
    data = {
            "code": code,
            "compiler": "php-8.0.3"
        }
    return json.dumps(data)
