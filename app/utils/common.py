import random
import string
import json


def is_json(json_to_check: bytes):
    try:
        json.loads(json_to_check)
    except ValueError as e:
        return False
    return True


def random_hash(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


if __name__ == "__main__":
    print(random_hash(100))