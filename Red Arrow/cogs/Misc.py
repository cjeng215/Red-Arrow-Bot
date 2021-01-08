from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        await ctx.send("""```List of commands:
        !help                   -- displays list of commands
        !clear_log              -- clears log file 
        !ping                   -- responds to channel with bot's latency to Discord 
        !giphy <subject>        -- responds to channel with gif relating to subject 
        !giphy_rand <subject>   -- responds to channel with a random gif relating to subject 
        !clear_messages         -- purges a text channel of all its messages
        !play <subject>         -- calls bot into current voice channel and plays a youtube audio
        !pause                  -- pauses bot's audio
        !resume                 -- resumes's bot's audio
        !stop                   -- stop's bot's audio and removes previous playing song
        !leave                  -- disconnect bot from the voice channel it's called from```""")

    @commands.command()
    async def clear_log(self, ctx):
        with open('log.txt', 'w'):
            pass

    @commands.command()
    async def clear_messages(self, ctx):
        await ctx.channel.purge()


def setup(bot):
    bot.add_cog(Misc(bot))
