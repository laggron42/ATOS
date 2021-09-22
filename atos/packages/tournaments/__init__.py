import logging
import aiohttp

from typing import TYPE_CHECKING
from .tournaments import Tournaments

if TYPE_CHECKING:
    from atos.core.bot import ATOSBot

log = logging.getLogger("atos.tournaments")


async def restore_tournaments(bot: "ATOSBot", cog: Tournaments):
    await bot.wait_until_ready()
    await cog.restore_tournaments()


def check_for_aiodns():
    """
    The achallonge library has special behaviour with resolvers
    It checks on load if aiodns is available, to determine which resolver to use.

    However, aiohttp will return instances of AsyncResolver only if the "aiodns" lib is
    available on load, else it will fail.

    Basically there's a problem if aiodns is installed with downloader, since aiohttp was
    initialized without aiodns, and achallonge believes it was, as long as the lib is importable.
    """
    try:
        import aiodns

        aiohttp.AsyncResolver()
    except ImportError:
        pass
    except RuntimeError as e:
        raise RuntimeError(
            "There is a problem with the `aiodns` library which cannot properly load. "
            "Please do one of the following:\n"
            "- Properly install `aiodns` in your environment (use `python3.8 -m pip install "
            "aiodns`, __the `[p]pipinstall` command will not work__), then restart the bot\n"
            "- Fully uninstall the `aiodns` library (it can be hidden in "
            "`redbot/cogs/Downloader/lib/`)"
        ) from e


async def setup(bot: "ATOSBot"):
    n = Tournaments(bot)
    check_for_aiodns()
    bot.add_cog(n)
    # await restore_tournaments(bot, n)
    log.debug("Cog successfully loaded on the instance.")
