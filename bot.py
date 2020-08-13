import discord

from discord.ext import commands

import os 

def run_bot():
    # Create an instance of a bot with the discord py commands extension
    bot = commands.Bot(command_prefix = "!")
    
    # Add a command for the bot to listen for
    # by default listens for the function name and takes things after command as variable
    @bot.command()
    async def setlocation(ctx, location: str):
        print(f"Location: {location}")

    # Runs the bot with Disccord Developer Portal bot token
    bot.run(os.getenv("TOKEN"))    