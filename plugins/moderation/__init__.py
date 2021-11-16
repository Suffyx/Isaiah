from core import Isaiah

from plugins.moderation.general import GeneralCommands
from plugins.moderation.misc import MiscCommands

def setup(bot: Isaiah):
  """Sets up the cogs from the core module.
    
     Parameters:
        bot: Isaiah - The bot the cog is loaded onto. Passed by discord.py
  """
  bot.add_cog(GeneralCommands(bot))
  bot.add_cog(MiscCommands(bot))
