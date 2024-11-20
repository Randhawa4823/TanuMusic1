import requests
from pyrogram import filters
from TanuMusic import app 

@app.on_message(filters.command("ask"))
def search_api(client, message):
    # Check if the user provided a query
    query = " ".join(message.command[1:]) if len(message.command) > 1 else None
    if not query:
        # Prompt the user for a query if none is provided
        return message.reply_text("ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ǫᴜᴇʀʏ ᴛᴏ ᴀsᴋ.")
    
    try:
        # Send request to the search API
        url = f"https://search.codesearch.workers.dev/?query={query}"
        response = requests.get(url).json()
        results = response.get("results", [])

        # Send only the search results
        if results:
            message.reply_text("\n".join(results))  # Send results as plain text
        else:
            message.reply_text("ɴᴏᴛ ʀᴇsᴘᴏɴsᴇ ғᴏᴜɴᴅ ғᴏʀᴍ ᴀᴘɪ.")
    except Exception as e:
        message.reply_text(f"An error occurred: {str(e)}")