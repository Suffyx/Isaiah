from plugins.ipc.ipc_routes import IPCRoutes
from core import Isaiah


def setup(bot: Isaiah):
    """Sets up the cogs from the core module.

    Parameters:
       bot: core.Isaiah - The bot the cog is loaded onto. Passed by discord.py
    """
    bot.add_cog(IPCRoutes(bot))
