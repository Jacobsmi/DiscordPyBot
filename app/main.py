# Import that loads in variables from the .env file
from dotenv import load_dotenv

from bot import run_bot
# Import needed for the dotenv library
import os

def main():
    # Function that loads the variables from .env
    load_dotenv()

    print("Welcome to the JacobsM1 Discord bot\nCreated by: Michael Jacobs")
    # runs the bot with run_bot() from bot.py
    run_bot()


if __name__ == "__main__":
    main()
