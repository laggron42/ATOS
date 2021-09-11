from __future__ import annotations

from typing import List, Optional, Union
import discord
from discord.enums import Enum
from discord.types.snowflake import Snowflake


class ApplicationCommandType(Enum):
    chat_input = 1
    user = 2
    message = 3


class ApplicationCommandOptionType(Enum):
    subcommand = 1
    subcommand_group = 2
    string = 3
    integer = 4
    boolean = 5
    user = 6
    channel = 7
    role = 8
    mentionable = 9
    number = 10


class ApplicationCommandOptionChoice:
    name: str
    value: Union[str, int]


class ApplicationCommandOption:
    type: ApplicationCommandOptionType
    name: str
    description: str
    required: bool
    choices: List[ApplicationCommandOptionChoice]
    options: List[ApplicationCommandOption]


class ApplicationCommand(Snowflake):
    type: ApplicationCommandType
    application_id: int
    guild: Optional[discord.Guild]
    name: str
    description: str
    options: List[ApplicationCommandOption]
    default_permission: bool
    version: int
