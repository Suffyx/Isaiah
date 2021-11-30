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

from discord.ui import Button, View

class Paginator():
    def __init__(pages, ctx, bot, ephemeral=False, timeout=60):
        self.index = 0
        self.pages = pages
        self.ctx = ctx
        self.bot=bot

        self.message = None

        next = Button(label = "Next", style = discord.ButtonStyle.green, emoji = "➡️", custom_id = "next")
        back = Button(label = "Back", style = discord.ButtonStyle.red, emoji="⬅️", custom_id = "back")
        close = Button(label = "Close", style = discord.ButtonStyle.gray, emoji="🔒", custom_id = "close")

        self.view = View(timeout=timeout)
        self.view.add_item(next)
        self.view.add_item(back)
        self.view.add_item(close)

    async def send(self):
        message = await self.ctx.respond(
            embed = self.pages[self.index],
            view = self.view,
            ephemeral = True if self.ephemeral else False
        )

        self.message = message

    async def next_page(self, interaction):
        self.index += 1 if self.index <= len(pages) - 1 else 0
        await self.message.edit(
            embed = self.pages[self.index],
            view=self.view
        )

    async def prev_page(self, interaction):
        self.index -= 1 if self.index >= 0 else len(self.pages) - 1
        await self.message.edit(
            embed = self.pages[self.index],
            view=self.view
        )

    async def close(self, interaction):
        next = Button(label = "Next", style = discord.ButtonStyle.green, emoji = "➡️", custom_id = "next", disabled=True)
        back = Button(label = "Back", style = discord.ButtonStyle.red, emoji="⬅️", custom_id = "back", disabled=True)
        close = Button(label = "Close", style = discord.ButtonStyle.gray, emoji="🔒", custom_id = "close", disabled=True)

        view = View()
        view.add_item(next)
        view.add_item(back)
        view.add_item(close)  

        await self.message.edit(
            view=view
        )    
