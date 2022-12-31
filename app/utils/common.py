import json


def is_json(json_to_check: bytes):
    try:
        json.loads(json_to_check)
    except ValueError as e:
        return False
    return True
