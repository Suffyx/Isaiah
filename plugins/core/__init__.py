from discord.ext import commands

from plugins.core.error import ErrorHandler
from plugins.core.startup import Login

def setup(bot: commands.Bot):
  """Sets up the cogs from the core module.
    
     Parameters:
        bot: discord.ext.commands.Bot - The bot the cog is loaded onto. Passed by discord.py
  """
  bot.add_cog(CommandError(bot))
  bot.add_cog(Login(bot))
