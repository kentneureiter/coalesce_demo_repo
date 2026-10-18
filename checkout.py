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
    """cart: dict of sku -> quantity. Returns a list of priced line items."""
    items = []
    for sku, qty in cart.items():
        if sku not in PRICES:
            raise ValueError(f"unknown item: {sku}")
        if qty <= 0:
            raise ValueError(f"bad quantity for {sku}: {qty}")
        items.append({"sku": sku, "qty": qty, "cents": PRICES[sku] * qty})
    return items


def subtotal(items):
    return sum(item["cents"] for item in items)


def shipping(sub):
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
