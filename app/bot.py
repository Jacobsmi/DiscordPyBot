from location_db_controller import Database

import discord

from discord.ext import commands

import os 


def run_bot():
    print("Running bot")
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
    async def setlocation(ctx, country_code):
        # Validate Country Code
        if (country_code.isalpha() and len(country_code) == 3):
            # Parse out necessary information
            country_code = country_code.upper()
            user_id = ctx.message.author.id
            user_name = str(bot.get_user(user_id)).split("#")[0]
            # Insert information into the database
            result = loc_db.insert_location(user_id, country_code)
            if result == 'insert success':
                # Send a confirmation message using ctx.send()
                await ctx.send(f"{user_name}'s location has been set as {country_code}.\nIf that is not correct please !setlocation again")
            elif result == 'update success':
                await ctx.send(f"{user_name}'s location has been updated to {country_code}.")
            else:
                await ctx.send('There was an error setting your location.')
        else: 
            await ctx.send('Country Code Format Error!\nPlease make sure you are entering your countries 3 letter country code\nExample: England = GBR')


    @bot.command()
    async def locations(ctx, *args):
        if not args:
            all_user_locs = loc_db.get_all_locations()
            locs = {}
            for entry in all_user_locs:
                if entry[1] in locs.keys():
                    locs[entry[1]] = locs[entry[1]] + 1
                else:
                    locs[entry[1]] = 1
            # Creating a string to return
            all_locs_str = "Locations of Users:\n"
            for key in locs:
                all_locs_str += f'{key}: {locs[key]}\n'
            await ctx.send(all_locs_str)
        else: 
            print(args[0])

    # Runs the bot with Disccord Developer Portal bot token
    bot.run(os.getenv("TOKEN"))    