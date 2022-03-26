import json


def buildPython(code: str) -> str:
    data = {
            "code": code,
            "compiler": "cpython-3.10.2"
        }
    return json.dumps(data)
