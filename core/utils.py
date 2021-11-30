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
from .Context import Context
from .Isaiah import Isaiah

from typing import Callable

def func_check(check: bool, function: Callable, *args, **kwargs):
    """Runs a function if a given check is valid.

    Parameters:
       check: bool - What is checked before the function is run
       function: Callable - The function run if the check is True
    """
    if check:
        function(args, kwargs)


def add_guild_to_db(guild_id: str, bot: Isaiah):
    """Adds a guild to the guilds database

    Parameters:
       guild_id: str - The guild you would like to check
       bot: Isaiah - The bot itself
    """
    bot.db['guilds'][str(guild_id)] = {}
    bot.db['guilds'][str(guild_id)]['cases'] = {}
    bot.db['guilds'][str(guild_id)]['case_num'] = 0

    bot.dump("guilds")
    return

def add_user_to_db(user_id: str, bot: Isaiah):
    """Adds a user to the users database

    Parameters:
       user_id: str - The user you would like to check
       bot: Isaiah - The bot itself
    """
    bot.db['users'][str(user_id)] = {}
    bot.db['users'][str(user_id)]['notes'] = {}
    bot.db['users'][str(user_id)]['note_id'] = 1

    bot.dump("users")
    return

def user_database_check(user_id: str, bot: Isaiah):
    """Checks if a guild is registered for the user's database.

    Parameters:
       user_id: str - The user you would like to check
       bot: Isaiah - The bot itself
    """
    func_check(
        str(user_id) not in bot.db["guilds"], add_user_to_db, user_id, bot
    )

    bot.dump("guilds")

def database_check(guild_id: str, bot: Isaiah):
    """Checks if a guild is registered for the guild's database.

    Parameters:
       guild_id: str - The guild you would like to check
       bot: Isaiah - The bot itself
    """
    func_check(
        str(guild_id) not in bot.db["guilds"], add_guild_to_db, guild_id, bot
    )

    bot.dump("guilds")


def add_ban(member: discord.Member, ctx: Context, bot: Isaiah):
    """Adds a ban to the database for a member.

    Parameters:
       member: discord.Member - The member who the ban will be added to.
       ctx: Context - The context of the ban command
       bot: Isaiah - The bot itself
    """

    database_check(str(ctx.guild.id), bot)

    bot.db['guilds'][str(ctx.guild.id)]['case_num'] += 1
    case_num = bot.db['guilds'][str(ctx.guild.id)]['case_num']

    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)] = {}
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['type'] = "ban"

    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['member'] = {}
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['member']['name'] = member.user
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['member']['id'] = member.id

    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['guild'] = {}
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['guild']['name'] = ctx.guild.name
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['guild']['id'] = ctx.guild.id

    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['author'] = {}
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['author']['name'] = ctx.author.user
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['id'] = ctx.author.id

    bot.dump("guilds")


def add_kick(member: discord.Member, ctx: Context, bot: Isaiah):
    """Adds a kick to the database for a member.

    Parameters:
       member: discord.Member - The member who the kick will be added to.
       ctx: Context - The context of the kick command
       bot: Isaiah - The bot itself
    """

    database_check(str(ctx.guild.id), bot)

    bot.db['guilds'][str(ctx.guild.id)]['case_num'] += 1
    case_num = bot.db['guilds'][str(ctx.guild.id)]['case_num']

    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)] = {}
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['type'] = "kick"

    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['member'] = {}
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['member']['name'] = member.user
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['member']['id'] = member.id

    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['guild'] = {}
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['guild']['name'] = ctx.guild.name
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['guild']['id'] = ctx.guild.id

    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['author'] = {}
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['author']['name'] = ctx.author.user
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['id'] = ctx.author.id

    bot.dump("guilds")


