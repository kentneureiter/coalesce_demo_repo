"""Tiny in-memory data layer for the demo app."""
from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    email: str

    @classmethod
    def get(cls, user_id):
        row = _USERS.get(user_id)
        if row is None:
            raise KeyError(f"no user with id {user_id}")
        return cls(**row)


_USERS = {
    1: {"id": 1, "name": "Ada Lovelace", "email": "ada@example.com"},
    2: {"id": 2, "name": "Alan Turing", "email": "alan@example.com"},
    3: {"id": 3, "name": "Grace Hopper", "email": "grace@example.com"},
}
