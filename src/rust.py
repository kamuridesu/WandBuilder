import json


def buildRust(code: str) -> str:
    data = {
            "code": code,
            "compiler": "rust-1.51.0"
        }
    return json.dumps(data)