def add_warn(member: discord.Member, ctx: Context, bot: Isaiah):
    """Adds a warn to the database for a member.

    Parameters:
       member: discord.Member - The member who the warn will be added to.
       ctx: Context - The context of the warn command
       bot: Isaiah - The bot itself
    """

    database_check(str(ctx.guild.id), bot)

    bot.db['guilds'][str(ctx.guild.id)]['case_num'] += 1
    case_num = bot.db['guilds'][str(ctx.guild.id)]['case_num']

    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)] = {}
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['type'] = "warn"

    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['member'] = {}
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['member']['name'] = member.user
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['member']['id'] = member.id

    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['guild'] = {}
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['guild']['name'] = ctx.guild.name
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['guild']['id'] = ctx.guild.id

    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['author'] = {}
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['author']['name'] = ctx.author.user
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['id'] = ctx.author.id

    bot.dump("guilds")


def add_mute(member: discord.Member, ctx: Context, duration: str, bot: Isaiah):
    """Adds a mute to the database for a member.

    Parameters:
       member: discord.Member - The member who the mute will be added to.
       ctx: Context - The context of the mute command
       duration: str - The duration of the mute
       bot: Isaiah - The bot itself
    """

    database_check(str(ctx.guild.id), bot)

    bot.db['guilds'][str(ctx.guild.id)]['case_num'] += 1
    case_num = bot.db['guilds'][str(ctx.guild.id)]['case_num']

    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)] = {}
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['type'] = "mute"

    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['member'] = {}
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['member']['name'] = member.user
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['member']['id'] = member.id

    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['guild'] = {}
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['guild']['name'] = ctx.guild.name
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['guild']['id'] = ctx.guild.id

    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['author'] = {}
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['author']['name'] = ctx.author.user
    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['author']['id'] = ctx.author.id

    bot.db['guilds'][str(ctx.guild.id)]['cases'][str(case_num)]['duration'] = duration

    bot.dump("guilds")


def add_prefix_to_db(guild_id: str, bot: Isaiah):
    """Adds a guild to the prefixes database

    Parameters:
       guild_id: str - The guild you would like to add
       bot: Isaiah - The bot itself
    """

    db["prefixes"][guild_id] = bot.default_prefix

    bot.dump("prefixes")


def prefix_check(guild_id: str, bot: Isaiah):
    """Checks if a guild is registered for the guild's database.

    Parameters:
       guild_id: str - The guild you would like to check
       bot: Isaiah - The bot itself
    """

    func_check(
        str(guild.id) not in bot.db["prefixes"], add_prefix_to_db, guild_id, bot
    )


def set_prefix(prefix: str, guild_id: str, bot: Isaiah):
    """Sets the prefix for a given guild

    Parameters:
       prefix: str - The new prefix for the guild.
       guild_id: str - The guild you want the prefix to change for
       bot: Isaiah - The bot itself
    """
    prefix_check(str(ctx.guild.id), bot)

    db["prefixes"][str(ctx.guild.id)] = prefix

    bot.dump("prefixes")


def set_muted_role(muted_role_id: str, guild_id: str, bot: Isaiah):
    """Sets the muted role for a guild.

    Parameters:
       muted_role_id: str - The new id for the muted role
       guild_id: str - The guild that the new muted role will be set in
       bot: Isaiah - The bot itself
    """

    database_check(str(guild_id), bot)

    self.bot.db["guilds"]["muted_role"] = muted_role_id
    bot.dump("guilds")

async def get_muted_role(ctx: Context, bot: Isaiah):
    """Gets the muted role for a guild.

    Parameters:
       ctx: Context - The context for the mute command
       bot: Isaiah - The bot itself
    """

    database_check(str(guild_id), bot)

    if 'muted_role' not in self.bot.db['guilds'][str(ctx.guild.id)]:
        role = await ctx.guild.create_role("Muted")
        self.bot.db['guilds'][str(ctx.guild.id)]['muted_role'] = str(role.id)

    role_id = self.bot.db['guilds'][str(ctx.guild.id)]['muted_role']

    bot.dump("guilds")
    return role_id

