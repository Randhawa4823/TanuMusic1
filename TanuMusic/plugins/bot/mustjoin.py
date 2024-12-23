import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from TanuMusic import app
from strings.image import Photos

MUST_JOIN = "C0DE_SEARCH"

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    random.choice(Photos),  # Select a random Photos from the imported list
                    caption=f"<pre>❖ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ !</pre>\n\n"
                            f"<pre>● ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ  ˹ ᴛᴀɴᴜ ꭙ ᴍᴜsɪᴄ™ ♡゙, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴀɴᴅ ʏᴏᴜ ᴊᴏɪɴᴇᴅ, ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴀʟʟ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.</pre>",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/AsuraaSupports"),
                                InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"๏ ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_ᴊᴏɪɴ ᴄʜᴀᴛ ➥ {MUST_JOIN}")