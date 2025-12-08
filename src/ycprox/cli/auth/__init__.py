from pydantic_settings import CliSubCommand, CliApp
from pydantic import BaseModel
from ycprox.core.config import settings
from ycprox.cli.auth.init import AuthInit
from ycprox.cli.auth.reset import AuthReset


class AuthApp(BaseModel, cli_prog_name=settings.cli_name):
    """Use this command to manage the Yandex OAuth authentication token"""

    init: CliSubCommand[AuthInit]
    reset: CliSubCommand[AuthReset]

    def cli_cmd(self) -> None:
        CliApp.run_subcommand(self)