from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    SQLALCHEMY_DATABASE_URI: str | None = None
    BASE_URL: str = "/almacen"


app_config = AppConfig()
