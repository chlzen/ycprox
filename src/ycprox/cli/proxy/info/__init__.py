from pydantic import BaseModel

from ycprox.cli.proxy.model import ProxySettings
from ycprox.core.secrets import vault


class ProxyAppInfo(BaseModel):
    """Use this command to get information about the proxy gateway."""

    def cli_cmd(self) -> None:
        # Retrieve saved settings from vault
        saved_settings = vault.get_proxy_settings()
        
        if saved_settings is None:
            print("No proxy settings found. Was the proxy started with 'up' command?")
            return

        # Reconstruct ProxySettings from saved data
        proxy = ProxySettings.model_validate(saved_settings)

        print(f"Proxy Gateway: '{proxy.gw_name}' (id: {proxy.gateway_id}) on URL https://{proxy.gateway_domain}/")
        print(f"Cloud Function: '{proxy.cf_name}' (id: {proxy.function_id})")

        print(f"\nYou can now use https://{proxy.gateway_domain}/ to proxy requests to {proxy.url}")