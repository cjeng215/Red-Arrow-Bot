from discord.ext import commands
from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from discord.utils import get
from discord import FFmpegPCMAudio

import os
import discord
import youtube_dl

load_dotenv()


def download_music_from_youtube(url):
    # EMBEDDING YOUTUBE-DL
    # https://github.com/ytdl-org/youtube-dl/blob/master/README.md#format-selection
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


class BotVoice(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.YOUTUBE_TOKEN = os.getenv('YOUTUBE_TOKEN')

    @commands.command()
    async def play(self, ctx, *, arg):

        song = os.path.isfile('[PATH]song.mp3')
        try:
            if song:
                os.remove('.[PATH]song.mp3')
        except PermissionError:
            await ctx.send('Music is currently being played (no queue) or use "stop" command')
            return

        vc = get(ctx.guild.voice_channels, name='General')

        try:
            await ctx.send(f'Red Arrow Bot connected to {vc}')
            await vc.connect()
        except discord.ClientException:
            await ctx.send("Already in a voice channel")
            await ctx.send(f'Playing next song in {vc}')

        # this can only be called if the bot voice already exists, otherwise it returns Nonetype
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        arg = arg.replace(' ', '+')
        url = self.get_url(arg)
        download_music_from_youtube(url)

        # move download youtube song to correct directory
        for file in os.listdir('./'):
            if file.endswith(".mp3"):
                d1 = 'PATH' + file
                d2 = 'PATH'
                os.rename(d1, d2)

        voice.play(FFmpegPCMAudio("./cogs/song.mp3"))

    # get youtube url from youtube's search api
    def get_url(self, arg):
        api_instance = build('youtube', 'v3', developerKey=self.YOUTUBE_TOKEN)
        url = ''
        try:
            youtube = api_instance.search().list(
                q=arg,
                part="id",
                maxResults=3)
            response = youtube.execute()

            url = 'https://www.youtube.com/watch?v=' + response['items'][0]['id']['videoId']

        except HttpError as e:
            print('Error response status code : {0}, reason : {1}'.format(e.resp.status, e.error_details))

        return url

    @commands.command()
    async def pause(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("Audio is paused")

    @commands.command()
    async def resume(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("Audio is resumed")

    @commands.command()
    async def leave(self, ctx):
        vc = get(ctx.guild.voice_channels, name='General')
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice.is_connected():
            await ctx.send(f"Bot is disconnecting from voice channel{vc}")
            await voice.disconnect()

    @commands.command()
    async def stop(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        voice.stop()


def setup(bot):
    bot.add_cog(BotVoice(bot))
