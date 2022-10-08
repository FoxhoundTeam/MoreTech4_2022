from typing import Any, Dict, Optional

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    project_name: str

    jwt_secret: str
    jwt_algorithm: str = "HS256"
    jwt_expires_s: int = 60 * 60 * 60

    postgres_server: str
    postgres_user: str
    postgres_password: str
    postgres_db: str
    database_uri: Optional[PostgresDsn] = None

    @validator("database_uri", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("postgres_user"),
            password=values.get("postgres_password"),
            host=values.get("postgres_server"),
            path=f"/{values.get('postgres_db') or ''}",
        )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
