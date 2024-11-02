from datetime import timedelta

from pydantic import BaseModel


class BotSettings(BaseModel):
    token: str

    sessions_ttl: timedelta = timedelta(weeks=1)
