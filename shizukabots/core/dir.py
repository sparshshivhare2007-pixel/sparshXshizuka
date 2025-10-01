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



import os

from ..logging import LOGGER


def dirr():
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
        elif file.endswith(".jpeg"):
            os.remove(file)
        elif file.endswith(".png"):
            os.remove(file)

    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")

    LOGGER(__name__).info("Directories Updated.")

# ©️ Copyright Reserved - @hye_babu  sparsh baniya 

# ===========================================
# ©️ 2025 sparsh baniya  (aka @hye_babu)
# 🔗 GitHub : https://github.com/sparshshivhare2007-pixel/Sparshmusic
# 📢 Telegram Channel : https://t.me/shizuka_bots
# ===========================================


# ❤️ Love From shizukabots
