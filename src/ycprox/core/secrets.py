import keyring
import json
from keyring.backend import KeyringBackend
from ycprox.core.config import settings
from enum import Enum


class TestKeyring(KeyringBackend):
    priority = 1
    storage = {}

    def set_password(self, service, username, password):
        self.storage[(service, username)] = password

    def get_password(self, service, username):
        return self.storage.get((service, username))

    def delete_password(self, service, username):
        self.storage.pop((service, username), None)


# assert settings.debug, "Debug mode must be enabled"
# keyring.set_keyring(TestKeyring())

class SecretsNames(Enum):
    OAUTH = "oauth_yandex_token"
    PROXY_SETTINGS = "proxy_settings"

class Vault():
    secrets: dict[SecretsNames, str] = {} 

    def load_oauth_token(self) -> str | None:
        token = keyring.get_password(settings.cli_name, SecretsNames.OAUTH.value)
        if token:
            self.secrets[SecretsNames.OAUTH] = token
            return token
        else:
            return None

    def get_oauth_token(self) -> str | None:
        return self.secrets.get(SecretsNames.OAUTH.value)

    def save_oauth_token(self, token: str):
        self.secrets[SecretsNames.OAUTH.value] = token
        keyring.set_password(settings.cli_name, SecretsNames.OAUTH.value, token)

    def remove_oauth_token(self):
        self.secrets.pop(SecretsNames.OAUTH.value, None)
        keyring.delete_password(settings.cli_name, SecretsNames.OAUTH.value)

    def save_proxy_settings(self, proxy_settings: dict):
        self.secrets[SecretsNames.PROXY_SETTINGS.value] = proxy_settings
        keyring.set_password(settings.cli_name, SecretsNames.PROXY_SETTINGS.value, json.dumps(proxy_settings))

    def get_proxy_settings(self) -> dict | None:
        """Load proxy settings from keyring."""
        data = keyring.get_password(settings.cli_name, SecretsNames.PROXY_SETTINGS.value)
        if data:
            proxy_settings = json.loads(data)
            self.secrets[SecretsNames.PROXY_SETTINGS] = proxy_settings
            return proxy_settings
        return None

    def pop_proxy_settings(self) -> dict | None:
        """Load and remove proxy settings from keyring."""
        proxy_settings = self.get_proxy_settings()
        if proxy_settings:
            self.secrets.pop(SecretsNames.PROXY_SETTINGS, None)
            keyring.delete_password(settings.cli_name, SecretsNames.PROXY_SETTINGS.value)
        return proxy_settings

vault = Vault()