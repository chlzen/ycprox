from pydantic import BaseModel
from ycprox.cli.proxy.model import ProxySettings
from ycprox.core.secrets import vault


class ProxyAppDown(BaseModel):
    """Use this command to tear down the proxy gateway."""

    def cli_cmd(self) -> None:
        # Retrieve saved settings from vault
        saved_settings = vault.pop_proxy_settings()
        
        if saved_settings is None:
            print("No proxy settings found. Was the proxy started with 'up' command?")
            return
        
        # Reconstruct ProxySettings from saved data
        settings = ProxySettings.model_validate(saved_settings)
        
        print("Proxy down command")
        print(f"Tearing down with settings: {settings.model_dump_json()}")
