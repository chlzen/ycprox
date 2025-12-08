from pydantic_settings import CliSubCommand, CliApp
from pydantic import BaseModel
from ycprox.core.config import settings
from ycprox.cli.auth import AuthApp
from ycprox.cli.proxy import Proxy


class Application(BaseModel, cli_prog_name=settings.cli_name):
    auth: CliSubCommand[AuthApp]
    proxy: CliSubCommand[Proxy]

    def cli_cmd(self) -> None:
        CliApp.run_subcommand(self)