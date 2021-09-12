import json


def buildJS(code: str) -> str:
    data = {
            "code": code,
            "compiler": "nodejs-head"
        }
    return json.dumps(data)
