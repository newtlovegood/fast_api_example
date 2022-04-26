from pydantic import BaseSettings, EmailStr


class settings(BaseSettings):
    SECRET_KEY: str = '722c80b0964cb83c867cbc34ec9b42a079e307b8c73e616746bf327f8b55c57a'
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    EMAIL_TEST_USER: EmailStr = "test@instance.com"
    FIRST_SUPERUSER: EmailStr = "admin@example.com"
    FIRST_SUPERUSER_PASSWORD: str = 'password'
    USERS_OPEN_REGISTRATION: bool = False
    
    class Config:
        case_sensitive = True


settings = settings()

