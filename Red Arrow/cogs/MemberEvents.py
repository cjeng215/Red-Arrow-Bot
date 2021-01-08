from discord.ext import commands
from time import gmtime, strftime

log_time_format = 'Time: ' + strftime("%a, %d %b %Y %H:%M:%S", gmtime())


class MemberEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # log user's entrance to server
        with open('log.txt', 'a') as f:
            f.write(f'{log_time_format}, User: {member} entered the server.\n')

        await member.send('Welcome to my discord server!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        # log user's exit from server
        with open('log.txt', 'a') as f:
            f.write(f'{log_time_format}, User: {member} exited the server.\n')

        channel = self.bot.get_channel(692282288653729845)
        await channel.send(f'cya next time {member}!')


def setup(bot):
    bot.add_cog(MemberEvents(bot))
