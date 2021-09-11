import os
import sys
import time
import argparse
import logging
import signal
import asyncio

import discord

from rich import print

from atos import __version__ as atos_version
from atos.loggers import init_logger

from atos.core.bot import ATOSBot

log = logging.getLogger("atos")


def parse_cli_flags(args):
    parser = argparse.ArgumentParser(description="ATOS - Discord bot", usage="atos [arguments]")
    parser.add_argument(
        "--version", "-V", action="store_true", help="Displays the bot's current version"
    )
    parser.add_argument("--debug", action="store_true", help="Enables debug logger")
    parser.add_argument("--token", help="Discord bot token")
    parser.add_argument(
        "--safe-start", action="store_true", help="Start the bot without loading any cog"
    )
    args = parser.parse_args(args)
    return args


def print_welcome():
    print("[green]{0:-^50}[/green]".format(" Automated Tournament Organisation System "))
    print("[blue]{0:^50}[/blue]".format("Discord bot made by El Laggron"))
    print("")
    print(" [red]{0:<20}[/red] [yellow]{1:>10}[/yellow]".format("Bot version:", atos_version))
    print(
        " [red]{0:<20}[/red] [yellow]{1:>10}[/yellow]".format(
            "Discord.py version:", discord.__version__
        )
    )
    print("")


async def shutdown_handler(bot: ATOSBot, signal_type: str = None):
    if signal_type:
        log.info(f"Received {signal_type}, stopping the bot...")
    else:
        log.info(f"Stopping the bot...")
    try:
        await bot.close()
    finally:
        pending = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
        [task.cancel() for task in pending]
        await asyncio.gather(*pending, return_exceptions=True)


def main():
    bot = None
    cli_flags = parse_cli_flags(sys.argv[1:])
    if cli_flags.version:
        print(f"ATOS Discord bot - {atos_version}")
        sys.exit(0)

    print_welcome()
    time.sleep(1)

    try:
        init_logger(cli_flags.debug)

        token = cli_flags.token or os.environ.get("ATOS_TOKEN", None)
        if not token:
            log.error("Token not found!")
            print("[yellow]You need to provide a token before starting the bot.[/yellow]")
            time.sleep(1)
            sys.exit(0)
        log.info("Initialized bot, connecting to Discord...")

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        bot = ATOSBot()

        try:
            loop.add_signal_handler(signal.SIGTERM, shutdown_handler, bot, "SIGTERM")
        except NotImplementedError:
            # Not a UNIX environment (Windows)
            pass

        loop.create_task(bot.start(token))
        loop.run_forever()
    except KeyboardInterrupt:
        if bot is not None:
            loop.run_until_complete(shutdown_handler(bot, "Ctrl+C"))
    except Exception:
        log.critical("Unhandled exception.", exc_info=True)
        if bot is not None:
            loop.run_until_complete(shutdown_handler(bot))


if __name__ == "__main__":
    main()
