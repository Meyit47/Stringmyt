import asyncio
import importlib

from pyrogram import idle

from StringGen import LOGGER, Alone
from StringGen.modules import ALL_MODULES


async def alone_boot():
    try:
        await Alone.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("StringGen.modules." + all_module)

    LOGGER.info(f"@{Alone.username} Started.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(alone_boot())
    LOGGER.info("Stopping String Gen Bot...")
