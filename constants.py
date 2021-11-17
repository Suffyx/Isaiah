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

DEFAULT_REASON = "violating the rules or guidelines."

BAN_COMMAND = {
    "name": "ban",
    "aliases": ["b"],
    "brief": "Bans a member from a server.",
    "help": "Bans a member from a server for a given reason.",
    "description": "Bans a member from a server for a given reason.",
    "usage": "<member> <reason>",
}

KICK_COMMAND = {
    "name": "kick",
    "aliases": ["k"],
    "brief": "Kicks a member from a server.",
    "help": "Kicks a member from a server for a given reason.",
    "description": "Kicks a member from a server for a given reason.",
    "usage": "<member> <reason>",
}

WARN_COMMAND = {
    "name": "warn",
    "aliases": ["w"],
    "brief": "Warns a member in a server.",
    "help": "Warns a member in a server for a given reason.",
    "description": "Warns a member in a server for a given reason.",
    "usage": "<member> <reason>",
}


MUTE_COMMAND = {
    "name": "mute",
    "aliases": ["m"],
    "brief": "Mutes a member in a server.",
    "help": "Mutes a member in a server for a given reason.",
    "description": "Mutes a member in a server for a given reason, and duration.",
    "usage": "<member> <reason> <duration>",
}


HELP_COMMAND = {
    "name": "help",
    "aliases": ["h"],
    "brief": "Returns a list of commands.",
    "help": "Returns a list of commands or information on a specific command.",
    "description": "Returns a list of commands or information on a specific command.",
    "usage": "<command: optional>"
}

class Colour:
    RED = 0xE34E3D
