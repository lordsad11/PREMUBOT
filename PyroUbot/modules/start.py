from .. import *


@PY.UBOT("ping")
async def _(client, message):
    await ping_cmd(client, message)
@bots.on_message(filters.user(DEVS) & filters.command("Cping", "") & ~filters.me)

@PY.BOT("start")
@PY.PRIVATE
async def _(client, message):
    await start_cmd(client, message)
