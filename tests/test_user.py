import pytest

from services.user import get_user


def test_get_user_returns_user():
    user = get_user(1)
    assert user.name == "Ada Lovelace"
    assert user.email == "ada@example.com"


def test_get_user_missing():
    with pytest.raises(KeyError):
        get_user(999)
