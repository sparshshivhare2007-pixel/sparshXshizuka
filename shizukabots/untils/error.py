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


import traceback
from functools import wraps

from pyrogram.errors.exceptions.forbidden_403 import ChatWriteForbidden

from config import LOG_GROUP_ID
from ShrutiMusic import app


def split_limits(text):
    if len(text) < 2048:
        return [text]

    lines = text.splitlines(True)
    small_msg = ""
    result = []
    for line in lines:
        if len(small_msg) + len(line) < 2048:
            small_msg += line
        else:
            result.append(small_msg)
            small_msg = line

    result.append(small_msg)

    return result


def capture_err(func):
    @wraps(func)
    async def capture(client, message, *args, **kwargs):
        try:
            return await func(client, message, *args, **kwargs)
        except ChatWriteForbidden:
            await app.leave_chat(message.chat.id)
            return
        except Exception as err:
            errors = traceback.format_exc()
            error_feedback = split_limits(
                "**ERROR** | {} | {}\n```command\n{}```\n\n```python\n{}```\n".format(
                    0 if not message.from_user else message.from_user.mention,
                    (
                        0
                        if not message.chat
                        else (
                            f"@{message.chat.username}"
                            if message.chat.username
                            else f"`{message.chat.id}`"
                        )
                    ),
                    message.text or message.caption,
                    "".join(errors),
                ),
            )
            for x in error_feedback:
                await app.send_message(LOGGER_ID, x)
            raise err

    return capture


# ©️ Copyright Reserved - @hye_babu  sparsh baniya 

# ===========================================
# ©️ 2025 sparsh baniya  (aka @hye_babu)
# 🔗 GitHub : https://github.com/sparshshivhare2007-pixel/Sparshmusic
# 📢 Telegram Channel : https://t.me/shizuka_bots
# ===========================================


# ❤️ Love From shizukabots