BAN_COMMAND = {
  "name": "ban",
  "aliases": [
    'b'
  ],
  "brief": "Bans a member from a server.",
  "help": "Bans a member from a server for a given reason.",
  "description": "Bans a member from a server for a given reason.",
  "usage": "<member> <reason>"
}

KICK_COMMAND = {
  "name": "kick",
  "aliases": [
    'k'
  ],
  "brief": "Kicks a member from a server.",
  "help": "Kicks a member from a server for a given reason.",
  "description": "Kicks a member from a server for a given reason.",
  "usage": "<member> <reason>"
}

WARN_COMMAND = {
  "name": "warn",
  "aliases": [
    'w'
  ],
  "brief": "Warns a member in a server.",
  "help": "Warns a member in a server for a given reason.",
  "description": "Warns a member in a server for a given reason.",
  "usage": "<member> <reason>"
}


MUTE_COMMAND = {
  "name": "mute",
  "aliases": [
    'm'
  ],
  "brief": "Mutes a member in a server.",
  "help": "Mutes a member in a server for a given reason.",
  "description": "Mutes a member in a server for a given reason, and duration.",
  "usage": "<member> <reason> <duration>"
}

class Colour:
  RED = 0xe34e3d
