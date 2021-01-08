import os
import discord
import json
from discord.ext import commands
from dotenv import load_dotenv
import giphy_client
from giphy_client.rest import ApiException

load_dotenv()


class Giphy(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.api_instance = giphy_client.DefaultApi()
        self.GIPHY_TOKEN = os.getenv('GIPHY_TOKEN')

    # reference: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html
    @commands.command()
    async def giphy(self, ctx, *, arg):

        try:
            arg = arg.replace(' ', "+")

            # Search Endpoint
            api_response = self.api_instance.gifs_search_get(api_key=self.GIPHY_TOKEN, q=arg, limit=1)

            if api_response.pagination.count > 0:
                # Convert api response(inline return type) data into dictionary
                # this isn't neccesary, just trying out some conversion stuff with python
                # you can do this part with simply: api_response.data.url
                api_response = api_response.data[0].to_dict()
                url = api_response['url']
                await ctx.send(url)
            else:
                await ctx.send('Query was invalid. Please try again with a new search :frowning2:')

        except ApiException as e:
            print("Exception when calling Defaultapi->gifs_search_get: %s\n" % e)

    # giphy client reference: https://github.com/Giphy/giphy-python-client
    @commands.command()
    async def giphy_rand(self, ctx, *, arg):
        try:
            arg = arg.replace(' ', "+")

            # Search Endpoint
            api_response = self.api_instance.gifs_random_get(api_key=self.GIPHY_TOKEN, tag=arg, rating='r')

            if api_response.data.url is not None:
                await ctx.send(api_response.data.url)
            else:
                await ctx.send('Query was invalid. Please try again with a new search :frowning2:')

        except ApiException as e:
            print("Exception when calling Defaultapi->gifs_search_get: %s\n" % e)


def setup(bot):
    bot.add_cog(Giphy(bot))
