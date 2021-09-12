import discord
import time
import sys

from typing import TYPE_CHECKING
from discord.ext import commands

from dislash.application_commands.slash_core import slash_command
from dislash.interactions.app_command_interaction import SlashInteraction
from dislash.interactions.message_components import ActionRow, Button, ButtonStyle

from atos import __version__ as bot_version

if TYPE_CHECKING:
    from .bot import ATOSBot


class Core(commands.Cog):
    """
    Core commands of ATOS
    """

    def __init__(self, bot: "ATOSBot"):
        self.bot = bot

    @slash_command(description="Shows the bot's response time.")
    async def ping(self, inter: SlashInteraction):
        t1 = time.time()
        msg = await inter.reply("Pong!")
        t2 = time.time()
        await msg.edit(content="Pong!\nDelay: `{t}ms`".format(t=round((t2 - t1) * 1000)))

    @slash_command(description="Shows info about ATOS")
    async def info(self, inter: SlashInteraction):
        action_row = ActionRow(
            Button(
                style=ButtonStyle.link,
                label="Documentation",
                emoji="📰",
                url="https://atos.laggron.red",
            ),
            Button(
                style=ButtonStyle.link,
                label="Discord server",
                emoji="🌐",
                url="https://discord.gg/DC6zCsZ",
            ),
            Button(
                style=ButtonStyle.link,
                label="Github",
                emoji="🖥",
                url="https://github.com/retke/ATOS",
            ),
        )
        py = sys.version_info
        embed = discord.Embed()
        embed.add_field(name="ATOS version", value=bot_version)
        embed.add_field(name="Python version", value=f"{py.major}.{py.minor}.{py.micro}")
        embed.add_field(name="Discord.py version", value=discord.__version__)
        await inter.reply(embed=embed, components=[action_row])
