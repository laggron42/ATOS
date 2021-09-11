import discord
import logging

log = logging.getLogger("atos")


class BotBase(discord.Client):
    pass


class ATOSBot(BotBase, discord.AutoShardedClient):
    """
    The ATOS Discord bot class.
    """

    async def on_shard_ready(self, shard_id: int):
        log.debug(f"Connected to shard #{shard_id}")

    async def on_ready(self):
        log.info(f"Successfully logged in as {self.user} ({self.user.id})!")
