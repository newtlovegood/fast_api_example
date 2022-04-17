from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    EMAIL_TEST_USER: EmailStr = "test@instance.com"
    FIRST_SUPERUSER: EmailStr = "admin@example.com"
    FIRST_SUPERUSER_PASSWORD: str = 'password'
    USERS_OPEN_REGISTRATION: bool = False

    class Config:
        case_sensitive = True


settings = Settings()

