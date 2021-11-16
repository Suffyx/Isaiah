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

Copyright (c) 2021 Suffyx Ltd.
"""

import discord
from discord.ext import commands

import shelve
import json
import os

from utils import __recursive_object_builder
# from utils import __build_database

class Isaiah(commands.AutoShardedBot):
  """Build and run base Isaiah class.
  
     Child of `discord.ext.commands.AutoShardedBot`
  """
  def __init__(self, *args, **kwargs):
    super().__init__(
      command_prefix = self.__get_prefix,
      intents = discord.Intents.all(),
      strip_after_prefix = True,
      case_insensitive = True,
      chunk_guild_at_startup = False,
      activity = discord.Activity(type=discord.ActivityType.listening, name="-help | -setup"),
      case_insensitive = True,
      *args,
      **kwargs
    )
    
    self.__default_prefix = self.config.DEFAULT_PREFIX
    
    self.__config_state = False
    self.__config = None

    self.db = {
      "prefixes": shelve.open(self.config.PREFIX_TABLE_PATH),
      "guilds": shelve.open(self.config.GUILD_TABLE_PATH),
      "users": shelve.open(self.config.USER_TABLE_PATH)
    }
    
    # makes sure that the database has all necessary attributes to run the bot properly
#     __build_database(self.db)

    for ext in self.config.EXTENSIONS:
      await self.load_extension(ext)

  @property
  def config(self):
    """Build and return config.json as an object."""
    # returns config object that has already been loaded if it has been loaded in the past
    if self.__config_state:
      return self.__config
    with open(os.getenv("CONFIG_PATH")) as f:
      config_obj = __recursive_object_builder(json.load(f))

    self.__config_state = True
    self.__config = config_obj
    return config_obj

  def __get_prefix(self, message: discord.Message):
    """Returns a guild's set prefix or the default prefix.
    
       Parameters:
          message: discord.Message - The context message for the prefix.
    """
    if not message.guild:
      return self.__default_prefix
    
    elif str(message.guild.id) not in self.db['prefixes']:
      return self.__default_prefix
    
    else:
      return self.db['prefixes'][str(message.guild.id)]
