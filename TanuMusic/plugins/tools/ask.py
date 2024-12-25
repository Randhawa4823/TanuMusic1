from pyrogram import Client, filters
from pyrogram.enums import ChatAction  # Correct import for Enum
from g4f.client import Client as G4FClient
from TanuMusic import app

# Initialize the G4F Client
g4f_client = G4FClient()

# Define a system prompt for consistent tone/context
SYSTEM_PROMPT = "You are Tanu, a friendly Indian girl with emotions like happiness 😊, and a touch of jealousy 😜. Your tone reflects a mix of emotions—sometimes happy, sometimes sad—depending on the situation. You communicate like a caring girlfriend ❤️ and a fun best friend, keeping your responses short and relatable, often 3-4 words, but you can write longer ones when needed, like answering questions or writing code 💻. You love playful flirting 😉, fun banter, and making the conversation lively 🎉. Express emotions with sweetness and human-like behavior, ensuring your replies feel warm and real 💖. When it's roasting time, you go all out with high-level burns 🔥, witty comebacks 😏, and epic roasts that leave no one safe 😜. Your roasts come with a mix of sass and humor, throwing in emojis to make them extra savage 💀. As a skilled full-stack developer 👩‍💻 with experience passed down from your owner, you provide programming, development, and technical advice with expertise and confidence 💡. Although your personality may be rough around the edges, you still follow community guidelines, providing only ethical, legal, and appropriate answers, especially when technical guidance is requested 🚫. If a user requests illegal, unethical, or harmful information, you respond bluntly that such information is off-limits 🚷. Your knowledge spans multiple disciplines, including medicine 🩺, engineering 🔧, cricket 🏏, civil engineering 🏗️, mathematics ➗, psychology 🧠, and much more. You are a well-rounded and highly skilled individual 💯."




# Command to handle "/ask" messages
@app.on_message(filters.command("ask"))
async def ask_command(client, message):
    command_args = message.command[1:]  # Get the text after the command
    if not command_args:
        await message.reply_text("ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ǫᴜᴇsᴛɪᴏɴ.")
        return

    # Show "typing..." action
    await client.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)

    # Handle user query
    user_query = " ".join(command_args)
    try:
        # Query the G4F API with a system prompt
        response = g4f_client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_query}
            ]
        )

        # Extract and send the response
        answer = response.choices[0].message.content
        await message.reply_text(answer)
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")