"""
The MIT License (MIT)
Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.

Copyright (c) 2021 Suffyx Ltd
"""

import discord
from discord.ext import commands

import typing

from constants import BAN_COMMAND
from constants import DEFAULT_REASON

from core import Context

class BanException(Exception):
  def __init__(self, member: discord.Member, guild: discord.Guild):
    """Builds BanException Exception class.
    
       Parameters:
          member: discord.Member - The member that the ban failed on.
          guild: discord.Guild - The guild that the ban failed in.
    """
    self.member = member
    self.guild = guild
  
  def __repr__(self):
    return f"The ban of user {self.member.user} failed in guild {self.guild.name}"

class GeneralCommands(commands.Cog):
  """Initialize GeneralCommands Cog
     
     Parameters:
        bot: discord.ext.commands.Bot - The bot on which the cog is loaded. Passed by setup function in plugins/core/__init__.py
  """
  def __init__(self, bot: commands.Bot):
    self.bot = bot
    
  @commands.command(BAN_COMMAND)
  @commands.has_permissions(ban_members = True)
  async def _ban(self, ctx: Context, member: typing.Union[discord.Member, str], *, reason: str = None):
    """Bans a given member for a given reason
    
       Parameters:
          ctx: core.Context - The context of the command that was raised
          member: typing.Union[discord.Member, str] - The member that will be banned
          reason: str - The reason the member will be banned for. Defaults to constants.DEFAULT_REASON
    """
    if reason is None:
      reason = DEFAULT_REASON
      
    if member.id == ctx.author.id:
      await ctx.error("You cannot ban yourself.")
      
    try:
      await member.ban(reason)
    except:
      raise BanException(member, ctx.guild)
      
    
