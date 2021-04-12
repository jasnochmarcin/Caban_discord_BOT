from discord.ext import commands

@commands.command()
async def hello(ctx):
    print('TEST')
    await ctx.send('Hello')