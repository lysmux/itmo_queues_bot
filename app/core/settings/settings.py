from pydantic_settings import BaseSettings, SettingsConfigDict

from app.core.settings.bot import BotSettings
from app.core.settings.database import DatabaseSettings
from app.core.settings.redis import RedisSettings
from app.core.settings.webhook import WebhookSettings


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_nested_delimiter="_")

    log_level: str = "INFO"

    database: DatabaseSettings
    redis: RedisSettings
    bot: BotSettings
    webhook: WebhookSettings | None = None
