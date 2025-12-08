from ycprox.cli.proxy.model import ProxySettings
from ycprox.core.secrets import vault


class ProxyAppUp(ProxySettings):
    """Use this command to spin up the proxy gateway.\nDo not forget to authenticate in Yandex first using the `ycprox auth` command."""

    def cli_cmd(self) -> None:
        print("Proxy up command")
        print(f"Settings: {self.model_dump_json()}")
        # Save settings for later use by down command
        vault.save_proxy_settings(self.model_dump())