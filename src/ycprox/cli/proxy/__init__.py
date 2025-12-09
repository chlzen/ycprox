from pydantic import BaseModel
from pydantic_settings import CliSubCommand, CliApp
from ycprox.cli.proxy.up import ProxyAppUp
from ycprox.cli.proxy.down import ProxyAppDown
from ycprox.cli.proxy.info import ProxyAppInfo

class ProxyApp(BaseModel):
    """Use this command to deploy the proxy gateway.\nDo not forget to authenticate in Yandex first using the `ycprox auth` command."""

    up: CliSubCommand[ProxyAppUp]
    down: CliSubCommand[ProxyAppDown]
    info: CliSubCommand[ProxyAppInfo]

    def cli_cmd(self) -> None:
        CliApp.run_subcommand(self)