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
from discord.commands import slash_command, Option

from core import Paginator

import core.utils as utils
from core import Context

from core import Isaiah

from constants import Colour

from constants import MODLOGS_COMMAND
from constants import CASE_COMMAND
from constants import NOTE_COMMAND
from constants import NOTES_COMMAND


class MiscCommands(commands.Cog):
    """Initialize MiscCommands Cog

    Parameters:
       bot: Isaiah - The bot on which the cog is loaded. Passed by setup function in plugins/moderation/__init__.py
    """

    def __init__(self, bot: Isaiah):
        self.bot = bot

    @slash_command(MODLOGS_COMMAND)
    async def _modlogs(
        self,
        ctx,
        member: Option(discord.Member, "The member you want the modlogs of.")
    ):
        _embeds = utils.get_modlogs(member, str(ctx.guild.id), self.bot)

        if isinstance(_embeds, discord.Embed):
            return await ctx.respond(
                embed=_embeds,
                ephemeral=True
            )

        else:
            pages = Paginator(embeds, ctx, self.bot)

            await pages.send()

    @slash_command(CASE_COMMAND)
    async def _case(
        self,
        ctx,
        case: Option(int, "The case number of the case in question.")
    ):

        _embed = utils.get_case(str(ctx.guild.id), self.bot, case)

        await ctx.respond(_embed)

    @slash_command(NOTE_COMMAND)
    async def _note(
        self,
        ctx,
        user: Option(discord.Member, "The member you want to make a note on."),
        note: Option(str, "The note to be made.")
    ):

        utils.make_note(ctx, str(user.id), note, self.bot)

        await ctx.respond(f"Note made on user **{user.name}#{user.discriminator}**", ephemeral=True)


    @slash_command(NOTES_COMMAND)
    async def _notes(
        self,
        ctx,
        member: Option(discord.Member, "The member to return the notes of.")
    ):
        _embeds = utils.get_notes(member, self.bot)

        if isinstance(_embeds, discord.Embed):
            return await ctx.respond(
                embed=_embeds,
                ephemeral=True
            )

        else:
            pages = Paginator(embeds, ctx, self.bot)

            await pages.send()