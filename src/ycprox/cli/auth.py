from typing import Optional
from pydantic_settings import CliSubCommand, CliApp
from pydantic import BaseModel, Field, model_validator
from ycprox.core.secrets import vault
from getpass import getpass
from ycprox.core.config import settings

oauth_url = "https://oauth.yandex.ru/authorize?response_type=token&client_id=1a6990aa636648e9b2ef855fa7bec2fb&_ym_uid=1737881378596538906&mc=v"

class Auth(BaseModel):
    """Use this command to get Yandex OAuth token to spin up the proxy"""

    def cli_cmd(self) -> None:
        print(f"Go to {oauth_url}, paste the token and press Enter to continue:")
        token = getpass("Token: ")
        vault.save_oauth_token(token)
        print("Token saved successfully")

class Proxy(BaseModel):
    name: str = Field(description="Name of the proxy gateway", default="proxy-gateway")
    org_id: Optional[str] = Field(default=None, description="Organization ID to deploy proxy-gateway")
    cloud_id: Optional[str] = Field(default=None, description="Cloud ID to deploy proxy-gateway")
    folder_id: Optional[str] = Field(default=None, description="Folder ID to deploy proxy-gateway")

    @model_validator(mode='after')
    def set_defaults_from_env(self) -> 'Proxy':
        if self.org_id is None:
            self.org_id = settings.org_id
        if self.cloud_id is None:
            self.cloud_id = settings.cloud_id
        if self.folder_id is None:
            self.folder_id = settings.folder_id
        return self

    def cli_cmd(self) -> None:
        print("Proxy command")
        print(f"Model dump: {self.model_dump_json()}")

class Application(BaseModel, cli_prog_name=settings.cli_name):
    auth: CliSubCommand[Auth]
    proxy: CliSubCommand[Proxy]

    def cli_cmd(self) -> None:
        CliApp.run_subcommand(self)