import json


def buildPHP(code: str) -> str:
    data = {
            "code": code,
            "compiler": "php-head"
        }
    return json.dumps(data)
