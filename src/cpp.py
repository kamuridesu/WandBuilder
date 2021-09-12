import json


def buildCPP(code: str) -> str:
    data = {
            "code": code,
            "options": "warning,gnu++1y",
            "compiler": "gcc-head"
        }
    return json.dumps(data)
