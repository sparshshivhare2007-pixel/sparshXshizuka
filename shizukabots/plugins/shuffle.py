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


import random

from pyrogram import filters
from pyrogram.types import Message

from sparshXshizuka import app
from sparshXshizuka.misc import db
from sparshXshizuka.utils.decorators import AdminRightsCheck
from sparshXshizuka.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(
    filters.command(["shuffle", "cshuffle"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def admins(Client, message: Message, _, chat_id):
    check = db.get(chat_id)
    if not check:
        return await message.reply_text(_["queue_2"])
    try:
        popped = check.pop(0)
    except:
        return await message.reply_text(_["admin_15"], reply_markup=close_markup(_))
    check = db.get(chat_id)
    if not check:
        check.insert(0, popped)
        return await message.reply_text(_["admin_15"], reply_markup=close_markup(_))
    random.shuffle(check)
    check.insert(0, popped)
    await message.reply_text(
        _["admin_16"].format(message.from_user.mention), reply_markup=close_markup(_)
    )


# ©️ Copyright Reserved - @hye_babu  sparsh baniya 

# ===========================================
# ©️ 2025 sparsh baniya  (aka @hye_babu)
# 🔗 GitHub : https://github.com/sparshshivhare2007-pixel/Sparshmusic
# 📢 Telegram Channel : https://t.me/shizuka_bots
# ===========================================


# ❤️ Love From shizukabots
