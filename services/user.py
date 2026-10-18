"""User lookups."""
from models import User


def get_user(user_id):
    """Return the user with this id."""
    return User.get(user_id)
