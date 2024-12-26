import aiohttp
from pyrogram import Client, filters
from pyrogram.enums import ChatAction
from TanuMusic import app 

@app.on_message(filters.command("ask") & filters.group)
async def fetch_med_info(client, message):
    query = " ".join(message.command[1:])  # Extract the query after the command
    if not query:
        await message.reply_text(
            "*Error:* Please provide a query to ask.", 
            parse_mode="markdown"
        )
        return

    # Send typing action to indicate bot is working
    await client.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)

    # Use the API to get medical data
    api_url = f"https://chatwithai.codesearch.workers.dev/?question={query}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as response:
                if response.status == 200:
                    data = await response.json()
                    reply = data.get("data", "Sorry, I couldn't fetch the data.")
                    formatted_reply = f"*Success:* {reply}"
                else:
                    formatted_reply = "*Error:* Failed to fetch data from the API."
    except Exception as e:
        formatted_reply = f"*Error:* An error occurred: `{e}`"

    # Reply to the user
    await message.reply_text(formatted_reply, parse_mode="markdown")