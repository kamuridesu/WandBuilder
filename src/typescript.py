import json


def buildTS(code: str) -> str:
    data = {
            "code": code,
            "compiler": "typescript-3.9.5"
        }
    return json.dumps(data)
