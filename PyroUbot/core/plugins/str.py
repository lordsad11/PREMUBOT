import asyncio
from datetime import datetime
from gc import get_objects
from time import time

from pyrogram.raw.functions import Ping
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import *



async def ping_cmd(client, message):
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    uptime = await get_time((time() - start_time))
    delta_ping = round((end - start).microseconds / 100000, 2)
    
    emot_1 = await get_vars(client.me.id, "EMOJI_PING")
    emot_2 = await get_vars(client.me.id, "EMOJI_UPTIME")
    emot_3 = await get_vars(client.me.id, "EMOJI_MENTION")
    emot_ping = emot_1 if emot_1 else "5269563867305879894"
    emot_uptime = emot_2 if emot_2 else "5971944878815317190"
    emot_owner = emot_3 if emot_3 else "5467406098367521267"
    
    if client.me.is_premium:
        _ping = f"""
<b><emoji id={emot_ping}>🏓</emoji>ᴘᴏɴɢ:</b> <code>{delta_ping} ms</code>
<b><emoji id={emot_uptime}>🕒</emoji>ᴜᴘᴛɪᴍᴇ: - <code>{uptime}</code></b>
<b><emoji id={emot_owner}>👑</emoji>ᴏᴡɴᴇʀ:</b> <code>{client.me.mention}</code>
"""
    else:
        _ping = f"""
<b>ᴘɪɴɢ:</b> <code>{delta_ping} ms</code>
<b>ᴜᴘᴛɪᴍᴇ: - <code>{uptime}</code></b>
<b>ᴜsᴇʀ:</b> <code>{client.me.mention}</code>
"""
    await message.reply(_ping)

async def start_cmd(client, message):
    if len(message.command) < 2:
        buttons = Button.start(message)
        msg = MSG.START(message)
        await message.reply(msg, reply_markup=InlineKeyboardMarkup(buttons))
    else:
        txt = message.text.split(None, 1)[1]
        msg_id = txt.split("_", 1)[1]
        send = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ...</b>")
        if "secretMsg" in txt:
            try:
                m = [obj for obj in get_objects() if id(obj) == int(msg_id)][0]
            except Exception as error:
                return await send.edit(f"<b>❌ ᴇʀʀᴏʀ:</b> <code>{error}</code>")
            user_or_me = [m.reply_to_message.from_user.id, m.from_user.id]
            if message.from_user.id not in user_or_me:
                return await send.edit(
                    f"<b>❌ ᴘᴇsᴀɴ ɪɴɪ ʙᴜᴋᴀɴ ᴜɴᴛᴜᴋᴍᴜ <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>"
                )
            else:
                text = await client.send_message(
                    message.chat.id,
                    m.text.split(None, 1)[1],
                    protect_content=True,
                    reply_to_message_id=message.id,
                )
                await send.delete()
                await asyncio.sleep(120)
                await message.delete()
                await text.delete()
        elif "copyMsg" in txt:
            try:
                m = [obj for obj in get_objects() if id(obj) == int(msg_id)][0]
            except Exception as error:
                return await send.edit(f"<b>❌ ᴇʀʀᴏʀ:</b> <code>{error}</code>")
            id_copy = int(m.text.split()[1].split("/")[-1])
            if "t.me/c/" in m.text.split()[1]:
                chat = int("-100" + str(m.text.split()[1].split("/")[-2]))
            else:
                chat = str(m.text.split()[1].split("/")[-2])
            try:
                get = await client.get_messages(chat, id_copy)
                await get.copy(message.chat.id, reply_to_message_id=message.id)
                await send.delete()
            except Exception as error:
                await send.edit(error)
                
