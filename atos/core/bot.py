import discord
import logging

from discord.ext.commands import Bot
from dislash import SlashInteraction
from dislash.application_commands.errors import ApplicationCommandError

log = logging.getLogger("atos")
PACKAGES = []


class BotBase(Bot):
    pass


class ATOSBot(BotBase, discord.AutoShardedClient):
    """
    The ATOS Discord bot class.
    """

    async def on_shard_ready(self, shard_id: int):
        log.debug(f"Connected to shard #{shard_id}")

    async def on_ready(self):
        log.info(f"Successfully logged in as {self.user} ({self.user.id})!")
        log.info("Loading packages...")
        loaded_packages = []
        for package in PACKAGES:
            try:
                self.load_extension(package)
            except Exception:
                log.error(f"Failed to load package {package}", exc_info=True)
            else:
                loaded_packages.append(package)
        if loaded_packages:
            log.info(f"Packages loaded: {', '.join(loaded_packages)}")
        else:
            log.info("No package loaded.")

    async def on_slash_command_error(
        self, inter: SlashInteraction, error: ApplicationCommandError
    ):
        log.error(f"Error in slash command {inter.slash_command.name}", exc_info=error)
        await inter.reply("An error occured.")
