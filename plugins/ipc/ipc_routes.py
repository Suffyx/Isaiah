"""
MIT License

Copyright (c) 2021 Suffyx

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import discord
from discord.ext import commands

from core import Isaiah


class Login(commands.Cog):
    """Initialize Login Cog

    Parameters:
       bot: Isaiah - The bot on which the cog is loaded. Passed by setup function in plugins/ipc/__init__.py
    """

    def __init__(self, bot: Isaiah):
        self.bot = bot

    @ipc.server.route()
    async def get_guild_ids(self, data):
        """Returns the an array of id's pertaining to guilds that the bot is in.

        Parameters:
           data: discord.ext.ipc.IpcResponse - The request data such as arguments and json
        """
        guild_ids = []

        for guild in self.bot.guilds:
            guild_ids.append(guild.id)

        return guild_ids

    @ipc.server.route()
    async def get_guild(self, data):
        """Returns a list json object of a guild from a given id.

        Parameters:
           data: discord.ext.ipc.IpcResponse - The request data such as arguments and json
        """
        guild = self.bot.get_guild(data.guild_id)
        if guild is None:
            return None

        return {
            "name": guild.name,
            "id": guild.id,
            "prefix": __get_guild_prefix(guild.id),
            "member_count": guild.member_count,
        }

    @ipc.server.route()
    async def get_roles(self, data):
        """Gets the roles for a given guild.

        Parameters:
           data: discord.ext.ipc.IpcResponse - The request data such as arguments and json
        """
        if data.guild is None:
            return None

        guild = self.bot.get_guild(data.guild_id)
        if guild is None:
            return None

        role_ids = []

        for role in guild.roles:
            role_ids.append(role.id)

        return role_ids

    @ipc.server.route()
    async def get_role(self, data):
        """Returns information on a role of a given id in a given guild

        Parameters:
          data: discord.ext.ipc.IpcResponse - The request data such as arguments and json
        """
        if data.guild is None:
            return None

        if data.role_id is None:
            return None

        guild = self.bot.get_guild(data.guild_id)
        if guild is None:
            return None

        for role in guild.roles:
            if role.id == data.role_id:
                return {
                    "name": role.name,
                    "colour": role.color,
                    "id": role.id,  # not necessary but for purposes of mere usefulness it has been included
                }

    @ipc.server.route()
    async def get_guild_count(self, data):
        """Sets the prefix for a guild of a given ID given that the prefix is correct. Can only be sent by discord.ext.ipc.Client request from an authorized user (an Administrator within the given guild.)

        Parameters:
          data: discord.ext.ipc.IpcResponse - The request data such as arguments and json
        """
        return len(self.bot.guilds)

    @ipc.server.route()
    async def set(self, data):
        """Sets the prefix for a guild of a given ID given that the prefix is correct. Can only be sent by discord.ext.ipc.Client request from an authorized user (an Administrator within the given guild.)

        Parameters:
          data: discord.ext.ipc.IpcResponse - The request data such as arguments and json

        Data attribute "opt" options:
           prefix: str - Sets the attribute option to change the prefix of a guild
           muted_role: str - Sets the attribute option to change the muted role of a guild
           # banned_words: str - Sets the attribute option to change the banned words of a guild
           # reaction_roles: str - Sets the attribute option to add or remove the reaction roles of a guild. More information on reaction role formatting can be found at <https://Suffyx.github.io/Isaiah/reaction_roles/>
        """
        if data.opt is None:
            return None

        if data.opt == "prefix":
            if data.prefix is None or data.guild_id is None:
                return None

            utils.__set_prefix(data.prefix, data.guild_id)

            return {"status": "Success"}

        if data.opt == "muted_role":
            if data.guild_id is None or data.role_id is None:
                return None

            utils.__set_muted_role(data.role_id, data.guild_id)
