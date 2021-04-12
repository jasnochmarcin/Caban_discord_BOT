from os import environ
from CabanBot import CabanBot
from dotenv import load_dotenv
from commands.hello import hello

load_dotenv()
DISCORD_TOKEN = environ.get('DISCORD_TOKEN')


bot = CabanBot(command_prefix='$')
bot.add_command(hello)
bot.run(DISCORD_TOKEN)