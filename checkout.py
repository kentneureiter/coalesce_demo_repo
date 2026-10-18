"""Checkout: turn a cart into a priced receipt for a user."""
from services.user import get_user

# Catalog prices in cents.
PRICES = {
    "notebook": 450,
    "pen": 125,
    "backpack": 3999,
    "water_bottle": 1550,
    "headphones": 5999,
}

TAX_RATE = 0.06  # Pennsylvania sales tax
FREE_SHIPPING_OVER = 5000
SHIPPING_FLAT = 599


def line_items(cart):
    """Convert a cart mapping into a list of priced line items.

    Args:
        cart: Dict mapping SKU strings to integer quantities.

    Returns:
        List of dicts, each with keys ``sku``, ``qty``, and ``cents``
        (total price for that line in cents).

    Raises:
        ValueError: If a SKU is not in the catalog or a quantity is <= 0.
    """
    items = []
    for sku, qty in cart.items():
        if sku not in PRICES:
            raise ValueError(f"unknown item: {sku}")
        if qty <= 0:
            raise ValueError(f"bad quantity for {sku}: {qty}")
        items.append({"sku": sku, "qty": qty, "cents": PRICES[sku] * qty})
    return items


def subtotal(items):
    """Sum the ``cents`` values across all line items.

    Args:
        items: List of line-item dicts as returned by :func:`line_items`.

    Returns:
        Integer total in cents before tax and shipping.
    """
    return sum(item["cents"] for item in items)


def shipping(sub):
    """Compute flat-rate shipping, waived above the free-shipping threshold.

    Args:
        sub: Subtotal in cents.

    Returns:
        Integer shipping cost in cents (0 if subtotal >= FREE_SHIPPING_OVER).
    """
    return 0 if sub >= FREE_SHIPPING_OVER else SHIPPING_FLAT


def checkout(user_id, cart):
    """Price the cart and build a receipt addressed to the user."""
    user = get_user(user_id)
    items = line_items(cart)
    sub = subtotal(items)
    tax = round(sub * TAX_RATE)
    ship = shipping(sub)
    return {
        "to": user.email,
        "customer": user.name,
        "items": items,
        "subtotal": sub,
        "tax": tax,
        "shipping": ship,
        "total": sub + tax + ship,
    }


def format_cents(cents):
    return f"${cents / 100:,.2f}"
