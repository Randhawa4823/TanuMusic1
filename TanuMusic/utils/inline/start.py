from pyrogram.types import InlineKeyboardButton

import config
from TanuMusic import app


def start_panel():
    buttons = [
        [
            InlineKeyboardButton(
                text="Add Me", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="Support", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel():
    buttons = [
        [
            InlineKeyboardButton(
                text="Add Me Baby",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="Owner", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="Support", url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(
                text="Help Commands", callback_data="settings_back_helper"
            ),
        ],
    ]
    return buttons