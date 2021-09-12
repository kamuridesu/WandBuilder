import json


def buildPython(code: str) -> str:
    data = {
            "code": code,
            "compiler": "cpython-head"
        }
    return json.dumps(data)
