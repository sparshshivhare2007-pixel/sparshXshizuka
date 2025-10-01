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


from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_GROUP


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_9"], url=SUPPORT_GROUP),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl


def supp_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["S_B_9"],
                    url=SUPPORT_GROUP,
                ),
            ]
        ]
    )
    return upl


# ©️ Copyright Reserved - @hye_babu  sparsh baniya 

# ===========================================
# ©️ 2025 sparsh baniya  (aka @hye_babu)
# 🔗 GitHub : https://github.com/sparshshivhare2007-pixel/Sparshmusic
# 📢 Telegram Channel : https://t.me/shizuka_bots
# ===========================================


# ❤️ Love From shizukabots