def get_modlogs(member: discord.Member, guild_id: str, bot: Isaiah):
    database_check(str(guild_id), bot)

    embeds = []

    embed = discord.Embed(
    ).set_footer(text=f"Modlogs for {member.name}#{member.discriminator} - {member.id}")

    for _case in self.bot.db['guilds'][str(guild_id)]['cases']:
        if self.bot.db['guilds'][str(guild_id)]['cases'][_case]['author']['id'] == str(member.id):
            case = self.bot.db['guilds'][str(guild_id)]['cases'][_case]

            value_str = f"**Type**: {case['type']}"  + f"**User**: {member.name}" + f"\t**Moderator**: {case['author']['name']}" + f"**Reason**: {case['reason']}"

            if case['type'] == 'mute':
                value_str += f"\n**Length**: {case['duration']}"

            embed.add_field(
                name = f"Case {_case}",
                value = value_str,
                inline=False
            )

            if len(embed.fields) > 10:
                embeds.append(embed)
                
                embed = discord.Embed(
                ).set_footer(text=f"Modlogs for {member.name}#{member.discriminator} - {member.id}")


    return embeds if len(embeds) > 1 else embeds[0]


async def set_banned_words(banned_words: list, guild_id: str, bot: Isaiah):
    """Sets the banned words in a guild.
    
    Parameters:
       banned_words: list - The list of banned terms.
       guild_id: str - The guild that the list will affect.
       bot: Isaiah - The bot itself  .   
    """
    database_check(str(guild_id), bot)

    self.bot.db['guilds'][str(ctx.guild.id)]['banned_words'] = banned_words

    bot.dump("guilds")

def get_case(guild_id: str, bot, _case: int):
    database_check(str(guild_id), bot)
    case = self.bot.db['guilds'][str(guild_id)]['cases'][_case]

    value_str = f"**Type**: {case['type']}"  + f"**User**: {member.name}" + f"\t**Moderator**: {case['author']['name']}" + f"**Reason**: {case['reason']}"

    if case['type'] == 'mute':
        value_str += f"\n**Length**: {case['duration']}"

    return discord.Embed(
        title = f"Case {_case}",
        description=value_str,
        color=discord.Colour.green()
    )

def make_note(ctx, user_id: str, note: str, bot):
    user_database_check(str(user_id), bot)

    note_id = self.bot.db["users"][user_id]['note_id'] + 1 if self.bot.db["users"][user_id]['note_id'] > 0 else 1
    self.bot.db["users"][user_id]['note_id'] = note_id

    self.bot.db["users"][user_id]['notes'][note_id] = {}
    self.bot.db["users"][user_id]['notes'][note_id]['author'] = {}
    self.bot.db["users"][user_id]['notes'][note_id]['author']['id'] = ctx.author.id
    self.bot.db["users"][user_id]['notes'][note_id]['author']['name'] = ctx.author.name
    self.bot.db["users"][user_id]['notes'][note_id]['content'] = note

    bot.dump("users")

def get_notes(member: discord.Member, bot):
    database_check(str(member.id), bot)

    embeds = []

    embed = discord.Embed(
    ).set_footer(text=f"Notes for {member.name}#{member.discriminator} - {member.id}")

    for _note in self.bot.db["users"][str(member.id)]:
        note = self.bot.db["users"][str(member.id)][_note]

        value_str = f"**Note**: {note['content']}\n" + f"\t**Author**: {note['author']['name']} - {note['author']['id']}"

        embed.add_field(name=f"Note {_note}", value=value_str, inline=False)

        if len(embed.fields) > 10:
            embeds.append(embed)
            
            embed = discord.Embed(
            ).set_footer(text=f"Notes for {member.name}#{member.discriminator} - {member.id}")


    return embeds if len(embeds) > 1 else embeds[0]