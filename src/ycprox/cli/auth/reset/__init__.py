from pydantic import BaseModel
from ycprox.core.secrets import vault

class AuthReset(BaseModel):
    """Use this command to reset the Yandex OAuth authentication token"""

    def cli_cmd(self) -> None:
        vault.remove_oauth_token()
        print("OAuth token reset successfully")