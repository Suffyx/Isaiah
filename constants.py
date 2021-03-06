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
DEFAULT_DURATION = "1 minute"

BAN_COMMAND = {
    "name": "ban",
    "description": "Bans a member from a server for a given reason.",
}

KICK_COMMAND = {
    "name": "kick",
    "description": "Kicks a member from a server for a given reason.",
}

WARN_COMMAND = {
    "name": "warn",
    "description": "Warns a member in a server for a given reason.",
}


MUTE_COMMAND = {
    "name": "mute",
    "description": "Mutes a member in a server for a given reason, and duration.",
}


HELP_COMMAND = {
    "name": "help",
    "description": "Returns a list of commands or information on a specific command.",
}

MODLOGS_COMMAND = {
    "name": "modlogs",
    "description": "Returns the moderation logs for a user."
}

CASE_COMMAND = {
    "name": "case",
    "description": "Returns information on a case."
}

NOTE_COMMAND = {
    "name": "note",
    "description": "Makes a note on a user."
}

NOTES_COMMAND = {
    "name": "notes",
    "description": "Returns the notes on a user."
}

class Colour:
    RED = 0xE34E3D
    GREEN = 0x32A852
