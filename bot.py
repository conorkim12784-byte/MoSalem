import logging
import os
import time

from pyrogram import Client, idle, enums
from pyrogram.errors.exceptions.bad_request_400 import BadRequest

from config import TOKEN, disabled_plugins, API_ID, API_HASH
from utils import get_restarted, del_restarted

with open("version.txt") as f:
    version = f.read().strip()

client = Client(
    "Cv_TALASHNY",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
    workers=24,
    plugins=dict(root="plugins", exclude=disabled_plugins)
)

with client:
    if __name__ == "__main__":
        wr = get_restarted()
        del_restarted()
        try:
            print(f"Bot started\nVersion: {version}")
            if wr:
                client.edit_message_text(wr[0], wr[1], "Restarted successfully.")
        except BadRequest:
            logging.warning("Unable to send message to log_chat.")
        idle()
