import discord

from discord.ext import commands

import os 

def run_bot():
    # Create an instance of a bot with the discord py commands extension
    bot = commands.Bot(command_prefix = "!")
    
    @bot.command()
    async def locationhelp(ctx):
        help_str = ""
        help_str += "You can set your location using !setlocation country_name\nExample: !setlocation United States of America"
        await ctx.send(help_str)
    
    # Add a command for the bot to listen for
    # by default listens for the function name and takes things after command as variable
    @bot.command()
    async def setlocation(ctx, *loc_args):
        loc_str = ' '.join(loc_args)
        await ctx.send(f'Your location is set as {loc_str}.\nIf that is not correct please !setlocation again')

    # Runs the bot with Disccord Developer Portal bot token
    bot.run(os.getenv("TOKEN"))    