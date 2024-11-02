from pydantic import BaseModel, computed_field
from sqlalchemy import URL


class DatabaseSettings(BaseModel):
    host: str = "localhost"
    port: int = 5432
    user: str
    password: str
    name: str

    @computed_field
    @property
    def url(self) -> str:
        return URL.create(
            drivername="postgresql+asyncpg",
            host=self.host,
            port=self.port,
            username=self.user,
            password=self.password,
            database=self.name,
        ).render_as_string(hide_password=False)
