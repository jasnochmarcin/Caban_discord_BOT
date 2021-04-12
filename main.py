from os import environ
from CabanBot import CabanBot
from dotenv import load_dotenv
from cogs.Greetings import Greetings
from cogs.Memes import Memes

load_dotenv()
DISCORD_TOKEN = environ.get('DISCORD_TOKEN')


bot = CabanBot(command_prefix='$')
bot.add_cog(Greetings(bot))
bot.add_cog(Memes(bot))
bot.run(DISCORD_TOKEN)
