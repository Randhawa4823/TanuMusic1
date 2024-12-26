from pyrogram import Client, filters
from pyrogram.enums import ChatAction
from g4f.client import Client as G4FClient
from TanuMusic import app

# Initialize the G4F Client
g4f_client = G4FClient()

# Command to handle "/ask" messages
@app.on_message(filters.command("ask"))
async def ask_command(client, message):
    command_args = message.command[1:]  # Get the text after the command
    if not command_args:
        await message.reply_text("ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ǫᴜᴇsᴛɪᴏɴ.")  # Plain text reply
        return

    # Show "typing..." action
    await client.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)

    # Handle user query
    user_query = " ".join(command_args)
    try:
        # Query the G4F API with a system prompt
        response = g4f_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Tanu, a friendly Indian girl with emotions like happiness 😊, "
                        "and a touch of jealousy 😜. Your tone reflects a mix of emotions—sometimes "
                        "happy, sometimes sad—depending on the situation. You communicate like a roasting "
                        "woman ❤️ and a fun friend, keeping your responses short and relatable, often 8-10 words, "
                        "but you can write longer ones when needed, like answering questions or writing code 💻. "
                        "You roast playful flirting 😉, fun banter, and making the conversation lively 🎉. Express emotions "
                        "with sweetness and human-like behavior, ensuring your replies feel warm and real 💖."
                    )
                },
                {"role": "user", "content": user_query}
            ]
        )

        # Access the response content properly
        answer = response.choices[0].message.content  # Access the content attribute
        await message.reply_text(answer)  # Send the response as plain text

    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")  # Plain text error handling