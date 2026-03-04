import logging
import asyncio

from pyrogram import Client, idle
from pyrogram.errors import BadMsgNotification

from config import TOKEN, disabled_plugins, API_ID, API_HASH
from utils import get_restarted, del_restarted

with open("version.txt") as f:
    version = f.read().strip()


async def main():
    client = Client(
        "Cv_TALASHNY",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=TOKEN,
        workers=24,
        plugins=dict(root="plugins", exclude=disabled_plugins)
    )

    async with client:
        wr = get_restarted()
        del_restarted()
        try:
            print(f"Bot started\nVersion: {version}")
            if wr:
                await client.edit_message_text(wr[0], wr[1], "Restarted successfully.")
        except Exception:
            logging.warning("Unable to send startup message.")
        await idle()


if __name__ == "__main__":
    asyncio.run(main())
