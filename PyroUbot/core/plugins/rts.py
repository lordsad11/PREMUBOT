import importlib

from PyroUbot import *


async def restart_cmd(client, message):
    msg = await message.reply("<b>Tunggu Sebentar Sayang</b>", quote=True)
    if message.from_user.id not in ubot._get_my_id:
        return await msg.edit(
            f"<b>ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ. ᴅɪᴋᴀʀᴇɴᴀᴋᴀɴ ᴀɴᴅᴀ ʙᴜᴋᴀɴ ᴘᴇɴɢɢᴜɴᴀ @{bot.me.username}</b>"
        )
    for X in ubot._ubot:
        if message.from_user.id == X.me.id:
            for _ubot_ in await get_userbots():
                if X.me.id == int(_ubot_["name"]):
                    try:
                        ubot._ubot.remove(X)
                        ubot._get_my_id.remove(X.me.id)
                        UB = Ubot(**_ubot_)
                        await UB.start()
                        for mod in loadModule():
                            importlib.reload(
                                importlib.import_module(f"PyroUbot.modules.{mod}")
                            )
                        return await msg.edit(
                            f"<b>✅ Udah berhasil restart nih bub {UB.me.first_name} {UB.me.last_name or ''} | {UB.me.id}</b>"
                        )
                    except Exception as error:
                        return await msg.edit(f"<b>{error}</b>")
