import sys
import time
import argparse

import discord

from colorama import Fore

from atos import __version__ as atos_version

# from atos.core.bot import ATOSBot


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
    print(Fore.GREEN + "{0:-^50}".format(" Automated Tournament Organisation System "))
    print(Fore.BLUE + "{0:^50}".format("Discord bot made by El Laggron"))
    print("")
    print(Fore.RED + " {0:<20} {1:>10}".format("Bot version:", atos_version))
    print(Fore.RED + " {0:<20} {1:>10}".format("Discord.py version:", discord.__version__))


def main():
    cli_flags = parse_cli_flags(sys.argv[1:])
    if cli_flags.version:
        print(f"ATOS Discord bot - {atos_version}")
        sys.exit(0)
    print_welcome()
    time.sleep(1)


if __name__ == "__main__":
    main()
