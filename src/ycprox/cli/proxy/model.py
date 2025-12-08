from typing import Optional
from pydantic import BaseModel, Field, model_validator
from ycprox.core.config import settings


class ProxySettings(BaseModel):
    """Shared proxy settings model for up/down commands."""

    name: str = Field(description="Name of the proxy gateway", default="proxy-gateway")
    org_id: Optional[str] = Field(default=None, description="Organization ID to deploy proxy-gateway")
    cloud_id: Optional[str] = Field(default=None, description="Cloud ID to deploy proxy-gateway")
    folder_id: Optional[str] = Field(default=None, description="Folder ID to deploy proxy-gateway")

    @model_validator(mode='after')
    def set_defaults_from_env(self) -> 'ProxySettings':
        if self.org_id is None:
            self.org_id = settings.org_id
        if self.cloud_id is None:
            self.cloud_id = settings.cloud_id
        if self.folder_id is None:
            self.folder_id = settings.folder_id
        return self
