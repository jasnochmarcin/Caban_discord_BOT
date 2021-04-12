from discord.ext import commands

class CabanBot(commands.Bot):
    async def on_ready(self):
        print(self.user)