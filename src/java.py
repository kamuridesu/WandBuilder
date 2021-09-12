import json


def buildJava(code: str) -> str:
    data = {
            "code": code,
            "compiler": "openjdk-head"
        }
    return json.dumps(data)
