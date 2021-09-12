import json


def buildRust(code: str) -> str:
    data = {
            "code": code,
            "compiler": "rust-head"
        }
    return json.dumps(data)
