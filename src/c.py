import json


def buildC(code: str) -> str:
    data = {
            "code": code,
            "compiler": "gcc-head"
        }
    return json.dumps(data)
