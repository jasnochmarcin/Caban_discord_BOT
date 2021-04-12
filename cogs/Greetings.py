from discord.ext import commands


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='Hello')
    async def hello(self, ctx):
        await ctx.send('Hello my friend')

    @commands.command(name='Cześć')
    async def hello(self, ctx):
        await ctx.send('Witam serdecznie')