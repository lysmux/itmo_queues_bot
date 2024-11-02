from urllib.parse import urljoin

from pydantic import BaseModel, computed_field


class WebhookSettings(BaseModel):
    domain: str
    path: str
    secret: str

    listen_port: int = 8000

    @computed_field
    @property
    def url(self) -> str:
        return urljoin(f"https://{self.domain}", self.path)
