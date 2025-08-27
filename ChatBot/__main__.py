import importlib

from pyrogram import idle

from ChatBot import app
from ChatBot.modules import ALL_MODULES

async def boot():
    await app.start()

    for module in ALL_MODULES:
        importlib.import_module(f"ChatBot.modules.{module}")

    await idle()
    await app.stop()

if __name__ == "__main__":
    app.run(boot())
