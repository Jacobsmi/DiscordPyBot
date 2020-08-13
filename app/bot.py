from location_db_controller import Database

import discord

from discord.ext import commands

import os 


def run_bot():
    # Create an instance of the database that will store information for the project
    loc_db = Database()
    loc_db.create_connection()
    # Create an instance of a bot with the discord py commands extension
    bot = commands.Bot(command_prefix = "!")
    
    @bot.command()
    async def locationhelp(ctx):
        help_str = ""
        help_str += "You can set your location using ``!setlocation country_code``\n"
        help_str += "Please use your countries three letter country code which can be found here https://abbreviations.yourdictionary.com/articles/country-abbreviations.html\n"
        help_str += "Example: !setlocation USA or !setlocation GBR\n"
        await ctx.send(help_str)
    
    # Add a command for the bot to listen for
    # by default listens for the function name and takes things after command as variable
    @bot.command()
    async def setlocation(ctx, *loc_args):
        loc_str = ' '.join(loc_args)
        user_id = ctx.message.author.id
        await ctx.send(f'{user_id} location has been set as {loc_str}.\nIf that is not correct please !setlocation again')

    # @bot.command()
    # async def locations(ctx, *user_args):

    # Runs the bot with Disccord Developer Portal bot token
    bot.run(os.getenv("TOKEN"))    