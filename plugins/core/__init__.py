from core import Isaiah

from plugins.core.error import ErrorHandler
from plugins.core.startup import Login

def setup(bot: Isaiah):
  """Sets up the cogs from the core module.
    
     Parameters:
        bot: core.Isaiah - The bot the cog is loaded onto. Passed by discord.py
  """
  bot.add_cog(ErrorHandler(bot))
  bot.add_cog(Login(bot))
