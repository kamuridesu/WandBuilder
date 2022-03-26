import json


def buildJava(code: str) -> str:
    data = {
            "code": code,
            "compiler": "openjdk-jdk-15.0.3+2"
        }
    return json.dumps(data)
