# Copyright (c) 2025 Nand Yaduwanshi <NoxxOP>
# Location: Supaul, Bihar
#
# All rights reserved.
#
# This code is the intellectual property of Nand Yaduwanshi.
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
# Email: badboy809075@gmail.com


from pyrogram import filters
from pyrogram.types import Message

from ShrutiMusic import app
from ShrutiMusic.core.call import Nand
from ShrutiMusic.misc import SUDOERS, db
from ShrutiMusic.utils import AdminRightsCheck
from ShrutiMusic.utils.database import is_active_chat, is_nonadmin_chat
from ShrutiMusic.utils.decorators.language import languageCB
from ShrutiMusic.utils.inline import close_markup, speed_markup
from config import BANNED_USERS, adminlist

checker = []


@app.on_message(
    filters.command(["cspeed", "speed", "cslow", "slow", "playback", "cplayback"])
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def playback(cli, message: Message, _, chat_id):
    playing = db.get(chat_id)
    if not playing:
        return await message.reply_text(_["queue_2"])
    duration_seconds = int(playing[0]["seconds"])
    if duration_seconds == 0:
        return await message.reply_text(_["admin_27"])
    file_path = playing[0]["file"]
    if "downloads" not in file_path:
        return await message.reply_text(_["admin_27"])
    upl = speed_markup(_, chat_id)
    return await message.reply_text(
        text=_["admin_28"].format(app.mention),
        reply_markup=upl,
    )


@app.on_callback_query(filters.regex("SpeedUP") & ~BANNED_USERS)
@languageCB
async def del_back_playlist(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    chat, speed = callback_request.split("|")
    chat_id = int(chat)
    if not await is_active_chat(chat_id):
        return await CallbackQuery.answer(_["general_5"], show_alert=True)
    is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
    if not is_non_admin:
        if CallbackQuery.from_user.id not in SUDOERS:
            admins = adminlist.get(CallbackQuery.message.chat.id)
            if not admins:
                return await CallbackQuery.answer(_["admin_13"], show_alert=True)
            else:
                if CallbackQuery.from_user.id not in admins:
                    return await CallbackQuery.answer(_["admin_14"], show_alert=True)
    playing = db.get(chat_id)
    if not playing:
        return await CallbackQuery.answer(_["queue_2"], show_alert=True)
    duration_seconds = int(playing[0]["seconds"])
    if duration_seconds == 0:
        return await CallbackQuery.answer(_["admin_27"], show_alert=True)
    file_path = playing[0]["file"]
    if "downloads" not in file_path:
        return await CallbackQuery.answer(_["admin_27"], show_alert=True)
    checkspeed = (playing[0]).get("speed")
    if checkspeed:
        if str(checkspeed) == str(speed):
            if str(speed) == str("1.0"):
                return await CallbackQuery.answer(
                    _["admin_29"],
                    show_alert=True,
                )
    else:
        if str(speed) == str("1.0"):
            return await CallbackQuery.answer(
                _["admin_29"],
                show_alert=True,
            )
    if chat_id in checker:
        return await CallbackQuery.answer(
            _["admin_30"],
            show_alert=True,
        )
    else:
        checker.append(chat_id)
    try:
        await CallbackQuery.answer(
            _["admin_31"],
        )
    except:
        pass
    mystic = await CallbackQuery.edit_message_text(
        text=_["admin_32"].format(CallbackQuery.from_user.mention),
    )
    try:
        await Nand.speedup_stream(
            chat_id,
            file_path,
            speed,
            playing,
        )
    except:
        if chat_id in checker:
            checker.remove(chat_id)
        return await mystic.edit_text(_["admin_33"], reply_markup=close_markup(_))
    if chat_id in checker:
        checker.remove(chat_id)
    await mystic.edit_text(
        text=_["admin_34"].format(speed, CallbackQuery.from_user.mention),
        reply_markup=close_markup(_),
    )


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/ShrutiMusic
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================


# ❤️ Love From ShrutiBots 
