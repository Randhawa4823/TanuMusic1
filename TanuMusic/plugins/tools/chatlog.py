import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from TanuMusic import app
from config import LOGGER_ID
from strings.image import Photos

@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)
            msg = (
                f"❖ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ #ɴᴇᴡ_ɢʀᴏᴜᴘ ❖\n\n"
                f"● ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➥ {message.chat.title}\n"
                f"● ɢʀᴏᴜᴘ ɪᴅ ➥ {message.chat.id}\n"
                f"● ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ➥ @{message.chat.username}\n"
                f"● ɢʀᴏᴜᴘ ʟɪɴᴋ ➥ {link}\n"
                f"● ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs ➥ {count}\n\n"
                f"❖ ᴀᴅᴅᴇᴅ ʙʏ ➥ {message.from_user.mention}"
            )
            await app.send_photo(
                LOGGER_ID,
                photo=random.choice(Photos),
                caption=msg,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(f"sᴇᴇ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɢʀᴏᴜᴘ", url=f"{link}")]
                ])
            )

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = (
            f"❖ <b>ʙᴏᴛ #ʟᴇғᴛ_ɢʀᴏᴜᴘ ʙʏ ᴀ ᴄʜᴜᴛɪʏᴀ</b> ❖\n\n"
            f"● ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➥ {title}\n\n"
            f"● ɢʀᴏᴜᴘ ɪᴅ ➥ {chat_id}\n\n"
            f"● ʙᴏᴛ ʀᴇᴍᴏᴠᴇᴅ ʙʏ ➥ {remove_by}\n\n"
            f"❖ ʙᴏᴛ ɴᴀᴍᴇ ➥ ˹ ᴍᴀʜᴀᴋ ꭙ ʀᴏʙᴏᴛ™ ♡゙"
        )
        await app.send_photo(
            LOGGER_ID,
            photo=random.choice(Photos),
            caption=left,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(f"ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{app.username}?startgroup=true")]
            ])
        )