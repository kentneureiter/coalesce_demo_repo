# coalesce_demo_repo

The small Python app that the agents work on during the Coalesce demo (contract section 13).

- `models.py`: `User` (id, name, email) with an in-memory store
- `services/user.py`: `get_user(user_id)` returns a `User`
- `checkout.py`: builds a receipt; calls `get_user` and reads `user.email`
- `orders.py`: order history; also calls `get_user`

Run the tests (well under 5 seconds):

```bash
python3 -m pytest -q
```

Demo branches off `main`: `feature/caching`, `feature/checkout`, `feature/orders`.
