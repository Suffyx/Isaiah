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

from constants import HELP_COMMAND


class HelpCommand(commands.Cog):
    """Initialize HelpCommand Cog

    Parameters:
       bot: core.Isaiah - The bot on which the cog is loaded. Passed by setup function in plugins/core/__init__.py
    """

    def __init__(self, bot: Isaiah):
        self.bot = bot

    @commands.command(HELP_COMMAND)
    async def _help(self, ctx, command: str = None):
        """Returns a list of commands or information on a single command.]

        Parameters:
           command: str - The command you want information on.
        """
        prefix = self.bot.config.DEFAULT_PREFIX
        if command == None:
            embed_array = []
            for cog in self.bot.cogs:
                cog = self.bot.get_cog(cog)
                if len(cog.get_commands()) < 1:
                    continue

                try:
                    cog_name = cog.name
                except AttributeError:
                    cog_name = type(cog).__name__ + " Category:"

                embed = discord.Embed(
                    title=cog_name, color=discord.Colour.dark_blue()
                ).set_footer(
                    text="For more information on a specific command run {}help <command>".format(
                        prefix
                    )
                )
                # iterate through commands
                for command in cog.get_commands():
                    embed.add_field(
                        name=f"**{command.name}**", value=command.brief, inline=False
                    )
                embed_array.append(embed)
            paginator = DiscordUtils.Pagination.AutoEmbedPaginator(ctx)
            await paginator.run(embed_array)
        else:
            commands = {}
            for command_obj in self.bot.commands:
                commands[command_obj.name] = command_obj
                for alias in command_obj.aliases:
                    commands[alias] = command_obj
            if command.lower() not in commands:
                raise InvalidCommandError(command)
            else:
                command_obj = commands[command.lower()]
                await ctx.send(
                    embed=discord.Embed(
                        color=discord.Colour.green(),
                        description=command_obj.description,
                    )
                    .set_author(name=command_obj.name)
                    .add_field(
                        name="Usage:",
                        value="{0}{1}{2} {3}".format(
                            prefix,
                            command_obj.name,
                            command_obj.aliases,
                            command_obj.usage,
                        ),
                        inline=False,
                    )
                )
