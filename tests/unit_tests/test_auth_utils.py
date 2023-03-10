from app.util.common import is_json, random_hash


def test_random_hash():
    assert len(random_hash()) == 12
    assert len(random_hash(100)) == 100


def test_is_json():
    assert is_json(b"{}")
    assert is_json(b'{"test": "test"}')
    assert not is_json(b"test")
    assert not is_json(b"test test")
    assert not is_json(b"test test test")
