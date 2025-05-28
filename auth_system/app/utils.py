# app/utils.py

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

# Create the hasher instance
ph = PasswordHasher()

# Hash the password
def hash_password(password: str) -> str:
    return ph.hash(password)

# Verify a hashed password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        ph.verify(hashed_password, plain_password)
        return True
    except VerifyMismatchError:
        return False

