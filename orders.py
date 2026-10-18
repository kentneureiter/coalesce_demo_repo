"""Order history."""
from services.user import get_user

_ORDERS = [
    {"order_id": 101, "user_id": 1, "total": 2399},
    {"order_id": 102, "user_id": 2, "total": 4500},
    {"order_id": 103, "user_id": 1, "total": 1550},
]


def order_history(user_id):
    """Return the user's name and their past orders."""
    user = get_user(user_id)
    orders = [o for o in _ORDERS if o["user_id"] == user_id]
    return {"customer": user.name, "orders": orders}
