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

import core.utils as utils
from core import Context

from core import Isaiah

from constants import COLOUR_COMMAND


class Misc(commands.Cog):
    """Initialize MiscCommands Cog
    Parameters:
       bot: Isaiah - The bot on which the cog is loaded. Passed by setup function in plugins/moderation/__init__.py
    """

    def __init__(self, bot: Isaiah):
        self.bot = bot
        
    @slash_command(COLOUR_COMMAND)
    async def _coloUr(
        self,
        ctx,
        color: Option(str, "The color (in hexadeximal) that you want to display.")
    ):
      
        pythonized_color = color.replace("#", "0x")
        
        color_int = int(color, base=16)
        
        
