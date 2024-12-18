import re
import json
import io
from pyrogram import filters
from pyrogram.types import Message
from TanuMusic import app
from config import OWNER_ID, MONGO_DB_URI
from TanuMusic.misc import SUDOERS
from TanuMusic.utils.pastebin import Bin
from TanuMusic.utils.database import (
    delete_collection,
    delete_database,
    list_databases,
    delete_all_databases,
    backup_database,
    restore_data,
)


# Helper Function for Mongo URL
def get_mongo_url(message):
    if len(message.command) > 1:
        return message.command[1]
    return MONGO_DB_URI


# Commands
@app.on_message(filters.command(["mongochk"]))
async def mongo_check_command(client, message: Message):
    if len(message.command) < 2:
        await message.reply("Please provide your MongoDB URL with the command: `/mongochk your_mongo_url`")
        return
    ok = await message.reply_text("**Please wait, I am checking your MongoDB...**")
    mongo_url = message.command[1]

    try:
        with MongoClient(mongo_url, serverSelectionTimeoutMS=5000) as mongo_client:
            databases = mongo_client.list_database_names()
            result = f"**MongoDB URL** `{mongo_url}` **is valid**.\n\n**Available Databases:**\n"
            for db_name in databases:
                if db_name not in ["admin", "local"]:
                    result += f"\n`{db_name}`:\n"
                    db = mongo_client[db_name]
                    for col_name in db.list_collection_names():
                        result += f"  `{col_name}` ({db[col_name].count_documents({})} documents)\n"

        if len(result) > 4096:
            paste_url = await Bin(result)
            await ok.delete()
            await message.reply(f"**The database list is too long to send here. You can view it at:** {paste_url}")
        else:
            await ok.delete()
            await message.reply(result)

    except Exception as e:
        await ok.delete()
        await message.reply(f"**Failed to connect to MongoDB**\n\n**Your MongoDB is dead ❌**\n\n**Error:** `{e}`")


@app.on_message(filters.command(["deletedb", "deldb"]) & filters.user(OWNER_ID))
async def delete_db_command(client, message: Message):
    if len(message.command) < 2:
        await message.reply("Please provide the database or collection to delete.")
        return

    try:
        mongo_url = get_mongo_url(message)
        with MongoClient(mongo_url, serverSelectionTimeoutMS=5000) as mongo_client:
            databases_and_collections = list_databases(mongo_client)

            if message.command[1].lower() == "all":
                delete_all_databases(mongo_client)
                await message.reply("**All databases and collections have been deleted successfully. 🧹**")
            else:
                await message.reply("Invalid command format.")
    except Exception as e:
        await message.reply(f"**Failed to delete databases:** {e}")


@app.on_message(filters.command(["transferdb"]) & filters.user(OWNER_ID))
async def transfer_db_command(client, message: Message):
    if len(message.command) < 3:
        await message.reply("Please provide both source and target MongoDB URLs.")
        return

    main_mongo_url = message.command[1]
    target_mongo_url = message.command[2]

    if not re.match(r"mongodb(?:\+srv)?:\/\/[^\s]+", target_mongo_url):
        await message.reply("**The target MongoDB URL format is invalid! ❌**")
        return

    try:
        with MongoClient(main_mongo_url, serverSelectionTimeoutMS=5000) as main_client:
            backup_data = backup_database(main_client)
        with MongoClient(target_mongo_url, serverSelectionTimeoutMS=5000) as target_client:
            restore_data(target_client, backup_data)

        await message.reply("**Data transfer to the new MongoDB is successful! 🎉**")
    except Exception as e:
        await message.reply(f"**Data transfer failed:** {e}")