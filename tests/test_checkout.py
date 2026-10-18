import pytest

from checkout import checkout, format_cents
from orders import order_history


def test_checkout_receipt():
    receipt = checkout(1, {"notebook": 2, "pen": 1})
    assert receipt["to"] == "ada@example.com"
    assert receipt["customer"] == "Ada Lovelace"
    assert receipt["subtotal"] == 1025
    assert receipt["tax"] == 62
    assert receipt["shipping"] == 599
    assert receipt["total"] == 1686


def test_free_shipping():
    receipt = checkout(2, {"headphones": 1})
    assert receipt["shipping"] == 0


def test_unknown_item():
    with pytest.raises(ValueError):
        checkout(1, {"laptop": 1})


def test_format_cents():
    assert format_cents(123456) == "$1,234.56"


def test_order_history():
    history = order_history(1)
    assert history["customer"] == "Ada Lovelace"
    assert [o["order_id"] for o in history["orders"]] == [101, 103]
