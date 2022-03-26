import json


def buildJS(code: str) -> str:
    data = {
            "code": code,
            "compiler": "nodejs-16.14.0"
        }
    return json.dumps(data)
