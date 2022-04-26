from passlib.context import CryptContext

pass_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pass_context.verify(plain_password, hashed_password)


def get_password_hash(raw_password) -> str:
    return pass_context.hash(raw_password)

