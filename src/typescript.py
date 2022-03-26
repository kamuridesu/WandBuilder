import json


def buildTS(code: str) -> str:
    data = {
            "code": code,
            "compiler": "typescript-4.2.4"
        }
    return json.dumps(data)
