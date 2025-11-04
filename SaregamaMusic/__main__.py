import asyncio
from pyrogram import Client
from pytgcalls import PyTgCalls

from SaregamaMusic import app  # apni file/module ka name yahan likho

async def main():
    await app.start()
    print("Bot started successfully!")
    await idle()  # agar tum pytgcalls ya async loop use kar rahe ho
    await app.stop()

if name == "main":
    asyncio.run(main())
