
# Copyright (c) 2025 sparsh baniya <baniya>
# Location: agra, up 
#
# All rights reserved.
#
# This code is the intellectual property of sparsh baniya.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: sparshshivhare20007@gmail.com


from SparshXshizuka.core.bot import sparsh
from SparshXshizuka.core.dir import dirr
from SparshXshizuka.core.git import git
from SparshXshizuka.core.userbot import Userbot
from SparshXshizuka.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Nand()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()


