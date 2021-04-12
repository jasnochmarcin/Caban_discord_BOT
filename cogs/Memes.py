from discord.ext import commands
import requests
from discord import Embed


class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='Meme')
    async def meme(self, ctx):
        r = requests.get('https://ivall.pl/memy')
        json_data = r.json()
        image_url = json_data['url']

        embed = Embed(title="Na życzenie losuje mema:", color=3447003)
        embed.set_image(url=image_url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"{ctx.author.name}#{ctx.author.discriminator}")

        await ctx.send(embed=embed)