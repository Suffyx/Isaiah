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

import typing
import asyncio

import discord
from discord.ext import commands

from durations import Duration

import core.utils as utils
from core import Context

from core import Isaiah

from constants import BAN_COMMAND
from constants import KICK_COMMAND
from constants import WARN_COMMAND
from constants import MUTE_COMMAND

from constants import DEFAULT_REASON
from constants import Colour


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


class KickException(Exception):
    def __init__(self, member: discord.Member, guild: discord.Guild):
        """Builds KickException Exception class.

        Parameters:
           member: discord.Member - The member that the kick failed on.
           guild: discord.Guild - The guild that the kick failed in.
        """
        self.member = member
        self.guild = guild

    def __repr__(self):
        return f"The kick of user {self.member.user} failed in guild {self.guild.name}"


class MuteException(Exception):
    def __init__(self, member: discord.Member, guild: discord.Guild):
        """Builds MuteException Exception class.

        Parameters:
           member: discord.Member - The member that the mute failed on.
           guild: discord.Guild - The guild that the mute failed in.
        """
        self.member = member
        self.guild = guild

    def __repr__(self):
        return f"The mute of user {self.member.user} failed in guild {self.guild.name}"


class GeneralCommands(commands.Cog):
    """Initialize GeneralCommands Cog

    Parameters:
       bot: Isaiah - The bot on which the cog is loaded. Passed by setup function in plugins/moderation/__init__.py
    """

    def __init__(self, bot: Isaiah):
        self.bot = bot

    @commands.command(BAN_COMMAND)
    @commands.has_permissions(ban_members=True)
    async def _ban(
        self,
        ctx: Context,
        member: typing.Union[discord.Member, str],
        *,
        reason: str = None,
    ):
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

        id = utils.add_ban(member, ctx, self.bot)

        await ctx.send(
            embed=discord.Embed(
                description=f"**{member.user}** banned successfully.", color=Colour.RED
            )
        )

        await member.send(
            embed=discord.Embed(
                description=f"You've been banned from **{ctx.guild.name}** for **{reason}**",
                color=Colour.RED,
            )
        )

    @commands.command(KICK_COMMAND)
    @commands.has_permissions(kick_members=True)
    async def _kick(
        self,
        ctx: Context,
        member: typing.Union[discord.Member, str],
        *,
        reason: str = None,
    ):
        """Kicks a given member for a given reason

        Parameters:
           ctx: core.Context - The context of the command that was raised
           member: typing.Union[discord.Member, str] - The member that will be kicked
           reason: str - The reason the member will be kicked for. Defaults to constants.DEFAULT_REASON
        """
        if reason is None:
            reason = DEFAULT_REASON

        if member.id == ctx.author.id:
            await ctx.error("You cannot kick yourself.")

        try:
            await member.kick(reason)
        except:
            raise KickException(member, ctx.guild)

        id = utils.add_kick(member, ctx)

        await ctx.send(
            embed=discord.Embed(
                description=f"**{member.user}** kicked successfully.", color=Colour.RED
            )
        )

        await member.send(
            embed=discord.Embed(
                description=f"You've been kicked from **{ctx.guild.name}** for **{reason}**",
                color=Colour.RED,
            )
        )

    @commands.command(WARN_COMMAND)
    @commands.has_permissions(manage_messages=True)
    async def _warn(
        self,
        ctx: Context,
        member: typing.Union[discord.Member, str],
        *,
        reason: str = None,
    ):
        """Warns a given member for a given reason

        Parameters:
           ctx: core.Context - The context of the command that was raised
           member: typing.Union[discord.Member, str] - The member that will be warned
           reason: str - The reason the member will be warned for. Defaults to constants.DEFAULT_REASON
        """
        if reason is None:
            reason = DEFAULT_REASON

        if member.id == ctx.author.id:
            await ctx.error("You cannot warn yourself.")

        id = utils.add_warn(member, ctx)

        await ctx.send(
            embed=discord.Embed(
                description=f"**{member.user}** warned successfully.", color=Colour.RED
            )
        )

        await member.send(
            embed=discord.Embed(
                description=f"You've been kicked in **{ctx.guild}** for **{reason}**",
                color=Colour.RED,
            )
        )

    @commands.command(MUTE_COMMAND)
    @commands.has_permissions(kick_members=True)
    async def _mute(
        self,
        ctx: Context,
        member: typing.Union[discord.Member, str],
        duration: str = None,
        *,
        reason: str = None,
    ):
        """Kicks a given member for a given reason

        Parameters:
           ctx: core.Context - The context of the command that was raised
           member: typing.Union[discord.Member, str] - The member that will be muted
           reason: str - The reason the member will be muted for. Defaults to constants.DEFAULT_REASON
           duration: str - The duration that the member will be muted for. Defaults to Isaiah.config.DEFAULT_DURATION
        """
        if reason is None:
            reason = DEFAULT_REASON

        if duration is None:
            duration = self.bot.config.DEFAULT_DURATION

        if member.id == ctx.author.id:
            await ctx.error("You cannot mute yourself.")

        muted_role = utils.get_muted_role(ctx)

        try:
            await member.add_roles(muted_role)
        except:
            raise MuteException(member, ctx.guild)

        id = utils.add_mute(member, ctx)

        await asyncio.sleep(Duration(duration).to_seconds())

        await ctx.send(
            embed=discord.Embed(
                description=f"**{member.user}** muted successfully.", color=Colour.RED
            )
        )
        
        await member.send(
            embed=discord.Embed(
                description=f"You've been muted in {ctx.guild} for {reason}. You will be unmuted in {duration}",
                color=Colour.RED,
            )
        )
        
#        if member.name.lower().endswith("s") === False:
#          name = member.name+"'s" 
#        else:
#          name = member.name+"'"
