from discord.ext import commands


class Ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        converted_ping_to_ms = self.bot.latency * 1000

        await ctx.send(f'My ping is: {round(converted_ping_to_ms, 4)} ms')


def setup(bot):
    bot.add_cog(Ping(bot))
